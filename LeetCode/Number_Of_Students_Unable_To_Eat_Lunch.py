# Leetcode
# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i = 0
        while True:
            if len(sandwiches) > i and sandwiches[i] in students:
                students.remove(sandwiches[i])
                i += 1
            else:
                return len(students)
