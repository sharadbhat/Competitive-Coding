# Leetcode
# https://leetcode.com/problems/permutations/


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        self.getPermutations(out, [], nums)
        return out

    def getPermutations(self, out: List[List[int]], prefix: List[int], nums: List[int]) -> None:
        if len(nums) == 1:
            out.append(prefix + nums)
            return

        for i in range(len(nums)):
            self.getPermutations(
                out, prefix + [nums[i]], nums[:i] + nums[i+1:])
