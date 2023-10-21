import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s')

project = "Machine Learning Project"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project}/_init_.py",
    f"src/{project}/components/_init_.py",
    f"src/{project}/utils/_init_.py",
    f"src/{project}/utils/common.py",
    f"src/{project}/config/_init_.py",
    f"src/{project}/config/configuration.py",
    f"src/{project}/pipeline/_init_.py",
    f"src/{project}/entity/_init_.py",
    f"src/{project}/entity/config_entity.py",
    f"src/{project}/constants/_init_.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory;{filedir} for the file: {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
            
    else:
        logging.info(f"{filename} is already exists")
    