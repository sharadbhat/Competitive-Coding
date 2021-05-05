# Leetcode
# https://leetcode.com/problems/rearrange-words-in-a-sentence/


class Solution:
    def arrangeWords(self, text: str) -> str:
        arr = sorted(text.split(), key=len)
        return ' '.join(arr).capitalize()
