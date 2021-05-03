# Leetcode
# https://leetcode.com/problems/binary-search-tree-iterator/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.inorder = []
        self.traverse(root)

    def traverse(self, root: TreeNode):
        if not root:
            return

        self.traverse(root.left)
        self.inorder.append(root.val)
        self.traverse(root.right)

    def next(self) -> int:
        return self.inorder.pop(0)

    def hasNext(self) -> bool:
        return len(self.inorder) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
