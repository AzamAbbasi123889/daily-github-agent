"""
Unit tests for the project generator pipeline.
These tests validate logic without interacting with GitHub.
"""

import os
import tempfile
import unittest
import json
from pathlib import Path
from unittest.mock import patch

from app.project_generator import ProjectGenerator, ProjectHistory
from app.project_validator import validate_project
from app.project_catalog import get_catalog


class TestProjectCatalog(unittest.TestCase):
    
    def test_catalog_not_empty(self):
        catalog = get_catalog()
        self.assertGreater(len(catalog), 0)
        
    def test_catalog_structure(self):
        catalog = get_catalog()
        for project in catalog:
            self.assertIn("name", project)
            self.assertIn("description", project)
            self.assertIn("category", project)
            self.assertIn("difficulty", project)
            self.assertIn("tech_stack", project)
            self.assertIsInstance(project["tech_stack"], list)


class TestProjectHistory(unittest.TestCase):
    
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.history_file = Path(self.temp_dir.name) / "projects.json"
        
    def tearDown(self):
        self.temp_dir.cleanup()
        
    def test_empty_history(self):
        history = ProjectHistory(history_file=str(self.history_file))
        self.assertFalse(history.is_generated("some-project"))
        
    def test_record_project(self):
        history = ProjectHistory(history_file=str(self.history_file))
        history.record_project({
            "name": "test-project",
            "category": "Testing",
            "difficulty": "Beginner"
        })
        
        self.assertTrue(history.is_generated("test-project"))
        
        # Load from disk to verify
        with open(self.history_file, "r") as f:
            data = json.load(f)
            self.assertEqual(len(data["projects"]), 1)
            self.assertEqual(data["projects"][0]["name"], "test-project")


class TestProjectGenerator(unittest.TestCase):
    
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        # Patch config paths
        self.patcher1 = patch('app.config.PROJECTS_DIRECTORY', str(Path(self.temp_dir.name) / "projects"))
        self.patcher2 = patch('app.config.PROJECT_HISTORY_FILE', str(Path(self.temp_dir.name) / "history.json"))
        self.patcher1.start()
        self.patcher2.start()
        
        self.generator = ProjectGenerator()
        
    def tearDown(self):
        self.patcher1.stop()
        self.patcher2.stop()
        self.temp_dir.cleanup()
        
    def test_select_project(self):
        project = self.generator.select_project()
        self.assertIsNotNone(project)
        self.assertIn("name", project)
        
    def test_select_target_project(self):
        project = self.generator.select_project(target_name="ai-resume-analyzer")
        self.assertIsNotNone(project)
        self.assertEqual(project["name"], "ai-resume-analyzer")
        
    def test_create_project_on_disk(self):
        project = self.generator.select_project(target_name="ai-resume-analyzer")
        
        # Generate files
        out_dir = self.generator.create_project_on_disk(project)
        out_path = Path(out_dir)
        
        self.assertTrue(out_path.exists())
        self.assertTrue((out_path / "README.md").exists())
        self.assertTrue((out_path / "requirements.txt").exists())
        self.assertTrue((out_path / ".gitignore").exists())
        self.assertTrue((out_path / "main.py").exists())
        
        # Validate the generated project
        validation_result = validate_project(str(out_path))
        self.assertTrue(validation_result["valid"], f"Validation failed: {validation_result.get('errors')}")


if __name__ == '__main__':
    unittest.main()
