"""
Writer: Ranel Ben Simman Tov, 315967703
"""

import os


def find_files_with_prefix(path, prefix='deep'):
    """
    Find all files in the given path that start with the given prefix
    default prefix is 'deep' but can be changed
    :param path: the path to search in
    :param prefix: the prefix to search for, default is 'deep'
    :return: a list of all the matching files
    """
    matching_files = []
    for file_name in os.listdir(path):
        # check if the file name starts with the given prefix and is not a directory
        if file_name.startswith(prefix) and not os.path.isdir(os.path.join(path, file_name)):
            matching_files.append(file_name)
    return matching_files
