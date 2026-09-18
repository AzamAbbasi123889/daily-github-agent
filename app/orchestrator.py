"""
Orchestrator for the Daily GitHub Agent.

Coordinates the complete pipeline:
A. Check GitHub authentication
B. Generate unused project idea
C. Create project directory
D. Generate project files
E. Validate project
F. Initialize Git
G. Create NEW GitHub repository
H. Push project
I. Record successful creation
J. Print final report
"""

import sys
from typing import Optional

from . import github_manager
from .project_generator import ProjectGenerator
from .project_validator import validate_project


class Orchestrator:
    """Manages the end-to-end execution pipeline."""

    def __init__(self, dry_run: bool = False):
        """
        Initialize the orchestrator.
        
        Args:
            dry_run: If True, skips actual GitHub repository creation and pushing.
        """
        self.dry_run = dry_run
        self.generator = ProjectGenerator()

    def run(self, target_project: Optional[str] = "ai-resume-analyzer"):
        """Run one complete generation cycle."""
        print("=" * 60)
        print("DAILY GITHUB AGENT - EXECUTION PIPELINE")
        if self.dry_run:
            print("[DRY RUN MODE - NO GITHUB CHANGES WILL BE MADE]")
        print("=" * 60)

        try:
            # STEP A: Check GitHub authentication
            print("\\n[STEP A] Checking GitHub authentication...")
            github_manager.verify_auth()
            username = github_manager.get_username()
            print(f"  [OK] Authenticated as: {username}")

            # STEP B: Generate an unused project idea
            print("\\n[STEP B] Selecting unused project...")
            
            # Try to get the specific target project first
            project = None
            if target_project:
                project = self.generator.select_project(target_project)
                if not project:
                    print(f"  [INFO] Target project '{target_project}' is already generated. Selecting next available.")
            
            # If target project was taken or not provided, pick the next available
            if not project:
                project = self.generator.select_project()
                
            if not project:
                print("  [ERROR] No unused projects available in the catalog.")
                sys.exit(1)
                
            repo_name = project["name"]
            print(f"  [OK] Selected project: {project['name']} ({project['category']})")

            # Check if repository already exists on GitHub to avoid conflicts
            print(f"  [OK] Checking GitHub for existing repository '{repo_name}'...")
            if github_manager.repo_exists(repo_name):
                print(f"  [INFO] Repository '{repo_name}' already exists on GitHub.")
                print(f"  [INFO] Finding alternative project...")
                
                # We need to find one that doesn't exist on GitHub either
                found_valid = False
                for p in self.generator.catalog:
                    if not self.generator.history.is_generated(p["name"]) and not github_manager.repo_exists(p["name"]):
                        project = p
                        repo_name = project["name"]
                        found_valid = True
                        break
                
                if not found_valid:
                    print("  [ERROR] Could not find a project name that doesn't exist on GitHub.")
                    sys.exit(1)
                    
                print(f"  [OK] Selected alternative project: {project['name']}")

            # STEPS C & D: Create directory and generate files
            print("\\n[STEP C & D] Generating project files on disk...")
            project_dir = self.generator.create_project_on_disk(project)
            print(f"  [OK] Project generated at: {project_dir}")

            # STEP E: Validate the project
            print("\\n[STEP E] Validating generated project...")
            validation_result = validate_project(project_dir)
            if not validation_result["valid"]:
                print("  [ERROR] Project validation failed:")
                for error in validation_result["errors"]:
                    print(f"    - {error}")
                print("\\nStopping pipeline to prevent invalid push.")
                sys.exit(1)
            print("  [OK] Validation passed (structure, syntax, secrets)")

            # STEPS F, G, H: Git init, repo creation, and push
            print("\\n[STEP F, G, H] Creating GitHub repository and pushing...")
            if self.dry_run:
                print("  [OK] [DRY RUN] Skipping actual git init, commit, and push.")
                print(f"  [OK] [DRY RUN] Would create public repository: {repo_name}")
                github_url = f"https://github.com/{username}/{repo_name} (DRY RUN)"
            else:
                try:
                    github_url = github_manager.create_and_push(
                        project_dir=project_dir,
                        repo_name=repo_name,
                        description=project["description"]
                    )
                    print(f"  [OK] Successfully pushed to GitHub: {github_url}")
                except github_manager.GitHubError as e:
                    print("  [ERROR] GitHub operation failed:")
                    print(f"    Command: {e.command}")
                    print(f"    Error:   {e.stderr}")
                    sys.exit(1)

            # STEP I: Record successful creation
            print("\\n[STEP I] Recording project in history...")
            if self.dry_run:
                print("  [OK] [DRY RUN] Skipping recording to history.")
            else:
                project["repository"] = repo_name
                project["github_url"] = github_url
                self.generator.history.record_project(project)
                print("  [OK] History updated")

            # STEP J: Print final report
            print("\\n\\n" + "=" * 50)
            print("DAILY GITHUB AGENT - SUCCESS")
            print("=" * 50)
            print(f"Project:    {project['name'].replace('-', ' ').title()}")
            print(f"Repository: {repo_name}")
            print(f"Category:   {project['category']}")
            print(f"Difficulty: {project['difficulty']}")
            print(f"Language:   Python")
            print(f"Status:     SUCCESS")
            print(f"GitHub:     {github_url}")
            print("=" * 50 + "\\n")

        except Exception as e:
            print(f"\\n[ERROR] Unexpected error in orchestrator: {e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)
