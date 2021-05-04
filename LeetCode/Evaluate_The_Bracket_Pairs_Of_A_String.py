# Leetcode
# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = {i[0]: i[1] for i in knowledge}
        out = ''
        i = 0
        brac_open = False
        temp_word = ''
        while i < len(s):
            if s[i] == '(':
                brac_open = True
            elif s[i] == ')':
                brac_open = False
                out += d.get(temp_word, '?')
                temp_word = ''
            else:
                if not brac_open:
                    out += s[i]
                else:
                    temp_word += s[i]
            i += 1
        return out
