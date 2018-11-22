# LeetCode
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val1 = ""
        val2 = ""
        while l1 != None:
            val1 = str(l1.val) + val1
            l1 = l1.next
        while l2 != None:
            val2 = str(l2.val) + val2
            l2 = l2.next
        val = str(int(val1) + int(val2))[::-1]
        output = ListNode(val[0])
        curr = output
        for i in val[1:]:
            new_node = ListNode(i)
            curr.next = new_node
            curr = new_node
        return output
