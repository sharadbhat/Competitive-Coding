# LeetCode
# https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        output = []
        for word in words:
            remove = False
            d = {}
            for i, j in zip(word, pattern):
                if i not in d:
                    if j not in d.values():
                        d[i] = j
                    else:
                        remove = True
                        break
                if i in d:
                    if d[i] != j:
                        remove = True
            if remove == False:
                output.append(word)
        return output
