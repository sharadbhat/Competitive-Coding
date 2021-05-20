# Leetcode
# https://leetcode.com/problems/destination-city/


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        has_outgoing = set()
        dest = set()
        for i in paths:
            has_outgoing.add(i[0])
            if i[1] not in has_outgoing:
                dest.add(i[1])
            dest.discard(i[0])

        return dest.pop()
