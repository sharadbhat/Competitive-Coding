# LeetCode
# https://leetcode.com/problems/self-dividing-numbers/description/

class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        out = []
        for i in range(left, right + 1):
            self_dividing = True
            num = i
            while num > 0:
                try:
                    if i % (num % 10) != 0:
                        self_dividing = False
                        break
                except:
                    self_dividing = False
                    break
                num //=10
            if self_dividing == True:
                out.append(i)
        return out
