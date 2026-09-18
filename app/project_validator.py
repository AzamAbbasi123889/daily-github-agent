"""
Project validator for Daily GitHub Agent.

Validates generated projects before GitHub push:
- Directory and file existence checks
- File non-emptiness checks
- Python syntax validation via ast.parse()
- Secret/credential pattern scanning
"""

import ast
import re
from pathlib import Path
from typing import Dict, List, Any


# Patterns that might indicate leaked secrets
SECRET_PATTERNS = [
    (r'sk-[a-zA-Z0-9]{20,}', 'OpenAI API key pattern'),
    (r'ghp_[a-zA-Z0-9]{36}', 'GitHub personal access token'),
    (r'gho_[a-zA-Z0-9]{36}', 'GitHub OAuth token'),
    (r'ghs_[a-zA-Z0-9]{36}', 'GitHub server token'),
    (r'AKIA[0-9A-Z]{16}', 'AWS access key ID'),
    (r'AIza[0-9A-Za-z\-_]{35}', 'Google API key pattern'),
    (r'-----BEGIN\s+(RSA\s+)?PRIVATE\s+KEY-----', 'Private key'),
    (r'password\s*=\s*["\'][^"\']+["\']', 'Hardcoded password'),
    (r'secret\s*=\s*["\'][^"\']+["\']', 'Hardcoded secret'),
    (r'token\s*=\s*["\'][a-zA-Z0-9]{20,}["\']', 'Hardcoded token'),
]

# Files that should never appear in generated projects
FORBIDDEN_FILES = [
    '.env',
    'credentials.json',
    'service-account.json',
    'id_rsa',
    'id_ed25519',
]


def validate_project(project_dir: str) -> Dict[str, Any]:
    """
    Validate a generated project before GitHub push.

    Args:
        project_dir: Path to the generated project directory.

    Returns:
        Dict with 'valid' (bool) and 'errors' (list of str).
    """
    errors: List[str] = []
    project_path = Path(project_dir)

    # 1. Directory existence
    if not project_path.exists():
        return {"valid": False, "errors": [f"Project directory does not exist: {project_dir}"]}

    if not project_path.is_dir():
        return {"valid": False, "errors": [f"Path is not a directory: {project_dir}"]}

    # 2. Required files
    required_files = ["README.md", "requirements.txt", "main.py"]
    for filename in required_files:
        filepath = project_path / filename
        if not filepath.exists():
            errors.append(f"Required file missing: {filename}")
        elif filepath.stat().st_size == 0:
            errors.append(f"Required file is empty: {filename}")

    # 3. Validate Python syntax
    for py_file in project_path.rglob("*.py"):
        try:
            source = py_file.read_text(encoding="utf-8")
            ast.parse(source)
        except SyntaxError as e:
            rel = py_file.relative_to(project_path)
            errors.append(f"{rel} contains invalid Python syntax: {e.msg} (line {e.lineno})")
        except Exception as e:
            rel = py_file.relative_to(project_path)
            errors.append(f"{rel} could not be read: {e}")

    # 4. Check for forbidden files
    for forbidden in FORBIDDEN_FILES:
        if (project_path / forbidden).exists():
            errors.append(f"Forbidden file found: {forbidden}")

    # 5. Scan for secrets
    for text_file in _iter_text_files(project_path):
        try:
            content = text_file.read_text(encoding="utf-8", errors="ignore")
            rel = text_file.relative_to(project_path)
            _scan_for_secrets(str(rel), content, errors)
        except Exception:
            pass

    # 6. Check .gitignore exists and contains .env
    gitignore = project_path / ".gitignore"
    if gitignore.exists():
        gi_content = gitignore.read_text(encoding="utf-8", errors="ignore")
        if ".env" not in gi_content:
            errors.append(".gitignore does not exclude .env files")
    else:
        errors.append(".gitignore file is missing")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
    }


def _iter_text_files(project_path: Path):
    """Yield text files in the project (skip binary files)."""
    text_extensions = {
        ".py", ".txt", ".md", ".yml", ".yaml", ".json",
        ".toml", ".cfg", ".ini", ".sh", ".bat", ".env",
        ".html", ".css", ".js", ".ts", ".jsx", ".tsx",
    }
    for f in project_path.rglob("*"):
        if f.is_file() and f.suffix.lower() in text_extensions:
            yield f


def _scan_for_secrets(filename: str, content: str, errors: List[str]):
    """Scan file content for secret patterns."""
    for pattern, description in SECRET_PATTERNS:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            # Skip matches inside comments or example placeholders
            for match in matches:
                match_str = match if isinstance(match, str) else match[0]
                # Allow placeholder patterns like "your-key-here"
                if "your" in match_str.lower() or "example" in match_str.lower():
                    continue
                # Allow patterns in .env.example
                if filename.endswith(".env.example"):
                    continue
                errors.append(
                    f"Possible secret in {filename}: {description}"
                )
                break  # One warning per pattern per file is enough
