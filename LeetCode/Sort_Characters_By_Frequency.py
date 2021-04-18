# Leetcode
# https://leetcode.com/problems/sort-characters-by-frequency


class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
        return ''.join(i * d[i] for i in sorted(d, key=d.get, reverse=True))
