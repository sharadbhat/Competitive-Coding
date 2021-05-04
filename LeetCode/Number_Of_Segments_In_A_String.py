# Leetcode
# https://leetcode.com/problems/number-of-segments-in-a-string/


class Solution:
    def countSegments(self, s: str) -> int:
        if not s:
            return 0

        count = 0
        word_curr = False
        for i in s:
            if i != ' ':
                if not word_curr:
                    count += 1
                    word_curr = True
            else:
                if word_curr:
                    word_curr = False

        return count
