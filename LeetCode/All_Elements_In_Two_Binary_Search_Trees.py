# Leetcode
# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        arr1 = self.getElements(root1, [])
        arr2 = self.getElements(root2, [])
        return sorted(arr1 + arr2)

    def getElements(self, root: TreeNode, arr: List[int]) -> List[int]:
        if not root:
            return []
        if root.left:
            self.getElements(root.left, arr)
        arr.append(root.val)
        if root.right:
            self.getElements(root.right, arr)

        return arr
