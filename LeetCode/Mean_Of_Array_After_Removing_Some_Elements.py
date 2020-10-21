# Leetcode
# https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        remove_length = len(arr) // 20 # 5%
        arr = arr[remove_length: -remove_length]
        return sum(arr) / len(arr)