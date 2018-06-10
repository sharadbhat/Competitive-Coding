# LeetCode
# https://leetcode.com/problems/goat-latin/description/

class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        a_count = 1
        vowels = ['a', 'e', 'i', 'o', 'u']
        s = S.split()
        o = []
        for i in s:
            if i[0].lower() in vowels:
                o.append(i + "ma" + "a" * a_count)
            else:
                o.append(i[1:] + i[0] + "ma" + "a" * a_count)
            a_count += 1
        return ' '.join(o)
