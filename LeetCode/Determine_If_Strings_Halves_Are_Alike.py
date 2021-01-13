# Leetcode
# https://leetcode.com/problems/determine-if-string-halves-are-alike


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        a, b = s[:len(s) // 2], s[len(s) // 2:]
        a_count, b_count = 0, 0

        for i in 'aeiou':
            a_count += a.count(i)
            b_count += b.count(i)

        return a_count == b_count
