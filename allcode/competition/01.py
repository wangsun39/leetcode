

from leetcode.allcode.competition.mypackage import *

class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        n = len(s)
        ss = set()
        for i in range(n - 1):
            t = s[i: i + 2]
            ss.add(t)
            if t[::-1] in s:
                return True
        return False


so = Solution()
print(so.isSubstringPresent("leetcode"))
print(so.isSubstringPresent("abcba"))
print(so.isSubstringPresent("abcd"))




