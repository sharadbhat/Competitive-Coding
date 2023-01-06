# Leetcode
# https://leetcode.com/problems/design-memory-allocator/

class Allocator:

    def __init__(self, n: int):
        self.n = n
        self.memory = [None] * n

    def allocate(self, size: int, mID: int) -> int:
        start = 0
        while self.memory[start] != None:
            start += 1
            if start >= self.n:
                return -1
        while start < self.n:
            if start + size > self.n:
                return -1
            found = True
            for end in range(size):
                if self.memory[start + end] != None:
                    start += end + 1
                    found = False
                    break
            if found:
                for end in range(size):
                    self.memory[start + end] = mID
                break
        return start

    def free(self, mID: int) -> int:
        count = 0
        for i in range(len(self.memory)):
            if self.memory[i] == mID:
                count += 1
                self.memory[i] = None
        return count

# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)