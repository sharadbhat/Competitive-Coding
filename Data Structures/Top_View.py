# HACKERRANK
# https://www.hackerrank.com/challenges/tree-top-view/problem

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def left_part(node):
    if node == None:
        return
    left_part(node.left)
    print node.data,

def right_part(node):
    if node == None:
        return
    print node.data,
    right_part(node.right)

def topView(root):
    left_part(root.left)
    print root.data,
    right_part(root.right)
