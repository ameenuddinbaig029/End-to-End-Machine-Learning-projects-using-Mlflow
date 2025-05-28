import os 
from pathlib import Path
import logging

# ------------------------------------------------------------------------------
# Project Setup Automation Script
#
# 📌 Purpose:
# This script auto-generates the folder and file structure for a new Python project.
# It creates boilerplate directories, empty modules, and configuration files.
# Ideal for consistent project setup with Git, DVC, Docker, etc.
#
# ⚙️ Usage:
# Run this script once at the start of your project:
#     python template.py my_project_name
#
# 🛠 Example Commands to Automate Further (optional):
#     git init                      # Initialize a new Git repository
#     dvc init                      # Initialize DVC tracking
#     python -m venv venv          # Create a virtual environment
#     pip install -r requirements.txt  # Install project dependencies
#     dvc add data/                # Track data with DVC
#     git add . && git commit -m "Initial project structure"  # First commit
# -------------------------------------------------------------------------------

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')


# Project Name
project_name = "mlproject"

# List of files 

list_of_files = [

    # Core source files
    # ------------------------------------------------------------------------------
    # "__init__.py" this file in every folder it try to makes a folder as a python package and This file marks the folder as a Python package.(Constructer)
    # It allows the folder's modules to be imported using dot notation.
    # Keeping this file (even if empty) ensures smooth imports and compatibility.
    # ------------------------------------------------------------------------------
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",

    # Configuration files
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "schema.yaml",

    # Root scripts and setup
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",

    # Research and web templates
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"
]



# Logic to Develop this Project Structure

for filepath in list_of_files:
    # Convert the string path to a Path object for cross-platform compatibility
    filepath = Path(filepath)

    # Split the path into directory and filename
    filedir, filename = os.path.split(filepath)

    # If the file has a directory, create the directory if it doesn't already exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Check if the file doesn't exist OR is an empty file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Create an empty file
        with open(filepath, "w") as f:
            pass  # File is created but left empty
            logging.info(f"Creating empty file: {filepath}")
    else:
        # If file already exists and is not empty, log a message
        logging.info(f"{filename} already exists")

