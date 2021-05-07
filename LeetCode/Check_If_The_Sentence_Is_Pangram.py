# Leetcode
# https://leetcode.com/problems/check-if-the-sentence-is-pangram


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = set()
        for i in sentence:
            letters.add(i)
        return len(letters) == 26
