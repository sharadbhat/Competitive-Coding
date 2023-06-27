# Leetcode
# https://leetcode.com/problems/push-dominoes

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        lst = [[] for _ in range(len(dominoes))]

        closest_r = -1
        for i in range(len(dominoes)):
            if dominoes[i] == 'R':
                closest_r = i
            elif dominoes[i] == 'L':
                closest_r = -1

            lst[i].append(i - closest_r if closest_r > -1 else sys.maxsize)

        closest_l = -1
        for i in range(len(dominoes) - 1, -1, -1):
            if dominoes[i] == 'L':
                closest_l = i
            elif dominoes[i] == 'R':
                closest_l = -1

            lst[i].append(closest_l - i if closest_l > -1 else sys.maxsize)
        
        out = ''
        for i in range(len(dominoes)):
            temp = ''
            if lst[i][0] == lst[i][1]:
                temp = '.'
            elif lst[i][0] == sys.maxsize or lst[i][1] < lst[i][0]:
                temp = 'L'
            else:
                temp = 'R'

            out += temp
        
        return out