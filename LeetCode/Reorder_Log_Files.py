# LeetCode
# https://leetcode.com/problems/reorder-log-files/

class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digit_logs = []
        letter_logs = []
        for i in logs:
            split_log = i.split()
            try:
                int(split_log[1])
                digit_logs.append(i)
            except:
                letter_logs.append(' '.join(split_log[1:] + split_log[:1]))
        letter_logs.sort()
        out = []
        for i in letter_logs:
            split_log = i.split()
            out.append(' '.join(split_log[-1:] + split_log[:-1]))
        return out + digit_logs
