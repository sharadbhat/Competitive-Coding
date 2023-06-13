# Leetcode
# https://leetcode.com/problems/largest-number

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(i) for i in nums]

        def compare(i, j):
            if i + j > j + i:
                return -1
            return 1

        nums = sorted(nums, key=cmp_to_key(compare))

        return str(int(''.join(nums)))