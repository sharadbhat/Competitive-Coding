# LeetCode
# https://leetcode.com/problems/maximum-swap/description/

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        for i in range(len(num) - 1):
            j = max(num[i + 1:])
            if num[i] < j:
                k = i + len(num[i + 1:]) - (num[i + 1:])[::-1].index(j)
                return int(num[:i] + num[k] + num[i + 1:k] + num[i] + num[k + 1:])
        return int(num)
