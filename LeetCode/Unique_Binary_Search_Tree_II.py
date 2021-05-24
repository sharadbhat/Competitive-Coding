# Leetcode
# https://leetcode.com/problems/unique-binary-search-trees-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        inorder = [i for i in range(1, n + 1)]

        def helper(arr):
            if len(arr) == 0:
                return []
            if len(arr) == 1:
                return [TreeNode(arr[0])]

            out = []
            for pos, i in enumerate(arr):
                left_trees = helper(arr[:pos]) or [None]
                right_trees = helper(arr[pos+1:]) or [None]

                for left_tree in left_trees:
                    for right_tree in right_trees:
                        curr = TreeNode(i, left_tree, right_tree)
                        out.append(curr)

            return out

        return helper(inorder)
