# setup.py
# 📦 This file is used to define the configuration for building and distributing your Python package.
# It tells setuptools how to install your project, what it contains, who wrote it, and where it's located.

import setuptools  # Import setuptools — the standard tool for packaging Python projects.

# 📖 Read the README.md file to use as the long description for your package (e.g., shown on PyPI).
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# 🏷️ Define your current version here. You should increment this with every new release.
__version__ = "0.0.0"

# ℹ️ Define your metadata — details about your project.
REPO_NAME = "End-to-End-Machine-Learning-projects-using-Mlflow"  # Your GitHub repository name.
AUTHOR_USER_NAME = "Ameenuddin"  # Your GitHub username or full name.
SRC_REPO = "mlproject"  # The name of the source code directory that contains your package.
AUTHOR_EMAIL = "ameenuddinbaig029@gmail.com"  # Your contact email.

# 🔧 Main configuration for your package
setuptools.setup(
    name=SRC_REPO,  # The installable package name (shown when someone installs it via pip)
    version=__version__,  # Package version (used for release tracking)
    author=AUTHOR_USER_NAME,  # Package author (you)
    author_email=AUTHOR_EMAIL,  # Author's email for support/contact
    description="A small Python package for ML app using MLflow",  # Short summary of what your package does
    long_description=long_description,  # The content from README.md for detailed description
    long_description_content_type="text/markdown",  # Specifies the README format (Markdown in this case)
    
    # 🔗 URLs for users to find more info about your project
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # Main GitHub repo link
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",  # Where to report issues
    },

    # 📂 Define where your actual source code is located
    package_dir={"": "src"},  # Tells setuptools that all packages are under the "src/" folder
    packages=setuptools.find_packages(where="src"),  # Automatically finds all packages inside "src/"

    # 🏷️ Classifiers help others discover your package. Choose appropriate ones from PyPI's list.
    classifiers=[
        "Programming Language :: Python :: 3",  # The Python version you're using
        "License :: OSI Approved :: MIT License",  # The license type (MIT in this case)
        "Operating System :: OS Independent",  # Your package can run on any OS
    ],

    # ✅ This ensures the user has at least this version of Python to use your package
    python_requires='>=3.7',  # Minimum supported Python version
)

"""
🧠 Why we use setup.py:
1. 📦 We use `setup.py` to package our Python project so it can be easily installed and shared with others (or reused in other projects).

2. ✅ Benefit of using setup.py:
   It allows us to install the project locally using `pip install -e .`, so any code changes are reflected immediately without needing to reinstall.

3. ❌ Problem before using setup.py:
   Without it, we had to manually set `PYTHONPATH`, manage imports with hacks, or copy/paste files — which was error-prone and unscalable.

4. 🛠️ How setup.py fixes it:
   It tells `setuptools` how to structure, install, and recognize our project as a Python package. This automates the process and makes our codebase cleaner and reusable.
"""
