# Leetcode
# https://leetcode.com/problems/longest-repeating-character-replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {s[0]: 1}
        longest = 0
        l, r = 0, 0

        while r < len(s):
            width = r - l + 1
            most_freq = None
            for i in counts:
                if most_freq == None or counts[i] > counts[most_freq]:
                    most_freq = i
            if width - counts[most_freq] <= k:
                longest = max(longest, width)
                r += 1
                if r == len(s):
                    break
                counts[s[r]] = counts.get(s[r], 0) + 1
            else:
                l += 1
                counts[s[l - 1]] -= 1
            
        return longest
