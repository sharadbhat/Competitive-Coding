# Leetcode
# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        found = False
        ended = False
        for i in s:
            if i == '1':
                if ended:
                    return False
                found = True
            else:
                if found:
                    ended = True

        return found
