# Leetcode
# https://leetcode.com/problems/construct-the-rectangle/


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        l = w = 0
        for i in range(int(area ** 0.5), 0, -1):
            if i * (area // i) == area:
                l = i
                w = area // i
                break

        return sorted([l, w], reverse=True)
