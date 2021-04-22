# Leetcode
# https://leetcode.com/problems/truncate-sentence


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        space_count = 0
        out = ''
        for i in s:
            if i == ' ':
                space_count += 1
                if space_count == k:
                    break
            out += i
        return out
