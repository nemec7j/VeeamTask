import os
import shutil
from utils import calculate_md5
from pathlib import Path
import logging


def sync_folders(source, replica):
    source_files = {str(file): calculate_md5(str(file)) for file in Path(source).rglob('*') if file.is_file()}
    replica_files = {str(file): calculate_md5(str(file)) for file in Path(replica).rglob('*') if file.is_file()}

    for s_file, s_hash in source_files.items():
        r_file = s_file.replace(source, replica)
        if r_file not in replica_files or s_hash != replica_files[r_file]:
            os.makedirs(os.path.dirname(r_file), exist_ok=True)
            shutil.copy2(s_file, r_file)
            logging.info(f'Copied or updated: {r_file}')

    for r_file in replica_files:
        s_file = r_file.replace(replica, source)
        if s_file not in source_files:
            os.remove(r_file)
            logging.info(f'Removed: {r_file}')
