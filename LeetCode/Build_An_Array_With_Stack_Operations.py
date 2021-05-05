# Leetcode
# https://leetcode.com/problems/build-an-array-with-stack-operations/


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        curr = 1
        out = []
        i = 0
        while i < len(target):
            if target[i] == curr:
                out.append("Push")
                i += 1
            else:
                out += ["Push", "Pop"]
            curr += 1
        return out
