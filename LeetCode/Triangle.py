# Leetcode
# https://leetcode.com/problems/triangle

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev_level = [triangle[0][0]]

        for level in range(1, len(triangle)):
            new_level = []
            for i in range(len(triangle[level])):
                cost = triangle[level][i] + prev_level[i - 1]
                if i == 0:
                    cost = triangle[level][i] + prev_level[i]
                if len(prev_level) > i:
                    cost = min(cost, triangle[level][i] + prev_level[i])

                new_level.append(cost)
            prev_level = new_level

        return min(prev_level)