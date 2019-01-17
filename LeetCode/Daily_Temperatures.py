# LeetCode
# https://leetcode.com/problems/daily-temperatures/

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        T = T[::-1]
        output = [0]
        stack = [(T[0], 0)]
        j = 1
        for i in range(1, len(T)):
            while len(stack) > 0 and stack[-1][0] <= T[i]:
                del stack[-1]
            if len(stack) == 0:
                output.append(0)
            else:
                output.append(j - stack[-1][1])
            stack.append((T[i], j))
            j += 1
        return output[::-1]
