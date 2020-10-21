# Leetcode
# https://leetcode.com/problems/third-maximum-number/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        order = [None, None, None]
        for i in nums:
            if order[0] == None or i > order[0]:
                order.insert(0, i)
                order.pop()
            elif order[1] == None or i > order[1]:
                order.insert(1, i)
                order.pop()
            elif order[2] == None or i > order[2]:
                order[2] = i
        if order[2] == None:
            return order[0]
        return order[2]