# Leetcode
# https://leetcode.com/problems/deepest-leaves-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        curr_sum = 0
        queue = [root]
        while queue:
            curr_sum = 0
            for i in range(len(queue)):
                curr = queue.pop(0)
                curr_sum += curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return curr_sum
