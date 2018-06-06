# LeetCode
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = 0
        a = None
        if head != None:
            a = ListNode(head.val)
            prev = head.val
            head = head.next
        else:
            return None

        current = a

        if head != None:
            while head.next != None:
                if head.val != prev:
                    new_node = ListNode(head.val)
                    prev = head.val
                    current.next = new_node
                    current = current.next

                head = head.next

        if head != None and head.val != prev:
            new_node = ListNode(head.val)
            current.next = new_node

        return a
