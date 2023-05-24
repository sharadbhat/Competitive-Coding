# Leetcode
# https://leetcode.com/problems/time-based-key-value-store

class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = [(timestamp, value)]
        else:
            self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d or self.d[key][0][0] > timestamp:
            return ''

        out = ''
        left, right = 0, len(self.d[key]) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.d[key][mid][0] == timestamp:
                out = self.d[key][mid][1]
                break
            elif self.d[key][mid][0] > timestamp:
                right = mid - 1
            else:
                out = self.d[key][mid][1]
                left = mid + 1
        return out


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)