# LeetCode
# https://leetcode.com/problems/implement-stack-using-queues/description/

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        q2 = []
        for i in self.q1:
            q2.append(i)
        q2.append(x)
        self.q1[:] = q2[:]


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        q2 = []
        while len(self.q1) > 1:
            q2.append(self.q1[0])
            del self.q1[0]
        last = self.q1[0]
        del self.q1[0]
        self.q1[:] = q2[:]
        return last


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        q2 = []
        while len(self.q1) > 1:
            q2.append(self.q1[0])
            del self.q1[0]
        last = self.q1[0]
        q2.append(self.q1[0])
        self.q1[:] = q2[:]
        return last


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if len(self.q1) == 0:
            return True
        return False



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
