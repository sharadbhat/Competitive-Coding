# Leetcode
# https://leetcode.com/problems/replace-all-digits-with-characters/


class Solution:
    def replaceDigits(self, s: str) -> str:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        out = ''
        for pos, letter in enumerate(s):
            if pos % 2 == 0:
                out += letter
            else:
                diff = int(letter)
                out += letters[letters.index(s[pos - 1]) + diff]
        return out
