# LeetCode
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        l = {}
        while headA != None:
            l[headA] = 1
            headA = headA.next

        while headB != None:
            if headB in l:
                return headB
            headB = headB.next

        return None
