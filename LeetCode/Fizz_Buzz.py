# LeetCode
# https://leetcode.com/problems/fizz-buzz/description/

class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = []
        for i in range(1, n + 1):
            s = ""
            if i % 3 == 0:
                s += "Fizz"
            if i % 5 == 0:
                s += "Buzz"
            if s == "":
                l.append(str(i))
            else:
                l.append(s)
        return l
