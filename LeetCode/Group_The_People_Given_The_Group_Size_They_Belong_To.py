# Leetcode
# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        out = []
        d = defaultdict(list)
        for pos, val in enumerate(groupSizes):
            d[val].append(pos)

        for size in d:
            out.extend(self.getChunks(d[size], size))

        return out

    def getChunks(self, arr: List[int], chunk_size: int):
        chunks = []
        for i in range(0, len(arr), chunk_size):
            chunks.append(arr[i:i + chunk_size])
        return chunks
