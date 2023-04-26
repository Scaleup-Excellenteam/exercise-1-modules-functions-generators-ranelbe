"""
Writer: Ranel Ben Simman Tov, 315967703
"""


def join(*list_of_lists, sep='-'):
    """
    Join all the lists in list_of_lists with the given separator
    :param list_of_lists: the lists to join
    :param sep: the separator to join the lists with
    :return: a list of all the elements in the lists in list_of_lists joined with the given separator
    """
    if not list_of_lists:  # if list_of_lists is empty
        return None
    new_list = []
    for lst in list_of_lists:
        new_list.extend(lst+[sep])
    return new_list[:-1]  # remove the last separator


# add some tests
def main():
    test1 = join([1, 2], [8], [9, 5, 6], sep='@')
    print(test1) # [1, 2, '@', 8, '@', 9, 5, 6]
    test2 = join([1, 2], [8], [9, 5, 6])
    print(test2) # [1, 2, '-', 8, '-', 9, 5, 6]
    test3 = join([1])
    print(test3) # [1]
    test4 = join()
    print(test4) # None


if __name__ == '__main__':
    main()