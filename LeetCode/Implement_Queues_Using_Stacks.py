# LeetCode
# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        self.first = None

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.s1.append(x)
        if self.first == None:
            self.first = x

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while len(self.s1) > 1:
            self.s2.append(self.s1.pop())
        temp = self.s1.pop()
        self.first = None
        while self.s2:
            self.push(self.s2.pop())
        return temp

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.first

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.s1

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
