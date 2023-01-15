# Leetcode
# https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        if s == '':
            return ['']
        
        out = set()
        perms = self.letterCasePermutation(s[1:])
        for perm in perms:
            out.add(s[0].lower() + perm)
            out.add(s[0].upper() + perm)
        return out