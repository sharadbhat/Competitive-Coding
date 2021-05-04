# Leetcode
# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class FindElements:

    def __init__(self, root: TreeNode):
        self.val_set = set()
        self.recoverTree(root, 0)

    def recoverTree(self, root: TreeNode, val: int) -> TreeNode:
        self.val_set.add(val)
        if root.left:
            root.left = self.recoverTree(root.left, val * 2 + 1)

        if root.right:
            root.right = self.recoverTree(root.right, val * 2 + 2)

    def find(self, target: int) -> bool:
        return target in self.val_set


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
