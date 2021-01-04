import os

from src import logger


def read_file(path):
    with open(path, "rb") as f:
        return f.read()


def save_file(path, data):
    dirname = os.path.dirname(path)
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    with open(path, "wb") as f:
        f.write(data)
        logger.info(f"File saved in '{path}'.")


def extract_or_create_filename(new_filename, current_filename):
    new_filename_basename = os.path.basename(new_filename)
    if not new_filename_basename:
        new_filename_basename = os.path.basename(current_filename).split(".")[0]
    return os.path.join(os.path.dirname(new_filename), new_filename_basename)
