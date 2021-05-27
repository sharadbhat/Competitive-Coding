# Leetcode
# https://leetcode.com/problems/find-lucky-integer-in-an-array/


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky = -1
        d = Counter(arr)
        for i in d:
            if d[i] == i and i > lucky:
                lucky = i
        return lucky
