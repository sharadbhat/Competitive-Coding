# LeetCode
# https://leetcode.com/problems/available-captures-for-rook/

class Solution:
    def numRookCaptures(self, board):
        captures = 0
        rook_pos = None
        position = None
        for pos, i in enumerate(board):
            if "R" in i:
                position = pos
                rook_pos = i.index("R")
                left = [j for j in i[:rook_pos] if j != "."]
                right = [j for j in i[rook_pos+1:] if j != "."]
                if len(left) > 0 and left[-1] == "p":
                    captures += 1
                if len(right) > 0 and right[0] == "p":
                    captures += 1
                break
        vertical_top = [i[rook_pos] for i in board[:position] if i[rook_pos] != "."]
        vertical_bottom = [i[rook_pos] for i in board[position + 1:] if i[rook_pos] != "."]
        if len(vertical_top) > 0 and vertical_top[-1] == "p":
            captures += 1
        if len(vertical_bottom) > 0 and vertical_bottom[0] == "p":
            captures += 1
        return captures
        
        