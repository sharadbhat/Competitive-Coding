# Leetcode
# https://leetcode.com/problems/find-common-characters/


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        d = {i: A[0].count(i) for i in A[0]}
        for i in A[1:]:
            for j in d:
                d[j] = min(d[j], i.count(j))

        out = []
        for i in d:
            out += [i] * d[i]

        return out
