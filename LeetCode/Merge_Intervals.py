# Leetcode
# https://leetcode.com/problems/merge-intervals


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        out = []

        start, end = intervals[0]
        for i in intervals:
            if i[0] <= end:
                end = max(end, i[1])
            else:
                out.append([start, end])
                start, end = i

        out.append([start, end])

        return out
