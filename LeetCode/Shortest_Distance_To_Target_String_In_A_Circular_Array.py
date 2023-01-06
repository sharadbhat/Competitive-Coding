# Leetcode
# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/

class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        positions = []
        for pos in range(len(words)):
            if words[pos] == target:
                positions.append(pos)
        dist = None
        for pos in positions:
            if dist == None:
                dist = min(abs(pos - startIndex), len(words) - abs(pos - startIndex))
            else:
                dist = min(dist, abs(pos - startIndex), len(words) - abs(pos - startIndex))
        return dist if dist != None else -1