# LeetCode
# https://leetcode.com/problems/sort-array-by-parity-ii/description/

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = sorted([i for i in A if i % 2 == 0])
        odd = sorted([i for i in A if i % 2 == 1])
        output = []
        for i in range(len(even)):
            output +=  [even[i], odd[i]]
        return output
