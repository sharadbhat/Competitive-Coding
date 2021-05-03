# Leetcode
# https://leetcode.com/problems/random-flip-matrix/

from random import randint


class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.popped = set()
        self.rows = n_rows
        self.cols = n_cols

    def flip(self) -> List[int]:
        total_pos = self.rows * self.cols
        choice = None
        while True:
            choice = randint(1, total_pos) - 1
            if choice not in self.popped:
                break
        self.popped.add(choice)
        return [choice // self.cols, choice % self.cols]

    def reset(self) -> None:
        self.popped = set()

# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()
