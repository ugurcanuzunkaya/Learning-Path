import random
import time
import pandas as pd

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "->".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


# Part A1

def MinList(inp_list):
    minval = float("inf")
    for i in inp_list:
        if minval > i:
            minval = i

    return minval


def MaxList(inp_list):
    maxval = float("-inf")
    for i in inp_list:
        if maxval < i:
            maxval = i

    return maxval


def Normalize(inp_list):
    normal_list = []
    min_val = MinList(inp_list)
    max_val = MaxList(inp_list)
    for i in inp_list:
        a = (i - min_val) / (max_val - min_val)
        normal_list.append(round(a, 5))

    return normal_list


print(MaxList([5, 9, -5, 6, 1, 54, -1]))
print(MinList([5, 9, -5, 6, 1, 54, -1]))
print(Normalize([5, 9, -5, 6, 1, 54, -1]))


# Part A2

def MinList_ll(inp_linkedlist):
    minval = float("inf")
    for i in inp_linkedlist:
        if minval > float(i.data):
            minval = float(i.data)

    return minval


def MaxList_ll(inp_linkedlist):
    maxval = float("-inf")
    for i in inp_linkedlist:
        if maxval < float(i.data):
            maxval = float(i.data)

    return maxval


def Normalize_ll(inp_linkedlist):
    normal_list = []
    min_val_ll = MinList_ll(inp_linkedlist)
    max_val_ll = MaxList_ll(inp_linkedlist)
    for i in inp_linkedlist:
        a = (float(i.data) - min_val_ll) / (max_val_ll - min_val_ll)
        normal_list.append(round(a, 5))

    return normal_list


inp_list = [5, 9, -5, 6, 1, 54, -1]
llist = LinkedList()
first_node = Node(str(inp_list[0]))
llist.head = first_node
for x in range(1, len(inp_list)):
    node = Node(str(inp_list[x]))
    first_node.next = node
    first_node = node

print(MinList_ll(llist))
print(MaxList_ll(llist))
print(Normalize_ll(llist))

# Part B

test_case_dict = {}
partA1 = []
partA2 = []
for j in range(10, 1010):
    inputlist = []
    for k in range(j):
        rn = random.randint(-10000, 10000)
        inputlist.append(rn)

    start = time.time()
    samples = Normalize(inputlist)
    stop = time.time()
    stop = stop - start
    partA1.append(round(stop, 10))

    input_llist = LinkedList()
    first_node = Node(str(inputlist[0]))
    input_llist.head = first_node
    for x in range(1, len(inputlist)):
        node = Node(str(inputlist[x]))
        first_node.next = node
        first_node = node

    start = time.time()
    samples = Normalize_ll(input_llist)
    stop = time.time()
    stop = stop - start
    partA2.append(round(stop, 10))

test_case_dict["Part A1 Tests"] = partA1
test_case_dict["Part A2 Tests"] = partA2

test_case_df = pd.DataFrame(test_case_dict)
print(test_case_df.describe())

