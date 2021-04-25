# Leetcode
# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        last = head
        total = 1
        while last.next:
            total += 1
            last = last.next

        curr = head
        nextCount = 2

        while nextCount <= total:
            last.next = curr.next
            curr.next = curr.next.next
            curr = curr.next

            last = last.next
            last.next = None
            nextCount += 2

        return head
