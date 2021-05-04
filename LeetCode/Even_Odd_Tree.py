# Leetcode
# https://leetcode.com/problems/even-odd-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        is_even = False
        queue = [root]
        while len(queue):
            curr = None
            prev = None
            for i in range(len(queue)):
                prev = curr
                curr = queue.pop(0)
                if curr.val % 2 == is_even:
                    return False
                if prev:
                    if is_even and prev.val <= curr.val:
                        return False
                    if not is_even and prev.val >= curr.val:
                        return False
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            is_even = not is_even

        return True
