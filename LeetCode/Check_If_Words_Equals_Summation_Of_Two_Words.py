# Leetcode
# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return self.getTotal(firstWord) + self.getTotal(secondWord) == self.getTotal(targetWord)

    def getTotal(self, word: str) -> int:
        total = 0
        for i in word:
            digit = ord(i) - 97
            total *= 10
            total += digit

        return total
