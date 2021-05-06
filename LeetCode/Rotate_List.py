# Leetcode
# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        length = 0
        temp = head
        while temp:
            temp = temp.next
            length += 1

        k = k % length

        slow = head
        fast = head

        while k > 0:
            if fast.next:
                fast = fast.next
            k -= 1

        while fast.next:
            slow = slow.next
            fast = fast.next

        fast.next = head
        head = slow.next
        slow.next = None

        return head
