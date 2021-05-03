# Leetcode
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        prev, slow, fast = head, head, head
        while fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next

        root = TreeNode(slow.val)
        prev.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root
