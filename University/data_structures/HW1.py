import random
import time
import pandas as pd


# Part A

def group_odd_even(integerlist):
    """
    Create a function which returns a list which consists of the odd elements of the integerlist at the begining
    and even values of the integerlist at the end.
    :param integerlist: List of random even and odd values
    :return: sorted list of first odd values then even values
    """
    return [j for j in integerlist if j % 2 == 1] + [i for i in integerlist if i % 2 == 0]


print("---Part A---")
print("Test Cases for Group Odd Even Function")
print("Test Case 1:", group_odd_even([3, 8, 7, 2, 5, 1, 6]))
print("Test Case 2:", group_odd_even([57, 42, 89, 24, 6, 3, 8, 1, 8, 34, 633]))
print("")


def longest_mon_inc_seq(inplist):
    """
    Create a function which gives the position of longest monotonic increasing sublist in the inputlist.
    If there is no monotonic increasing sublist in the list, function should return -1.
    :param inplist: Sequence list both contains all integer number's types.
    :return: Starting position of largest monotonic increasing sublist.
    """
    first = inplist[0]
    count = 0
    res = 0
    for i in range(1, len(inplist)):
        if first < inplist[i]:
            count += 1
        elif res < count:
            res = count
            count = 0
        first = inplist[i]

    if res == 0:
        res = -1
    return res


print("Test Cases for Longest Monotonic Increasing Sequence Function")
print("Test Case 1:", longest_mon_inc_seq([1, 0, 2, -1, 3, 4, 7, 2, 3, 5]))
print("Test Case 2:", longest_mon_inc_seq([7, 5, 4, 4, 3, 2, 2, 1, -1, -5, -9]))

# Part B
print("----Part B---")
test_case_dictionary = {}
test_case_counter = 1
partA1 = []
for i in range(10, 1000):
    inputlist2 = []
    for j in range(i):
        rn = random.randint(0, 100000)
        inputlist2.append(rn)

    start1 = time.time()
    samples = group_odd_even(inputlist2)
    stop1 = time.time()
    stop1 = stop1 - start1
    partA1.append(round(stop1, 1))
    test_case_counter += 1

test_case_dictionary["Part A1 Tests"] = partA1

test_case_counter2 = 1
partA2 = []
for j in range(10, 1000):
    inputlist3 = []
    for k in range(j):
        rn = random.randint(-10000, 10000)
        inputlist3.append(rn)

    start2 = time.time()
    samples2 = longest_mon_inc_seq(inputlist3)
    stop2 = time.time()
    stop2 = stop2 - start2
    partA2.append(round(stop2, 10))
    test_case_counter2 += 1

test_case_dictionary["Part A2 Tests"] = partA2

test_cases_df = pd.DataFrame(test_case_dictionary)
print(test_cases_df.describe())
