# To create folder structure automatically i.e. creating Project template

import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO,
                    format = '[%(asctime)s]: %(message)s:')

# list of files and folders required
# can add name of the additional files/folders required and rerun this file
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "requirement.txt",
    "setup.py",
    "research/trials.ipynb",
    "app.py"
]

# To take care of OS while using path to create folder structure
for filepath in list_of_files:
    filepath=Path(filepath) # To take care of OS while using path to create folder structure
    filedir, filename = os.path.split(filepath)   # separate out file from folders

    if filedir != "":
        os.makedirs(filedir, exist_ok= True)  #if already exists then do not create again
        logging.info(f"Creating directory {filedir} for the files{filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file : {filepath}")

    else:
        logging.info(f"{filename} already exists!")



