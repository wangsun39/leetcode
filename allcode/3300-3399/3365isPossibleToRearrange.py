

from leetcode.allcode.competition.mypackage import *

class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n = len(s)
        s1 = []
        k = n // k
        for i in range(0, n, k):
            s1.append(s[i: i + k])
        s1.sort()
        t1 = []
        for i in range(0, n, k):
            t1.append(t[i: i + k])
        t1.sort()
        return s1 == t1



so = Solution()
print(so.isPossibleToRearrange(s = "abcd", t = "cdab", k = 2))
print(so.isPossibleToRearrange(s = "aabbcc", t = "bbaacc", k = 3))
print(so.isPossibleToRearrange(s = "abcd", t = "cdab", k = 2))




