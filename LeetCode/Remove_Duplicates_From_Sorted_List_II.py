# Leetcode
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        sentinel = ListNode(0, head)
        prev = sentinel
        curr = head

        while curr:
            isDup = False
            while curr.next and curr.next.val == curr.val:
                isDup = True
                curr = curr.next
            if isDup:
                prev.next = curr.next
            else:
                prev.next = curr
                prev = curr
            curr = curr.next
        return sentinel.next
