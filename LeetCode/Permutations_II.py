# Leetcode
# https://leetcode.com/problems/permutations-ii/


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        unique = set()
        out = []
        self.getPermutations(unique, out, [], nums)
        return list(out)

    def getPermutations(self, unique: Set[str], out: List[List[int]], prefix: List[int], nums: List[int]) -> None:
        if len(nums) == 1:
            if str(prefix + nums) not in unique:
                unique.add(str(prefix + nums))
                out.append(prefix + nums)
            return

        for i in range(len(nums)):
            self.getPermutations(unique, out, prefix +
                                 [nums[i]], nums[:i] + nums[i+1:])
