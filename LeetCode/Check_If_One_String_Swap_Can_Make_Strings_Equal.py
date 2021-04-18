# Leetcode
# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff_count = 0
        set1, set2 = set(), set()
        for i, j in zip(s1, s2):
            set1.add(i)
            set2.add(j)
            if i != j:
                diff_count += 1
        return diff_count in (0, 2) and set1 == set2
