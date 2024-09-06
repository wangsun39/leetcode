

from leetcode.allcode.competition.mypackage import *

class Solution:
    def stringHash(self, s: str, k: int) -> str:
        c2i = {c: i for i, c in enumerate(ascii_lowercase)}
        i2c = {i: c for i, c in enumerate(ascii_lowercase)}
        n = len(s)
        ans = []
        def trans(ss):
            v = sum(c2i[x] for x in ss) % 26
            return i2c[v]
        for i in range(n // k):
            ans.append(trans(s[i * k: (i + 1) * k]))
        return ''.join(ans)


so = Solution()
print(so.stringHash(s = "abcd", k = 2))
print(so.stringHash(s = "mxz", k = 3))




