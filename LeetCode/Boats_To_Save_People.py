# Leetcode
# https://leetcode.com/problems/boats-to-save-people/


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        start = 0
        end = len(people) - 1

        while start <= end:
            if people[start] + people[end] <= limit:
                end -= 1
            start += 1

        return start
