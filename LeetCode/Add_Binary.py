# LeetCode
# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        longest = max(len(a), len(b))
        a = "0" * (longest - len(a)) + a
        b = "0" * (longest - len(b)) + b
        carry = [0] * (longest + 1)
        out = ""
        for i in range(longest - 1, -1, -1):
            val = int(a[i]) + int(b[i]) + carry[i + 1]
            if val > 1:
                carry[i] = 1
                val = 0 if val == 2 else 1
            out = str(val) + out
        if carry[0] == 1:
            out = "1" + out
        return out
