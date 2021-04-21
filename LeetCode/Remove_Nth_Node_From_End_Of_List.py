# Leetcode
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr = head
        count = 1
        while curr.next != None:
            count += 1
            curr = curr.next
        n = count - n
        if n == 0:
            head = head.next
        else:
            curr = head
            i = 0
            while i < n - 1:
                i += 1
                curr = curr.next
            curr.next = curr.next.next
        return head
