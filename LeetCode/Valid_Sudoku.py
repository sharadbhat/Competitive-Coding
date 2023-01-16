# Leetcode
# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_val = [set() for _ in range(9)]
        col_val = [set() for _ in  range(9)]
        block_val = []
        for _ in range(3):
            block_val.append([set() for _ in range(3)])

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == '.':
                    continue
                temp_row = row // 3
                temp_col = col // 3
                if val in row_val[row] or val in col_val[col] or val in block_val[temp_row][temp_col]:
                    return False
                row_val[row].add(val)
                col_val[col].add(val)
                block_val[temp_row][temp_col].add(val)
        return True

# Alternate Block Set Solution

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_val = [set() for _ in range(9)]
        col_val = [set() for _ in  range(9)]
        block_val = [set() for _ in  range(9)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == '.':
                    continue
                block_idx = (3 * (row // 3)) + col // 3
                if val in row_val[row] or val in col_val[col] or val in block_val[block_idx]:
                    return False
                row_val[row].add(val)
                col_val[col].add(val)
                block_val[block_idx].add(val)
        return True