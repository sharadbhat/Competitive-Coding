# Leetcode
# https://leetcode.com/problems/unique-number-of-occurrences/


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        unique = set(arr)
        d = set([arr.count(i) for i in unique])

        return len(unique) == len(d)
