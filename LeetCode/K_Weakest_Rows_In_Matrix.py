# Leetcode
# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d = {}
        for i in range(len(mat)):
            d[i] = sum(mat[i])

        return sorted(d, key=d.get)[:k]
