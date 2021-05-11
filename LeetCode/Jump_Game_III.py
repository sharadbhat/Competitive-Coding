# Leetcode
# https://leetcode.com/problems/jump-game-iii/


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        return self.check(arr, start, set())

    def check(self, arr: List[int], curr: int, visited: set) -> bool:
        if curr < 0 or curr >= len(arr) or curr in visited:
            return False

        visited.add(curr)

        if arr[curr] == 0:
            return True

        return self.check(arr, curr + arr[curr], visited) or self.check(arr, curr - arr[curr], visited)
