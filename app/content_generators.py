"""
AI Code Review Assistant - Main Entry Point

Analyzes Python code for bugs, style issues, complexity,
and security vulnerabilities using AST analysis.
"""

import os
import sys
from src.analyzer import CodeAnalyzer
from src.reporter import format_report

SAMPLE_CODE = """
import os
import pickle


def process_data(data, flag=True):
    result = []
    for i in range(len(data)):
        item = data[i]
        if flag == True:
            if item != None:
                try:
                    val = eval(item)
                    result.append(val)
                except:
                    pass

    password = os.getenv("PASSWORD")
    db_url = os.getenv("DATABASE_URL")
    return result


class DataProcessor:
    def __init__(self):
        self.data = []

    def add(self, item):
        self.data.append(item)

    def process(self):
        for i in range(len(self.data)):
            x = self.data[i]
            if type(x) == str:
                print(x)
"""


def main():
    """Run code analysis on sample code."""
    print("=" * 60)
    print("AI Code Review Assistant")
    print("=" * 60)

    analyzer = CodeAnalyzer()
    results = analyzer.analyze(SAMPLE_CODE)
    report = format_report(results)
    print(report)


if __name__ == "__main__":
    main()
