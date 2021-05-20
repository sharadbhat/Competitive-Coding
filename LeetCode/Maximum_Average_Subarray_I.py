# Leetcode
# https://leetcode.com/problems/maximum-average-subarray-i/


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        arr = deque(nums[:k])
        total = sum(arr)
        max_avg = total / k

        for i in range(k, len(nums)):
            total -= arr.popleft()
            total += nums[i]
            arr.append(nums[i])

            max_avg = max(max_avg, total / k)

        return max_avg
