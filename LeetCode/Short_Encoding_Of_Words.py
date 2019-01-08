# LeetCode
# https://leetcode.com/problems/short-encoding-of-words/

class Solution:
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = set(words)
        words2 = words.copy()
        for word in words2:
            for i in range(1, len(word)):
                words.discard(word[i:])
        return sum([len(i) + 1 for i in words])
