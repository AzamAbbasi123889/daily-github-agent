"""
Project generator logic.

Handles selecting an unused project, tracking history,
and writing generated files to disk.
"""

import os
import json
import datetime
from pathlib import Path
from typing import Dict, Any, Optional

from . import config
from .project_catalog import get_catalog
from .content_generators import generate_files


class ProjectHistory:
    """Manages project history to prevent duplicates."""

    def __init__(self, history_file: str = config.PROJECT_HISTORY_FILE):
        self.history_file = Path(history_file)
        self._history = self._load()

    def _load(self) -> Dict[str, Any]:
        """Load history from JSON file."""
        if self.history_file.exists():
            try:
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                pass
        return {"projects": []}

    def save(self):
        """Save history to JSON file."""
        self.history_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.history_file, 'w', encoding='utf-8') as f:
            json.dump(self._history, f, indent=4)

    def is_generated(self, project_name: str) -> bool:
        """Check if a project name has already been generated."""
        return any(p["name"] == project_name for p in self._history["projects"])

    def record_project(self, project_data: Dict[str, Any]):
        """Record a successfully generated and pushed project."""
        record = {
            "name": project_data["name"],
            "repository": project_data.get("repository", project_data["name"]),
            "github_url": project_data.get("github_url", ""),
            "created_at": datetime.datetime.now().isoformat(),
            "category": project_data["category"],
            "difficulty": project_data.get("difficulty", "Unknown"),
            "language": "Python",
            "status": "created",
        }
        self._history["projects"].append(record)
        self.save()


class ProjectGenerator:
    """Core project generation engine."""

    def __init__(self):
        self.catalog = get_catalog()
        self.history = ProjectHistory()

    def select_project(self, target_name: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """
        Select an unused project from the catalog.
        If target_name is provided, try to select that one specifically.
        """
        if target_name:
            for project in self.catalog:
                if project["name"] == target_name:
                    if not self.history.is_generated(project["name"]):
                        return project
            return None

        # Select first unused project
        for project in self.catalog:
            if not self.history.is_generated(project["name"]):
                return project

        return None

    def create_project_on_disk(self, project: Dict[str, Any]) -> str:
        """
        Generate all project files and write them to disk.
        
        Args:
            project: Project metadata dict.
            
        Returns:
            Absolute path to the created project directory.
        """
        project_name = project["name"]
        
        # Ensure name is safe (lowercase, hyphens)
        safe_name = project_name.lower().replace(" ", "-")
        safe_name = "".join(c for c in safe_name if c.isalnum() or c == "-")
        project["name"] = safe_name
        
        # Determine output directory
        out_dir = Path(config.PROJECTS_DIRECTORY) / safe_name
        
        # If the directory already exists, it might be from a failed previous run.
        # We can either clean it or just overwrite files.
        # For safety, we will just overwrite/add files.
        out_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate file contents
        files = generate_files(project)
        
        # Write files
        for rel_path, content in files.items():
            filepath = out_dir / rel_path
            filepath.parent.mkdir(parents=True, exist_ok=True)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
                
        return str(out_dir.absolute())
