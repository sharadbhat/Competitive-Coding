# Leetcode
# https://leetcode.com/problems/minimum-distance-to-the-target-element/


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        if nums[start] == target:
            return 0

        left = start - 1
        right = start + 1

        while True:
            if left >= 0 and nums[left] == target:
                return start - left
            if right < len(nums) and nums[right] == target:
                return right - start

            left -= 1
            right += 1
