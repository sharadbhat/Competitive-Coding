# Leetcode
# https://leetcode.com/problems/next-greater-node-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next

        out = []
        stack = []
        for val in vals[::-1]:
            if stack and stack[-1] <= val:
                while stack and stack[-1] <= val:
                    stack.pop()

            if not stack:
                out.append(0)
            else:
                out.append(stack[-1])
            stack.append(val)

        return out[::-1]
