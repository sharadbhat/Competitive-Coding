# LeetCode
# https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, N, trust):
        for i in range(1, N + 1):
            temp_trust = True
            for j in range(1, N + 1):
                if j != i:
                    if [j, i] not in trust:
                        temp_trust = False
                        break
            if temp_trust == True:
                if True not in [k[0] == i for k in trust]:
                    return i
        return -1