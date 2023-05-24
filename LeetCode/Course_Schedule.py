# Leetcode
# https://leetcode.com/problems/course-schedule

# DFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        done = set()
        q = set()
        d = {}
        for i in prerequisites:
            if i[0] not in d:
                d[i[0]] = set([i[1]])
            else:
                d[i[0]].add(i[1])
        for i in range(numCourses):
            if i not in d:
                done.add(i)
        
        def dfs(course):
            for i in d[course]:
                if i not in done:
                    if i in q:
                        return False
                    q.add(i)
                    if dfs(i):
                        done.add(i)
                    else:
                        return False
            return True

        for i in d:
            if i not in done:
                q = set([i])
                if dfs(i):
                    done.add(i)
        
        return len(done) == numCourses

# My original solution
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        done = set()
        pending = numCourses
        d = {}
        for i in prerequisites:
            if i[0] not in d:
                d[i[0]] = set([i[1]])
            else:
                d[i[0]].add(i[1])
        for i in range(numCourses):
            if i not in d:
                done.add(i)
                pending -= 1

        while pending > 0:
            updated = False
            for i in d:
                new_set = set(d[i])
                for j in d[i]:
                    if j in done:
                        new_set.remove(j)
                        if len(new_set) == 0:
                            pending -= 1
                            updated = True
                            done.add(i)
                d[i] = new_set
            if not updated:
                break
        
        return pending == 0