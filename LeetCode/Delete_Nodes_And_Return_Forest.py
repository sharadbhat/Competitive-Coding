# Leetcode
# https://leetcode.com/problems/delete-nodes-and-return-forest/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root or not to_delete:
            return [root]

        to_delete = set(to_delete)
        out = []

        def removeNodes(curr: TreeNode, parent: TreeNode):
            if not curr:
                return None

            curr_out = curr
            if curr.val in to_delete:
                curr_out = None
                if parent:
                    if parent.left == curr:
                        parent.left = None
                    else:
                        parent.right = None
            else:
                if not parent:
                    out.append(curr)

            curr.left = removeNodes(curr.left, curr_out)
            curr.right = removeNodes(curr.right, curr_out)

            return curr_out

        removeNodes(root, None)

        return out
