class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        count = 0
        out = ""
        for i in range(len(S) - 1, -1, -1):
            count = (count + shifts[i]) % 26
            out = chr(((ord(S[i]) - 97 + count) % 26) + 97) + out
        return out
