# LeetCode
# https://leetcode.com/problems/unique-email-addresses/

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        count = 0
        s = set()
        for i in emails:
            a = i.split('@')
            domain = a[1]
            first = a[0].split('+')[0].replace('.', '')
            if first + domain not in s:
                s.add(first + domain)
                count += 1
        return count
