# Leetcode
# https://leetcode.com/problems/merge-similar-items/

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        value_dict = {}
        for item in items1:
            value_dict[item[0]] = value_dict.get(item[0], 0) + item[1]
        for item in items2:
            value_dict[item[0]] = value_dict.get(item[0], 0) + item[1]
        
        return [[i, value_dict[i]] for i in sorted(value_dict)]
