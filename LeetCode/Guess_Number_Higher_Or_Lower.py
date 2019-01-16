# LeetCode
# https://leetcode.com/problems/guess-number-higher-or-lower/

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        while True:
            mid = (low + high) // 2
            val = guess(mid)
            if val == 0:
                return mid
            if val == -1:
                high = mid - 1
            else:
                low = mid + 1
