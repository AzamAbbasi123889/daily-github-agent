"""
GitHub Manager for Daily GitHub Agent.

All GitHub operations use the GitHub CLI (gh) via subprocess.
No tokens are stored or hardcoded — authentication comes from gh auth.

Security rules:
- No shell=True in subprocess calls
- No gh repo delete anywhere
- All errors captured with stderr
- Never prints or logs tokens
"""

import subprocess
import re
from pathlib import Path
from typing import Optional, Tuple

from . import config


class GitHubError(Exception):
    """Raised when a GitHub CLI operation fails."""

    def __init__(self, message: str, command: str = "", stderr: str = "",
                 returncode: int = -1):
        super().__init__(message)
        self.command = command
        self.stderr = stderr
        self.returncode = returncode


def _run_command(
    args: list,
    cwd: Optional[str] = None,
    check: bool = True,
) -> subprocess.CompletedProcess:
    """
    Run a subprocess command safely.

    Uses argument arrays (no shell=True).
    Captures stdout and stderr.
    """
    try:
        result = subprocess.run(
            args,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=120,
        )
        if check and result.returncode != 0:
            cmd_str = " ".join(args)
            raise GitHubError(
                message=f"Command failed: {cmd_str}",
                command=cmd_str,
                stderr=result.stderr.strip(),
                returncode=result.returncode,
            )
        return result
    except subprocess.TimeoutExpired:
        cmd_str = " ".join(args)
        raise GitHubError(
            message=f"Command timed out: {cmd_str}",
            command=cmd_str,
            stderr="Timeout after 120 seconds",
        )
    except FileNotFoundError:
        cmd_str = " ".join(args)
        raise GitHubError(
            message=f"Command not found: {args[0]}",
            command=cmd_str,
            stderr=f"'{args[0]}' is not installed or not in PATH",
        )


def verify_auth() -> bool:
    """
    Verify that GitHub CLI is authenticated.

    Returns:
        True if authenticated.

    Raises:
        GitHubError if not authenticated.
    """
    result = _run_command(["gh", "auth", "status"], check=False)
    combined = result.stdout + result.stderr

    if result.returncode != 0 or "not logged in" in combined.lower():
        raise GitHubError(
            message="GitHub CLI is not authenticated. Run: gh auth login",
            command="gh auth status",
            stderr=result.stderr.strip(),
            returncode=result.returncode,
        )
    return True


def get_username() -> str:
    """
    Get the authenticated GitHub username.

    Returns:
        The GitHub username string.

    Raises:
        GitHubError if username cannot be determined.
    """
    result = _run_command(["gh", "api", "user", "--jq", ".login"])
    username = result.stdout.strip()

    if not username:
        raise GitHubError(
            message="Could not determine GitHub username",
            command="gh api user --jq .login",
            stderr=result.stderr.strip(),
        )
    return username


def repo_exists(repo_name: str) -> bool:
    """
    Check whether a repository already exists under the authenticated account.

    Args:
        repo_name: The repository name to check.

    Returns:
        True if the repository exists, False otherwise.
    """
    username = get_username()
    result = _run_command(
        ["gh", "repo", "view", f"{username}/{repo_name}", "--json", "name"],
        check=False,
    )
    return result.returncode == 0


def create_and_push(
    project_dir: str,
    repo_name: str,
    visibility: Optional[str] = None,
    description: str = "",
) -> str:
    """
    Create a new GitHub repository and push the project.

    Steps:
    1. git init
    2. git add .
    3. git commit
    4. gh repo create (with --source and --push)

    Args:
        project_dir: Absolute path to the project directory.
        repo_name: Name for the new GitHub repository.
        visibility: 'public' or 'private'. Defaults to config setting.
        description: Repository description.

    Returns:
        The GitHub repository URL.

    Raises:
        GitHubError if any step fails.
    """
    if visibility is None:
        visibility = config.GITHUB_DEFAULT_VISIBILITY

    project_path = Path(project_dir)

    if not project_path.exists():
        raise GitHubError(f"Project directory does not exist: {project_dir}")

    # Check if repo already exists
    if repo_exists(repo_name):
        raise GitHubError(
            message=f"Repository '{repo_name}' already exists on GitHub",
            command="gh repo view",
            stderr="Repository already exists. Choose a different name.",
        )

    # Step 1: git init (skip if already initialized)
    git_dir = project_path / ".git"
    if not git_dir.exists():
        _run_command(["git", "init"], cwd=str(project_path))

    # Step 2: Configure git user if not set globally
    _ensure_git_config(str(project_path))

    # Step 3: git add all files
    _run_command(["git", "add", "."], cwd=str(project_path))

    # Step 4: git commit
    commit_msg = f"Initial commit: {repo_name}"
    _run_command(
        ["git", "commit", "-m", commit_msg],
        cwd=str(project_path),
    )

    # Step 5: Create repo and push
    create_args = [
        "gh", "repo", "create", repo_name,
        f"--{visibility}",
        "--source", ".",
        "--push",
    ]
    if description:
        create_args.extend(["--description", description])

    _run_command(create_args, cwd=str(project_path))

    # Step 6: Get the repository URL
    username = get_username()
    repo_url = f"https://github.com/{username}/{repo_name}"

    return repo_url


def _ensure_git_config(cwd: str):
    """Ensure git user.name and user.email are configured."""
    # Check if name is set
    result = _run_command(
        ["git", "config", "user.name"],
        cwd=cwd,
        check=False,
    )
    if result.returncode != 0 or not result.stdout.strip():
        # Use GitHub username as fallback
        try:
            username = get_username()
            _run_command(
                ["git", "config", "user.name", username],
                cwd=cwd,
            )
        except GitHubError:
            _run_command(
                ["git", "config", "user.name", "Daily GitHub Agent"],
                cwd=cwd,
            )

    # Check if email is set
    result = _run_command(
        ["git", "config", "user.email"],
        cwd=cwd,
        check=False,
    )
    if result.returncode != 0 or not result.stdout.strip():
        try:
            username = get_username()
            _run_command(
                ["git", "config", "user.email",
                 f"{username}@users.noreply.github.com"],
                cwd=cwd,
            )
        except GitHubError:
            _run_command(
                ["git", "config", "user.email",
                 "agent@daily-github-agent.local"],
                cwd=cwd,
            )
