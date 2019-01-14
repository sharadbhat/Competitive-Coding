# LeetCode
# https://leetcode.com/problems/bulls-and-cows/

class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        guess_dict = {}
        cows = 0
        bulls = 0
        skip = set()
        for pos, val in enumerate(guess):
            if val == secret[pos]:
                bulls += 1
                skip.add(pos)
            else:
                guess_dict[val] = guess_dict.get(val, 0) + 1
        for pos, val in enumerate(secret):
            if pos not in skip:
                if val in guess_dict:
                    cows += 1
                    guess_dict[val] -= 1
                    if guess_dict[val] == 0:
                        del guess_dict[val]
        return f'{bulls}A{cows}B'
