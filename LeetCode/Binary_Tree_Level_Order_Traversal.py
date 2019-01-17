# LeetCode
# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        l = []
        q = [[root]]
        while len(q) > 0:
            temp = []
            tempq = []
            for i in q[0]:
                temp.append(i.val)
                if i.left:
                    tempq.append(i.left)
                if i.right:
                    tempq.append(i.right)
            if len(tempq) > 0:
                q.append(tempq)
            del q[0]
            l.append(temp)
        return l
