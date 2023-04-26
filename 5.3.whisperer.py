"""
Writer: Ranel Ben Simman Tov, 315967703
"""
import re

MESSAGE_LENGTH = 5  # minimum length of a secret message
CHUNK_SIZE = 1024  # size of each chunk to read from the file
MESSAGE_REGEX = rb'[a-z]{5,}!'  # regular expression to match secret messages


def find_secret_messages(filename, chunk_size=CHUNK_SIZE):
    """
    Find all secret messages in the given file
    :param filename: the file to search in
    :param chunk_size: the size of each chunk to read from the file
    :yield: the secret messages found in the file
    """
    with open(filename, 'rb') as file:
        while chunk := file.read(chunk_size):
            for message in re.findall(MESSAGE_REGEX, chunk):
                yield message.decode()


def main():
    print(*list(find_secret_messages('logo.jpg')), sep='\n')


if __name__ == '__main__':
    main()
