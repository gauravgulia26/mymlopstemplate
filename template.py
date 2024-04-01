from pathlib import Path
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir = filepath.parent
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logger.info(f"Created directory: {filedir}")

    if (not filepath.exists()) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # create an empty file
