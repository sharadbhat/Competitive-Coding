# LeetCode
# https://leetcode.com/problems/merge-sorted-array/description/


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        if n:
            while m + j < m + n:
                if nums1[i] >= nums2[j] or i >= m + j:
                    nums1.insert(i, nums2[j])
                    nums1.pop()
                    j += 1
                i += 1
