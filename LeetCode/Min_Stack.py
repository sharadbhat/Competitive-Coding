# LeetCode
# https://leetcode.com/problems/min-stack/description/

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []
        self.stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.min_stack) == 0 or x <= self.min_stack[-1]:
            self.min_stack.append(x)


    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                del self.min_stack[-1]
            del self.stack[-1]


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1] if self.stack else None


    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1] if self.stack else None



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
