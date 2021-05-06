# Leetcode
# https://leetcode.com/problems/subarray-sum-equals-k/


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        out = 0
        seen_count = {0: 1}
        curr_sum = 0

        for i in nums:
            curr_sum += i
            out += seen_count.get(curr_sum - k, 0)
            seen_count[curr_sum] = seen_count.get(curr_sum, 0) + 1

        return out
