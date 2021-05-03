# Leetcode
# https://leetcode.com/problems/find-the-highest-altitude/


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maximum = curr = 0
        for i in gain:
            curr += i
            maximum = max(curr, maximum)
        return maximum
