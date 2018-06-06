# LeetCode
# https://leetcode.com/problems/min-stack/description/

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.top_element = -1
        self.stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.top_element += 1
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.top_element -= 1
        del self.stack[-1]


    def top(self):
        """
        :rtype: int
        """
        return self.stack[self.top_element]


    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
