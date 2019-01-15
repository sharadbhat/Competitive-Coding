# LeetCode
# https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        def distance(x, y):
            return (x ** 2 + y ** 2) ** 0.5
        d = {}
        for i in points:
            d[tuple(i)] = distance(i[0], i[1])
        l = sorted(d, key=d.get)
        return l[:K]
