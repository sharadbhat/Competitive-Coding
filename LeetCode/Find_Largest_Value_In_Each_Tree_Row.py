# Leetcode
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        out = []
        queue = [[root, 1]]
        while len(queue):
            curr, depth = queue.pop(0)
            if len(out) < depth:
                out.append(curr.val)
            elif out[depth - 1] < curr.val:
                out[depth - 1] = curr.val

            if curr.left:
                queue.append([curr.left, depth + 1])
            if curr.right:
                queue.append([curr.right, depth + 1])
        return out
