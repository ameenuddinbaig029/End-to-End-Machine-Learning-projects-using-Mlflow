import os
from box.exceptions import BoxValueError
from box import ConfigBox  # ✅ Needed to return ConfigBox in functions
import yaml
from src.mlproject import logger
import json
import joblib
from ensure import ensure_annotations
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object (dot-accessible dictionary).

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: For any other file-related issues.

    Returns:
        ConfigBox: Parsed YAML content.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates multiple directories.

    Args:
        path_to_directories (list): List of paths to create.
        verbose (bool): If True, logs the directory creation. Default is True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves a dictionary as a JSON file.

    Args:
        path (Path): Path where the JSON will be saved.
        data (dict): Dictionary to save.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads a JSON file and returns its contents as a ConfigBox.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: JSON content with dot-accessible keys.
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves data as a binary file using joblib.

    Args:
        data (Any): Object to save.
        path (Path): Destination path.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads data from a binary file.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: Loaded object.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Returns the file size in kilobytes.

    Args:
        path (Path): Path to the file.

    Returns:
        str: File size in KB (rounded).
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~{size_in_kb} KB"
