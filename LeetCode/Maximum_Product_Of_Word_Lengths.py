# Leetcode
# https://leetcode.com/problems/maximum-product-of-word-lengths/


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_prod = 0
        words = [[set(i), len(i)] for i in words]
        for i in range(len(words) - 1):
            for j in range(i, len(words)):
                if not words[i][0] & words[j][0]:
                    max_prod = max(max_prod, words[i][1] * words[j][1])
        return max_prod
