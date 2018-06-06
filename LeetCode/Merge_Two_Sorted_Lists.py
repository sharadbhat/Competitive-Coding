# LeetCode
# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 != None and l2 != None:
            if l1.val < l2.val:
                merged = ListNode(l1.val)
                l1 = l1.next
            else:
                merged = ListNode(l2.val)
                l2 = l2.next

            current = merged

            while l1 != None and l2 != None:
                if l1.val < l2.val:
                    a = ListNode(l1.val)
                    l1 = l1.next
                    current.next = a
                    current = current.next
                else:
                    a = ListNode(l2.val)
                    l2 = l2.next
                    current.next = a
                    current = current.next

            while l1 != None:
                a = ListNode(l1.val)
                l1 = l1.next
                current.next = a
                current = current.next

            while l2 != None:
                a = ListNode(l2.val)
                l2 = l2.next
                current.next = a
                current = current.next

            return merged
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
