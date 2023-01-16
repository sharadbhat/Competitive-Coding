# Leetcode
# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        largest = 0
        og = set(nums)
        visited = set()
        for num in og:
            if num in visited:
                continue
            count = 0
            while True:
                if num in og:
                    count += 1
                    visited.add(num)
                    num += 1
                else:
                    break
            largest = max(largest, count)
        return largest