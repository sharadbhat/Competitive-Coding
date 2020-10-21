# LeetCode
# https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/

import string
import random

class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        for i in range(0, len(s)):
            if s[i] == '?':
                while True:
                    check1 = True
                    check2 = True
                    s[i] = self.randomCharacter()
                    if i > 0 and s[i - 1] == s[i]:
                        check1 = False
                    if i < (len(s) - 1) and s[i + 1] == s[i]:
                        check2 = False
                    if check1 and check2:
                        break
        return ''.join(s)

    def randomCharacter(self) -> str:
        return random.choice(string.ascii_lowercase)