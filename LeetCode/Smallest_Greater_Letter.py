# LeetCode
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        letters2 = sorted(letters[:])
        letters = sorted([i for i in letters if ord(i) > ord(target)])
        if letters:
            return letters[0]
        return letters2[0]
