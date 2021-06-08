# Leetcode
# https://leetcode.com/problems/find-all-anagrams-in-a-string/


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        s_len = len(s)
        p_len = len(p)
        s_count = Counter(s[:p_len])
        out = []
        if p_count == s_count:
            out.append(0)

        for i in range(1, s_len - p_len + 1):
            if s_count[s[i-1]] == 1:
                del s_count[s[i - 1]]
            else:
                s_count[s[i - 1]] -= 1
            s_count[s[i + p_len - 1]] = s_count.get(s[i + p_len - 1], 0) + 1

            if p_count == s_count:
                out.append(i)

        return out
