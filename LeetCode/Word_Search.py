# Leetcode
# https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        i = 0
        visited = []
        for row in board:
            visited.append([False] * len(board[0]))

        def recurse(x, y, char_pos, visited):
            if char_pos == len(word) - 1:
                return True
            char_pos += 1
            res = False
            for new_x, new_y in zip([x - 1, x + 1, x, x], [y, y, y - 1, y + 1]):
                if new_x < 0 or new_y < 0 or new_x >= len(board) or new_y >= len(board[0]):
                    continue
                if not visited[new_x][new_y] and board[new_x][new_y] == word[char_pos]:
                    visited[new_x][new_y] = True
                    res = recurse(new_x, new_y, char_pos, visited)
                    if not res:
                        visited[new_x][new_y] = False
                    else:
                        break
            return res

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0]:
                    visited[x][y] = True
                    if recurse(x, y, 0, visited):
                        return True
                    else:
                        visited[x][y] = False
        return False