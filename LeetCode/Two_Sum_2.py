# LeetCode
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        min_pos = 0
        max_pos = len(numbers) - 1
        while min_pos < max_pos:
            summation = numbers[min_pos] + numbers[max_pos]
            if summation == target:
                return [min_pos + 1, max_pos + 1]
            elif summation < target:
                min_pos += 1
            else:
                max_pos -= 1
