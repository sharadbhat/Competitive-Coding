# Leetcode
# https://leetcode.com/problems/last-stone-weight/


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while len(stones) > 1:
            stone1, stone2 = stones.pop(), stones.pop()
            if stone1 != stone2:
                stones.append(abs(stone1 - stone2))
                stones.sort()

        if len(stones) == 1:
            return stones.pop()

        return 0
