import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

ProjectName = 'TextSummarizer'

# Create project directory

list_of_files = [
    '.github/workflows/.gitkeep',
    f'src/{ProjectName}/__init__.py',
    f'src/{ProjectName}/components/__init__.py',
    f'src/{ProjectName}/utils/__init__.py',
    f'src/{ProjectName}/config/__init__.py',
    f'src/{ProjectName}/config/configuration.py',
    f'src/{ProjectName}/pipeline/__init__.py',
    f'src/{ProjectName}/entity/__init__.py',
    f'src/{ProjectName}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'app.py',
    'main.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/trails.ipynb'
    # Add more files as needed
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir}")
    
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:
            pass  # Create an empty file
        logging.info(f"Created file: {filepath}")
    else:
        logging.info(f"File already exists and is not empty: {filepath}")