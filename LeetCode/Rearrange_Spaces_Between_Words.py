# LeetCode
# https://leetcode.com/problems/rearrange-spaces-between-words/

class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        word_count = len(words)
        spaces = text.count(" ")
        spaces_in_between = spaces // ((word_count - 1) if word_count > 1 else 1)
        remainder_spaces = (spaces % (word_count - 1)) if word_count > 1 else spaces
        return (" " * spaces_in_between).join(words) + (" " * remainder_spaces)