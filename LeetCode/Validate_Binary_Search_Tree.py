# Leetcode
# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        traversed = self.traverse(root)
        for i in range(len(traversed) - 1):
            if traversed[i] >= traversed[i + 1]:
                return False
        return True

    def traverse(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.traverse(root.left) + [root.val] + self.traverse(root.right)
