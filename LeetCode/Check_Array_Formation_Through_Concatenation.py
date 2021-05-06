# Leetcode
# https://leetcode.com/problems/check-array-formation-through-concatenation/


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d = {i[0]: i for i in pieces}

        i = 0
        while i < len(arr):
            if arr[i] in d:
                length = len(d[arr[i]])
                if arr[i:i+length] != d[arr[i]]:
                    return False
                i += length
            else:
                return False

        return True
