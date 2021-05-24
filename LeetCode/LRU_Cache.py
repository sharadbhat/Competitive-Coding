# Leetcode
# https://leetcode.com/problems/lru-cache/


class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.queue = deque()
        self.max_cap = capacity

    def get(self, key: int) -> int:
        if key in self.d:
            self.queue.remove(key)
            self.queue.append(key)
            return self.d[key]

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key] = value
            self.queue.remove(key)
            self.queue.append(key)
        else:
            if len(self.queue) == self.max_cap:
                self.d.pop(self.queue.popleft())
            self.d[key] = value
            self.queue.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
