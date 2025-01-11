

from leetcode.allcode.competition.mypackage import *

class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        l = p.split('*')
        if len(l[0]) == 0:
            return l[1] in s
        if len(l[1]) == 0:
            return l[0] in s
        p1 = s.find(l[0])
        p2 = s.rfind(l[1])
        if p1 == -1 or p2 == -1:
            return False
        if p1 + len(l[0]) <= p2:
            return True
        return False


so = Solution()
print(so.hasMatch(s = "leetcode", p = "ee*e"))




