import os


def ensure_directory(file_path):
    directory = os.path.dirname("./" + file_path)
    if not os.path.exists(directory):
        print('creating directory')
        os.mkdir(directory)
