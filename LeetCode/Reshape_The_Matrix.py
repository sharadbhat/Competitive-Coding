# Leetcode
# https://leetcode.com/problems/reshape-the-matrix


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums) * len(nums[0]) != r * c:
            return nums

        reshaped = []
        row = []
        for i in nums:
            for j in i:
                if len(row) < c:
                    row.append(j)
                    if len(row) == c:
                        reshaped.append(row)
                        row = []
        return reshaped
