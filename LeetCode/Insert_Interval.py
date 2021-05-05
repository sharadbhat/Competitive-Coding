# Leetcode
# https://leetcode.com/problems/insert-interval/


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals = sorted(intervals + [newInterval])

        i = 1
        curr = 0
        while i < len(intervals):
            done = False
            curr_start, curr_stop = intervals[curr]
            start, stop = intervals[i]
            if curr_start >= start and curr_start <= stop:
                done = True
            elif curr_stop >= start and curr_stop <= stop:
                done = True
            elif curr_start < start and curr_stop > stop:
                done = True

            if done:
                intervals[curr][0] = min(start, curr_start)
                intervals[curr][1] = max(stop, curr_stop)
                intervals.pop(i)
                continue

            curr = i
            i += 1

        return intervals
