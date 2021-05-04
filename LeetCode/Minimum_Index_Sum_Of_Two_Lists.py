# Leetcode
# https://leetcode.com/problems/minimum-index-sum-of-two-lists/


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {v: k for k, v in enumerate(list1)}
        min_val = len(list1) + len(list2)
        out = set()
        for k, v in enumerate(list2):
            if v in d:
                if k + d[v] > min_val:
                    continue
                if k + d[v] < min_val:
                    min_val = k + d[v]
                    out.clear()
                out.add(v)

        return list(out)
