# Leetcode
# https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        longest_zeros = 0
        longest_ones = 0

        prev = None
        curr_len = 0
        for i in s:
            if i == prev:
                curr_len += 1
            else:
                curr_len = 1
                prev = i

            if i == '0':
                longest_zeros = max(longest_zeros, curr_len)
            else:
                longest_ones = max(longest_ones, curr_len)

        return longest_ones > longest_zeros
