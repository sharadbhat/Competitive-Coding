# Leetcode
# https://leetcode.com/problems/finding-the-users-active-minutes/


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        d = defaultdict(set)
        for user, minute in logs:
            d[user].add(minute)

        out = [0] * k
        for i in d:
            out[len(d[i]) - 1] += 1

        return out
