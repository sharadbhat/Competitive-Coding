# Leetcode
# https://leetcode.com/problems/sorting-the-sentence/


class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        out = [None] * len(words)

        for word in words:
            pos = -1
            i = len(word) - 1
            while i > -1:
                try:
                    pos = int(word[i:])
                    i -= 1
                except:
                    break
            out[pos - 1] = word[:i + 1]
        return ' '.join(out)
