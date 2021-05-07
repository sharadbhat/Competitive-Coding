# LeetCode
# https://leetcode.com/problems/uncommon-words-from-two-sentences/

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        d_a = {}
        d_b = {}
        for i in A.split():
            d_a[i] = d_a.get(i, 0) + 1
        for i in B.split():
            d_b[i] = d_b.get(i, 0) + 1
        l = [i for i in d_a if d_a[i] < 2 and i not in d_b]
        l += [i for i in d_b if d_b[i] < 2 and i not in d_a]
        return l
