# Leetcode
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        out = []
        if len(digits) == 1:
            return list(d[digits[0]])

        sub = self.letterCombinations(digits[1:])
        for letter in d[digits[0]]:
            for combo in sub:
                out.append(letter + combo)

        return out
