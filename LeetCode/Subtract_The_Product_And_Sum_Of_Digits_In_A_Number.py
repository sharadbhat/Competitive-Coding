# Leetcode
# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product, sum_total = 1, 0
        while n:
            digit = n % 10
            n //= 10
            product *= digit
            sum_total += digit

        return product - sum_total
