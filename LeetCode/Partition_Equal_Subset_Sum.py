# Leetcode
# https://leetcode.com/problems/partition-equal-subset-sum

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2
        possible_sums = set([0])

        for i in nums[::-1]:
            if i == target:
                return True
            for j in list(possible_sums):
                if j == target or j + i == target:
                    return True
                possible_sums.add(j + i)
            possible_sums.add(i)
        
        return False