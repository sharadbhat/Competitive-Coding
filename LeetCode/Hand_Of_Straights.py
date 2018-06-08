# LeetCode
# https://leetcode.com/problems/hand-of-straights/description/

class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        l = len(hand)
        if l % W != 0:
            return False

        d = {}
        for i in hand: # Count of each number
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        i = 0

        while i < (l // W):
            j = 1
            a = min(d)

            d[a] -= 1 # Reduce count
            if d[a] == 0:
                del d[a]
            while j < W:
                if (a + 1) in d:
                    if d[a + 1] <= 0:
                        return False
                    d[a + 1] -= 1
                    if d[a + 1] == 0:
                        del d[a + 1]
                    a += 1
                else:
                    return False
                j += 1
            i += 1
        return True
