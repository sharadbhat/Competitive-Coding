# Leetcode
# https://leetcode.com/problems/course-schedule-ii

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = {}
        done = set([i for i in range(numCourses)])

        for i in prerequisites:
            c1, c2 = i[0], i[1]
            pre[c1] = pre.get(c1, []) + [c2]
            if c1 in done:
                done.remove(c1)

        def dfs(curr, path):
            temp = []
            path.add(curr)
            for course in pre[curr]:
                if course in path:
                    return -1
                if course not in done:
                    temp2 = dfs(course, path)
                    if temp2 == -1:
                        return -1
                    temp += temp2
                    path.remove(course)

            done.add(curr)
            return temp + [curr]

        out = list(done)
        for i in range(numCourses):
            if i not in done:
                temp = dfs(i, set([]))
                if temp == -1:
                    return []
                out += temp

        return out
