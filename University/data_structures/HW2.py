import time
import pandas as pd
import numpy as np


# Part A

class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to pop an empty stack")

        topIdx = len(self.items) - 1
        item = self.items[topIdx]
        del self.items[topIdx]
        return item

    def push(self, item):
        self.items.append(item)

    def top(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to get top of empty stack")

        topIdx = len(self.items) - 1
        return self.items[topIdx]

    def isEmpty(self):
        return len(self.items) == 0


class Queue:
    def __init__(self):
        self.items = []
        self.frontIdx = 0

    def __compress(self):
        newlst = [self.items[i] for i in range(self.frontIdx, len(self.items))]
        self.items = newlst
        self.frontIdx = 0

    def dequeue(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to dequeue an empty queue")

        if self.frontIdx * 2 > len(self.items):
            self.__compress()

        item = self.items[self.frontIdx]
        self.frontIdx += 1
        return item

    def enqueue(self, item):
        self.items.append(item)

    def front(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to access front of empty queue")
        return self.items[self.frontIdx]

    def isEmpty(self):
        return self.frontIdx == len(self.items)


class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


def transpose_stack(inp_mat):
    """
    Create a function for calculation of a transpose of any variable sized matrix
    (MxN where M and N are variables) by using stack structure.
    :param inp_mat: MxN matrix need to transpose
    :return: transposed NxM matrix
    """
    row = len(inp_mat)
    column = len(inp_mat[0])
    temp_stack = Stack()
    res_matrix = [[] for x in range(column)]
    for i in range(column - 1, -1, -1):
        for j in range(row - 1, -1, -1):
            temp_stack.push(inp_mat[j][i])

    count = len(temp_stack.items) - 1
    for i in range(column):
        for _ in range(row):
            res_matrix[i].append(temp_stack.items[count])
            count -= 1
    return res_matrix


print("Stack Test Case 1", transpose_stack([[0, 1, 2], [3, 4, 5]]))
print("Stack Test Case 2", transpose_stack([[5, 9, 7, 5], [5, 5, 7, 14], [9, 1, 5, 6]]))
print()


def transpose_queue(inp_mat):
    """
    Create a function for calculation of at transpose of any variable sized matrix
    (MxN where M and N are variables) by using queue structure.
    :param inp_mat: MxN matrix need to transpose
    :return: transposed NxM matrix
    """
    row = len(inp_mat)
    column = len(inp_mat[0])
    temp_queue = Queue()
    res_matrix = [[] for x in range(column)]
    for i in range(column):
        for j in range(row):
            temp_queue.enqueue(inp_mat[j][i])

    count = 0
    for i in range(column):
        for _ in range(row):
            res_matrix[i].append(temp_queue.items[count])
            count += 1

    return res_matrix


print("Queue Test Case 1", transpose_queue([[0, 1, 2], [3, 4, 5]]))
print("Queue Test Case 2", transpose_queue([[5, 9, 7, 5], [5, 5, 7, 14], [9, 1, 5, 6]]))
print()


def transpose_deque(inp_mat):
    """
    Create a function for calculation of at transpose of any variable sized matrix
    (MxN where M and N are variables) by using deck structure.
    :param inp_mat: MxN matrix need to transpose
    :return: transposed NxM matrix
    """
    row = len(inp_mat)
    column = len(inp_mat[0])
    temp_deque = Deque()
    res_matrix = [[] for x in range(column)]
    for i in range(column):
        for j in range(row):
            temp_deque.add_front(inp_mat[j][i])

    count = 0
    for i in range(column):
        for _ in range(row):
            res_matrix[i].append(temp_deque.items[count])
            count += 1

    return res_matrix


print("Deque Test Case 1", transpose_deque([[0, 1, 2], [3, 4, 5]]))
print("Deque Test Case 2", transpose_deque([[5, 9, 7, 5], [5, 5, 7, 14], [9, 1, 5, 6]]))
print()

# Part B

test_case_dictionary = {}

start1 = time.time()
transpose_stack([[0, 1, 2], [3, 4, 5]])
stop1 = time.time()
total1 = stop1 - start1
test_case_dictionary["Stack Time"] = total1

start2 = time.time()
transpose_queue([[0, 1, 2], [3, 4, 5]])
stop2 = time.time()
total2 = stop2 - start2
test_case_dictionary["Queue Time"] = total2

start3 = time.time()
transpose_deque([[0, 1, 2], [3, 4, 5]])
stop3 = time.time()
total3 = stop3 - start3
test_case_dictionary["Deque Time"] = total3

print(test_case_dictionary)
