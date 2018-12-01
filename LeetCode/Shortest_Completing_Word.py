# LeetCode
# https://leetcode.com/problems/shortest-completing-word/

class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        licensePlate = licensePlate.lower()
        counts = {}
        for i in licensePlate:
            if i.isalpha() == True:
                counts[i] = counts.get(i, 0) + 1
        words.sort(key=len)
        for i in words:
            done = True
            for j in counts:
                if j not in i or i.count(j) < counts[j]:
                    done = False
                    break
            if done == True:
                return i
