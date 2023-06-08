# Leetcode
# https://leetcode.com/problems/path-sum-ii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        if not root.left and not root.right:
            if root.val == targetSum:
                return [[root.val]]

        left, right = [], []
        if root.left:
            left = self.pathSum(root.left, targetSum - root.val)
        
        if root.right:
            right = self.pathSum(root.right, targetSum - root.val)

        out = []
        for i in left + right:
            if sum(i) + root.val == targetSum:
                out.append([root.val] + i)
        
        return out