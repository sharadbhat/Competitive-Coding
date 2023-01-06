# Leetcode
# https://leetcode.com/problems/count-pairs-of-similar-strings/

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count_dict = {}
        for word in words:
            index = ''.join(sorted(set(list(word))))
            count_dict[index] = count_dict.get(index, 0) + 1
        out = 0
        for val in count_dict.values():
            out += (val * (val - 1)) // 2
        return out