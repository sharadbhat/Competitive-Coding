# HACKERANK
# https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    pos = []
    while True:
        pos.append(head)
        if head.next != None:
            head = head.next
            if head in pos:
                return 1
        else:
            return 0
