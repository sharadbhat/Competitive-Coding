# HACKERRANK
# https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem

'''
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
    curr = root
    v1, v2 = min(v1, v2), max(v1, v2)
    while True:
        if curr.info >= v1 and curr.info <= v2:
            return curr
        elif curr.info > v1 and curr.info > v2:
            curr = curr.left
        elif curr.info < v1 and curr.info < v2:
            curr = curr.right
