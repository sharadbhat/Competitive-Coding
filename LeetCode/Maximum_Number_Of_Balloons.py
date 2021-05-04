# Leetcode
# https://leetcode.com/problems/maximum-number-of-balloons/


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {}
        for i in text:
            if i in 'balon':
                d[i] = d.get(i, 0) + 1

        if 'l' in d:
            d['l'] = d['l'] // 2
        if 'o' in d:
            d['o'] = d['o'] // 2

        if len(d) == 5:
            return min(d.values())
        return 0
