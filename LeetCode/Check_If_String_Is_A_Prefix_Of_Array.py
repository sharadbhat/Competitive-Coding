# Leetcode
# https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        gen_string = ''
        if s == '':
            return True
        for word in words:
            gen_string += word
            if gen_string == s:
                return True
        return False