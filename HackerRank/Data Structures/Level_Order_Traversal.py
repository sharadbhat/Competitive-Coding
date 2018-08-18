# HACKERRANK
# https://www.hackerrank.com/challenges/tree-level-order-traversal/problem

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def levelOrder(root):
    queue = [root]
    while len(queue) != 0:
        curr = queue[0]
        print(curr.info, end=' ')
        if curr.left != None:
            queue.append(curr.left)
        if curr.right != None:
            queue.append(curr.right)
        queue = queue[1:]
