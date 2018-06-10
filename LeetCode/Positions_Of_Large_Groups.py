# LeetCode
# https://leetcode.com/problems/positions-of-large-groups/description/

class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        if len(S) == 0:
            return []
        start = 0
        curr = 1
        curr_letter = S[0]
        count = 1
        l = []
        while curr < len(S):
            if S[curr] == curr_letter:
                count += 1
            else:
                if count > 2:
                    l.append([start, curr - 1])
                count = 1
                start = curr
                curr_letter = S[curr]
            curr += 1
        if count > 2:
            l.append([start, curr - 1])
        return l
