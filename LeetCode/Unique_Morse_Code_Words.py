# LeetCode
# https://leetcode.com/problems/unique-morse-code-words/description/

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        s = set()

        for word in words:
            word_morse = ""
            for letter in word:
                word_morse += morse[ord(letter) - 97]
            if word_morse not in s:
                s.add(word_morse)
        return len(s)
