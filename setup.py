from setuptools import setup, find_packages

setup(
    name="git-batch-commit",
    version="1.0.2",
    author="Vaishal",
    description="A powerful Git batch commit tool that stages, commits, and pushes files in customizable batches.",
    long_description="""
# Git Batch Commit

Git Batch Commit is an advanced Python-based command-line tool designed to automate and simplify batch staging, 
committing, and pushing files in Git repositories. Ideal for developers working with a large number of files, 
it allows users to control the number of files per commit, reducing performance issues and making version 
control more efficient.

## Features:
- **Batch Staging & Committing** – Stage and commit files in user-defined batch sizes.
- **Interactive CLI** – Users can choose the number of files to commit at each step.
- **Automated Push** – Commits are automatically pushed to the remote repository.
- **Error Handling** – Prevents common Git errors, such as missing staged files.
- **Custom Commit Messages** – Users can provide their own commit messages or use generated ones.
- **Cross-Platform** – Works on Windows, macOS, and Linux.

## Installation:
You can install Git Batch Commit via `pip`:
```sh
pip install git-batch-commit
```

## Usage:
Once installed, you can run the tool using:
```sh
git-batch-commit
```
Follow the interactive prompts to stage, commit, and push files.

## Requirements:
- Python 3.6 or later
- Git installed and configured

## License:
This project is licensed under the MIT License.

## Author:
Developed by Vaishal.
    """,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
             "git-batch-commit=git_batch_commit.__main__:batch_commit"
        ]
    },
    install_requires=[
        "gitpython",  # Ensures GitPython is installed for handling Git operations
        "rich"  # Enhances CLI output with colors and formatting
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Version Control :: Git",
    ],
    python_requires=">=3.6",
    project_urls={
        "GitHub": "https://github.com/Vaishal-Business/git-batch-commit",
    },
)
