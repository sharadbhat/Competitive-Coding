# Leetcode
# https://leetcode.com/problems/reorganize-string/

from heapq import heapify, heappush, heappop


class Solution:
    def reorganizeString(self, S: str) -> str:
        heap = [(-v, k) for k, v in Counter(S).items()]
        heapify(heap)
        prev_val, prev_letter = 0, ''
        out = ''
        while heap:
            val, letter = heappop(heap)
            out += letter
            if prev_val < 0:
                heappush(heap, (prev_val, prev_letter))
            prev_val, prev_letter = val + 1, letter

        if len(S) != len(out):
            return ''
        return out
