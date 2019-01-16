# LeetCode
# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/

from random import choice

class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.l = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.d[val] = self.d.get(val, 0) + 1
        self.l.append(val)
        return self.d[val] == 1

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.d and self.d[val] > 0:
            self.d[val] -= 1
            self.l.remove(val)
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return choice(self.l)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
