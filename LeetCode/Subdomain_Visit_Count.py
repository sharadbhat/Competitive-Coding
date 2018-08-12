# LeetCode
# https://leetcode.com/problems/subdomain-visit-count/description/

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        d = {}
        for i in cpdomains:
            temp = i.split()
            k, l = int(temp[0]), temp[1].split(".")
            for j in range(len(l)):
                sub = '.'.join(l[j:])
                d[sub] = d.get(sub, 0) + k
        return ["{} {}".format(d[i], i) for i in d]
