# Leetcode
# https://leetcode.com/problems/decode-xored-array


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        out = [first]
        for i in range(len(encoded)):
            out.append(out[i] ^ encoded[i])
        return out
