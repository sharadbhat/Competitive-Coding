# Leetcode
# https://leetcode.com/problems/relative-ranks/


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        d = {
            0: "Gold Medal",
            1: "Silver Medal",
            2: "Bronze Medal"
        }
        sorted_scores = sorted(score, reverse=True)
        out = []
        for i in score:
            pos = sorted_scores.index(i)
            out.append(d[pos] if pos < 3 else str(pos + 1))
        return out
