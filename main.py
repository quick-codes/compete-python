import heapq
import string
from bisect import bisect, bisect_left
from collections import Counter, deque, defaultdict
import re
from copy import copy
from math import inf
from queue import Queue
from typing import List

from tree_node import TreeNode, list_to_binary_tree


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked_list(items):
    head = None
    for item in reversed(items):
        head = ListNode(item, head)
    return head


def linked_list_to_string(head):
    items = []
    while head:
        items.append(head.val)
        head = head.next
    return list_to_string(items)


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def list_to_random_linked_list(items):
    cache = {}
    head = Node(0)
    current = head
    for i, (v, _) in enumerate(items):
        current.next = Node(v)
        cache[i] = current.next
        current = current.next

    current = head.next
    for _, i in items:
        if i > -1:
            current.random = cache[i]
        current = current.next

    return head.next


def random_linked_list_to_string(head):
    cache = {}
    current = head
    i = 0
    while current:
        cache[current] = i
        current = current.next
        i += 1

    nodes = []
    current = head
    while current:
        nodes.append('[' + str(current.val) + ', ' + str(cache[current.random] if current.random else -1) + ']')
        current = current.next
    return '[' + ', '.join(nodes) + ']'


def list_to_string(items):
    items = [str(entry) for entry in items]
    return '[' + ', '.join(items) + ']'


if __name__ == '__main__':
    inputs = [
        [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8],
        [6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5],
    ]
    for _input in inputs:
        _root = list_to_binary_tree(_input)
        print('root =', _input)
