import random
import time


# Part A

def seq_search(inplist1, searched_list):
    """
    Assume that you have an unordered list and you want to search an unordered sublist in that list.
    Design a sequential iterative search function, which returns the start index of searched sublist,
    if it is found in the larger list. Otherwise, your search function returns None value.
    :param inplist1: Unordered list that we search for sublist.
    :param searched_list: Unordered sublist that we search for.
    :return: Position of searched sublist in the larger list.
    """

    for i in range(len(inplist1)):
        if inplist1[i:i + len(searched_list)] == searched_list:
            return i
    return None


searched_index = seq_search([5, 3, 8, 10, 1, 6], [8, 10])
print("Position of searched sublist:", searched_index)


def recur_seq_ordered_search(inplist1, searched_list):
    """
    Design a recursive sequential search function by the assumption of your larger list and
    searched list are ordered lists in ascending order.
    :param inplist1: Large list that assuming ordered in ascending order.
    :param searched_list: Sublist that assuming ordered in ascending order.
    :return: Position of searched sublist in the larger list.
    """

    if len(searched_list) == 0 or len(inplist1) == 0:
        return 0
    if inplist1[0] == searched_list[0]:
        return recur_seq_ordered_search(inplist1[1:], searched_list[1:])
    else:
        return 1 + recur_seq_ordered_search(inplist1[1:], searched_list)


searched_index = recur_seq_ordered_search([1, 3, 5, 6, 8, 10], [8, 10])
print("Position of searched sublist:", searched_index)


def iter_bin_search(inplist1, searched_list):
    """
    Design an iterative binary search function by the assumption of your larger list and
    searched list are ordered lists in ascending order.
    :param inplist1: Large list that assuming ordered in ascending order.
    :param searched_list: Sublist that assuming ordered in ascending order.
    :return: Position of searched sublist in the larger list.
    """

    low = 0
    high = len(inplist1) - 1
    while low <= high:
        mid = (low + high) // 2
        if inplist1[mid] == searched_list[0]:
            if inplist1[mid:mid + len(searched_list)] == searched_list:
                return mid
            else:
                low = mid + 1
        else:
            high = mid - 1
    return None


searched_index = iter_bin_search([1, 3, 5, 6, 8, 10], [8, 10])
print("Position of searched sublist:", searched_index)


def recur_bin_search(inplist1, searched_list):
    """
    Design a recursive binary search function by the assumption of your larger list and
    searched list are ordered lists in ascending order.
    :param inplist1: Large list that assuming ordered in ascending order.
    :param searched_list: Sublist that assuming ordered in ascending order.
    :return: Position of searched sublist in the larger list.
    """

    if len(searched_list) == 0 or len(inplist1) == 1:
        return 0
    mid = len(inplist1) // 2
    if inplist1[mid] != searched_list[0]:
        return mid + recur_bin_search(inplist1[mid:], searched_list)
    if inplist1[mid:mid + len(searched_list)] == searched_list:
        return mid
    else:
        return recur_bin_search(inplist1[:mid], searched_list)


searched_index = recur_bin_search([1, 3, 5, 6, 8, 10], [8, 10])
print("Position of searched sublist:", searched_index)

exec_time_seq_search = []

exec_time_recur_seq_search = []

exec_time_iter_bin_search = []

exec_time_recur_bin_search = []

for n in range(5, 50, 5):
    inplist = random.sample(range(0, 10 * n), n)

    ordered_inplist = sorted(inplist)

    seq_row = []

    recur_sec_row = []

    iter_bin_row = []

    recur_bin_row = []

    for m in range(1, n // 2):
        searchedlist = random.sample(range(0, 10 * m), m)

        ordered_searchedlist = sorted(searchedlist)

        t1 = time.time()

        seq_search(inplist, searchedlist)

        t2 = time.time()

        seq_row.append(round((t2 - t1) * 1000, 2))  # Execution time in ms

        t1 = time.time()

        recur_seq_ordered_search(ordered_inplist, ordered_searchedlist)

        t2 = time.time()

        recur_sec_row.append(round((t2 - t1) * 1000, 2))

        t1 = time.time()

        iter_bin_search(ordered_inplist, ordered_searchedlist)

        t2 = time.time()

        iter_bin_row.append(round((t2 - t1) * 1000, 2))

        t1 = time.time()

        recur_bin_search(ordered_inplist, ordered_searchedlist)

        t2 = time.time()

        recur_bin_row.append(round((t2 - t1) * 1000, 2))

    exec_time_seq_search.append(seq_row)

    exec_time_recur_seq_search.append(recur_sec_row)

    exec_time_iter_bin_search.append(iter_bin_row)

    exec_time_recur_bin_search.append(recur_bin_row)


def print2d(list2d):
    for i in range(len(list2d)):

        print('[', end=' ')

        for j in range(len(list2d[i])):
            print(list2d[i][j], end=' ')

        print(']')


print("Execution time for iterative sequential search:")

print2d(exec_time_seq_search)

print("Execution time for recursive sequential search:")

print2d(exec_time_recur_seq_search)

print("Execution time for iterative binary search:")

print2d(exec_time_recur_seq_search)

print("Execution time for recursive binary search:")

print2d(exec_time_recur_bin_search)
