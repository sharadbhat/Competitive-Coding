# LeetCode
# https://leetcode.com/problems/plus-one/description/

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        pos = len(digits) - 1
        while pos >= 0:
            if digits[pos] == 9:
                digits[pos] = 0
                pos -= 1
            else:
                digits[pos] += 1
                break

        all_zero = True
        for i in digits:
            if i != 0:
                all_zero = False
                break
        if all_zero == True:
            digits = [1] + digits

        return digits
