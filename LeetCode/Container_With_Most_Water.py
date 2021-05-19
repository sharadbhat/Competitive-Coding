# Leetcode
# https://leetcode.com/problems/container-with-most-water/


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start, end, max_area = 0, len(height) - 1, 0

        while start < end:
            if height[start] <= height[end]:
                max_area = max(max_area, height[start] * (end - start))
                start += 1
            else:
                max_area = max(max_area, height[end] * (end - start))
                end -= 1

        return max_area
