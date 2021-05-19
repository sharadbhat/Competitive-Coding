# Leetcode
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = -1
        out = []
        for i in arr[::-1]:
            out.insert(0, max_val)
            max_val = max(max_val, i)

        return out
