# Leetcode
# https://leetcode.com/problems/design-an-ordered-stream/

class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value
        if self.ptr == idKey - 1:
            out = []
            i = self.ptr
            for i in self.stream[self.ptr:]:
                if i == None:
                    break
                out.append(i)
            self.ptr += len(out)
            return out


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)