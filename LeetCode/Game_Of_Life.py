# LeetCode
# https://leetcode.com/problems/game-of-life/

class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def get_live_neighbors(board, x, y):
            neighbors = []
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                        neighbors.append(board[i][j])
            return sum(neighbors) - board[x][y]
        rows = len(board)
        columns = len(board[0])
        temp_board = [[0] * (columns + 2)] + [([0] + i + [0]) for i in board] + [[0] * (columns + 2)]
        for row in range(1, len(board) + 1):
            for column in range(1, len(board[0]) + 1):
                count = get_live_neighbors(temp_board, row, column)
                if count not in {2, 3}:
                    board[row - 1][column - 1] = 0
                elif count == 3:
                    board[row - 1][column - 1] = 1
