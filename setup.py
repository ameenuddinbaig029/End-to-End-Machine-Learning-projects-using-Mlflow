import setuptools

# Read the content of your README file to use as the long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Package version
__version__ = "0.0.0"

# Project metadata
REPO_NAME = "End-to-End-Machine-Learning-projects-using-Mlflow"
AUTHOR_USER_NAME = "Ameenuddin"
SRC_REPO = "mlproject"
AUTHOR_EMAIL = "ameenuddinbaig029@gmail.com"

# Setup configuration
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small Python package for ML app using MLflow",
    long_description=long_description,
    long_description_content_type="text/markdown",  # 🔸 You missed this
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # 🔸 Missing slash before username
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[  # 🔸 Recommended for PyPI metadata and visibility
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',  # 🔸 Optional but good practice
)

