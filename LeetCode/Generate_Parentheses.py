# Leetcode
# https://leetcode.com/problems/generate-parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = set()

        def recurse(curr, rem_o, rem_c):
            if rem_o == 0 and rem_c == 0:
                out.add(curr)
                return

            if rem_o > 0:
                recurse(curr + '(', rem_o - 1, rem_c)
            if rem_c > rem_o:
                recurse(curr + ')', rem_o, rem_c - 1)

        recurse('', n, n)

        return list(out)