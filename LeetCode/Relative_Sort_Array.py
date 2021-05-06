# Leetcode
# https://leetcode.com/problems/relative-sort-array/


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        out = []
        d = Counter(arr1)

        for i in arr2:
            out += [i] * d.get(i, 0)
            d.pop(i)

        extra = []
        for i in d:
            extra += [i] * d[i]

        return out + sorted(extra)
