# Leetcode
# https://leetcode.com/problems/accounts-merge

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        d = {}
        out = []
        for item in accounts:
            if item[0] not in d:
                d[item[0]] = [set(item[1:])]
            else:
                d[item[0]].append(set(item[1:]))

        for item in d:
            if len(d[item]) == 1:
                out.append([item] + sorted([i for i in d[item][0]]))
            else:
                i, j = 0, 0
                while i in range(len(d[item])):
                    updated = False
                    j = i + 1
                    while j in range(i + 1, len(d[item])):
                        temp = d[item][i].union(d[item][j])
                        if len(temp) < (len(d[item][i]) + len(d[item][j])):
                            del d[item][j]
                            del d[item][i]
                            updated = True
                            j -= 1
                            d[item].append(temp)
                        j += 1
                    if not updated:
                        i += 1

                for i in d[item]:
                    out.append([item] + sorted([j for j in i]))

        return out