# Leetcode
# https://leetcode.com/problems/binary-subarrays-with-sum/


class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        curr_sum = 0
        d = {0: 1}
        count = 0

        for i in A:
            curr_sum += i
            if curr_sum - S in d:
                count += d[curr_sum - S]
            d[curr_sum] = d.get(curr_sum, 0) + 1

        return count
