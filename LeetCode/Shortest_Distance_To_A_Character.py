# LeetCode
# https://leetcode.com/problems/shortest-distance-to-a-character/description/

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        dist = []
        d = {}
        for i in range(len(S)):
            if S[i] == C:
                dist.append(0)
                d[S[i]] = i
            else:
                if C in d:
                    if C in S[i + 1:]:
                        dist.append(min(abs(d[C] - i), S[i + 1:].index(C) + 1))
                    else:
                        dist.append(abs(d[C] - i))
                else:
                    dist.append(S[i + 1:].index(C) + 1)
        return dist
