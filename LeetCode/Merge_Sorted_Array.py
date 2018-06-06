# LeetCode
# https://leetcode.com/problems/merge-sorted-array/description/

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        pos_one = 0
        pos_two = 0
        added = 0
        while pos_one < (m + added) and pos_two < n:
            if nums1[pos_one] > nums2[pos_two]:
                nums1.insert(pos_one, nums2[pos_two])
                pos_two += 1
                added += 1
                del nums1[-1]
            pos_one += 1

        while pos_two < n:
            nums1.insert(pos_one, nums2[pos_two])
            pos_two += 1
            pos_one += 1
            del nums1[-1]
