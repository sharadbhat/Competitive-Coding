# LeetCode
# https://leetcode.com/problems/linked-list-cycle/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        try:
            while True:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return True
        except:
            return False
