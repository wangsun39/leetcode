from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains):
        dict_domain = defaultdict(int)
        def seperateCountAndDomain(cpdomain):
            pos = cpdomain.find(' ')
            return int(cpdomain[:pos]), cpdomain[pos+1:]
        for cpdomain in cpdomains:
            count, domain = seperateCountAndDomain(cpdomain)
            print(count, domain)
            pos1 = domain.rfind('.')
            dict_domain[domain[pos1+1:]] += count
            pos2 = domain.rfind('.', 0, pos1-1)
            if -1 == pos2:
                dict_domain[domain] += count
            else:
                dict_domain[domain[pos2+1:]] += count
                dict_domain[domain] += count
        res = []
        for key in dict_domain:
            res.append(str(dict_domain[key]) + ' ' + key)
        return res



so = Solution()
print(so.subdomainVisits(["9001 discuss.leetcode.com"]))
print(so.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))

