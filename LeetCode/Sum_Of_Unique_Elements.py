# Leetcode
# https://leetcode.com/problems/sum-of-unique-elements/


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = {}
        out = 0
        for i in nums:
            d[i] = d.get(i, 0) + 1
            if d[i] == 1:
                out += i
            elif d[i] == 2:
                out -= i
        return out
