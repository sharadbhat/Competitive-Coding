# Leetcode
# https://leetcode.com/problems/divide-array-into-equal-pairs/

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2 != 0:
            return False
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num in count:
            if count[num] % 2 != 0:
                return False
        return True