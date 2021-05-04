# Leetcode
# https://leetcode.com/problems/set-mismatch/


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        vals = set()
        out = []
        for i in nums:
            if i in vals:
                out.append(i)
            vals.add(i)

        return out + [i for i in range(1, len(nums) + 1) if i not in vals]
