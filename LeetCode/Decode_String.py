# Leetcode
# https://leetcode.com/problems/decode-string/


class Solution:
    def decodeString(self, s: str) -> str:
        out = ''
        i = 0
        while i < len(s):
            if s[i] in 'abcdefghijklmnopqrstuvwxyz':
                out += s[i]
            elif s[i] in '1234567890':
                j = i + 1
                while s[j] != '[':
                    j += 1
                multiplier = int(s[i:j])
                k = j + 1
                bracket_count = 1
                while k < len(s):
                    if s[k] == '[':
                        bracket_count += 1
                    elif s[k] == ']':
                        bracket_count -= 1
                        if bracket_count == 0:
                            break
                    k += 1
                out += multiplier * self.decodeString(s[j + 1:k])
                i = k
            i += 1
        return out
