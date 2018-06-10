# LeetCode
# https://leetcode.com/problems/number-of-lines-to-write-string/description/

class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        line_count = 0
        i = 0
        temp_count = 0
        
        while i < len(S):
            width = widths[ord(S[i]) - 97]

            if temp_count + width < 100:
                temp_count += width
            elif temp_count + width > 100:
                line_count += 1
                temp_count = width
            else:
                line_count += 1
                temp_count = 0

            i += 1

        if temp_count != 0:
            line_count += 1

        return [line_count, temp_count]
