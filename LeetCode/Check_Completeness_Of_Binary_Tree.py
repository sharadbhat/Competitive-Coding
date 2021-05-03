# Leetcode
# https://leetcode.com/problems/check-completeness-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue = [root]
        empty_spot = False
        while len(queue):
            for i in range(len(queue)):
                curr = queue.pop(0)
                if curr:
                    if empty_spot:
                        return False
                    queue.append(curr.left)
                    queue.append(curr.right)
                else:
                    empty_spot = True
        return True
