# Leetcode
# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        out = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]
                if total_sum == 0:
                    out.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < len(nums) and nums[left] == nums[left - 1]:
                        left += 1
                    while right > i and nums[right] == nums[right + 1]:
                        right -= 1

                elif total_sum > 0:
                    right -= 1
                else:
                    left += 1
        return out