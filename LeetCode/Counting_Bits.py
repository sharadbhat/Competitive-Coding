# Leetcode
# https://leetcode.com/problems/counting-bits/


class Solution:
    def countBits(self, num: int) -> List[int]:
        out = [0] if num == 0 else [0, 1]
        for i in range(2, num + 1):
            if i % 2 == 0:
                out.append(out[i // 2])
            else:
                out.append(out[i // 2] + 1)
        return out
