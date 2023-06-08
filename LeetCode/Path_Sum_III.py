# Leetcode
# https://leetcode.com/problems/path-sum-iii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def recurse(root, init_target, targetSums):
            if not root:
                return 0

            out = 0
            new_d = {init_target: 1}

            for target in targetSums:
                new_d[target - root.val] = new_d.get(target - root.val, 0) + targetSums[target]
                if target == root.val:
                    out += targetSums[target]
            
            out += recurse(root.left, init_target, new_d)
            out += recurse(root.right, init_target, new_d)

            return out
        
        return recurse(root, targetSum, {targetSum: 1})