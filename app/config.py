"""
Configuration module for Daily GitHub Agent.

Loads settings from environment variables with sensible defaults.
No secrets are stored in this file — GitHub auth comes from the CLI.
"""

import os
from pathlib import Path


# Base directory is the project root (parent of app/)
BASE_DIR = Path(__file__).resolve().parent.parent

# Project generation settings
PROJECTS_DIRECTORY = os.getenv(
    "PROJECTS_DIRECTORY",
    str(BASE_DIR / "generated_projects")
)

PROJECT_HISTORY_FILE = os.getenv(
    "PROJECT_HISTORY_FILE",
    str(BASE_DIR / "data" / "projects.json")
)

# GitHub settings
GITHUB_DEFAULT_VISIBILITY = os.getenv("GITHUB_DEFAULT_VISIBILITY", "public")

# Ensure directories exist
Path(PROJECTS_DIRECTORY).mkdir(parents=True, exist_ok=True)
Path(PROJECT_HISTORY_FILE).parent.mkdir(parents=True, exist_ok=True)
