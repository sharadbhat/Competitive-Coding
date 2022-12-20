# Leetcode
# https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(pos):
            for key in rooms[pos]:
                if key not in visited:
                    visited.add(key)
                    dfs(key)
        visited = set([0])
        dfs(0)
        return len(visited) == len(rooms)