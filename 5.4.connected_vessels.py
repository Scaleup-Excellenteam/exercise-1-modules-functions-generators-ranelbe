"""
Writer: Ranel Ben Simman Tov, 315967703
"""
from itertools import zip_longest


def interleave(*iterables):
    """
    Interleave the given iterables - regular implementation
    :param iterables: the iterables to interleave
    :return: an interleaved list of all the elements in the given iterables
    """
    zips = list(zip_longest(*iterables))  # zip the iterables
    return [item for tup in zips
            for item in tup if item is not None]


def interleave_generator(*iterables):
    """
    Interleave the given iterables - generator implementation
    :param iterables: the iterables to interleave
    :yield: an item of the interleaved list
    """
    for tup in zip_longest(*iterables):
        for item in tup:
            if item is not None:
                yield item


def main():
    # regular version
    print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
    # generator version
    print(list(interleave_generator('abc', [1, 2, 3], ('!', '@', '#'))))


if __name__ == '__main__':
    main()
