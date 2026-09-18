"""
Daily GitHub Agent - AI/ML Project Factory.
Main entry point.
"""

import argparse
from app.orchestrator import Orchestrator


def main():
    parser = argparse.ArgumentParser(description="Daily GitHub Agent - Project Factory")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Run the pipeline locally without making changes to GitHub or history"
    )
    parser.add_argument(
        "--target",
        type=str,
        default="ai-resume-analyzer",
        help="Target project name to generate (if available)"
    )
    
    args = parser.parse_args()
    
    orchestrator = Orchestrator(dry_run=args.dry_run)
    orchestrator.run(target_project=args.target)


if __name__ == "__main__":
    main()
