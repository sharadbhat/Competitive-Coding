# Leetcode
# https://leetcode.com/problems/count-the-number-of-consistent-strings


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set([i for i in allowed])
        count = 0
        for word in words:
            add = 1
            for character in word:
                if character not in allowed:
                    add = 0
                    break
            count += add
        return count
