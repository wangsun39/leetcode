

from leetcode.allcode.competition.mypackage import *

class Solution:
    def replaceDigits(self, s: str) -> str:
        res = list(s)
        c2i = {c: i for i, c in enumerate(ascii_lowercase)}
        i2c = {i: c for i, c in enumerate(ascii_lowercase)}
        def shift(c, x):
            return i2c[c2i[c] + x]
        for i in range(1, len(res), 2):
            res[i] = shift(res[i - 1], int(res[i]))
        return ''.join(res)


so = Solution()
print(so.replaceDigits(s = "a1c1e1"))




