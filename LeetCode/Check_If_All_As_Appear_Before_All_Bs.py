# Leetcode
# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

class Solution:
    def checkString(self, s: str) -> bool:
        b_seen = False
        for i in s:
            if i == 'b':
                b_seen = True
            if i == 'a' and b_seen:
                return False
        return True