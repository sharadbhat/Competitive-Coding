# LeetCode
# https://leetcode.com/problems/most-common-word/description/

class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned = set(banned)
        punc = set(["!", "?", "'", ";", ".", ","])
        paragraph = ''.join([i.lower() for i in paragraph if i not in punc])
        d = {}
        max_count = 0
        max_word = ""
        for i in paragraph.split():
            if i not in banned:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
                if max_count < d[i]:
                    max_count = d[i]
                    max_word = i
        return max_word
