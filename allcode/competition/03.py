

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minAnagramLength(self, s: str) -> int:
        def factors(x):
            res = []
            i = 1
            while i * i <= x:
                if x % i == 0:
                    res.append(i)
                    if i * i != x:
                        res.append(x // i)
                i += 1
            return res
        n = len(s)
        fs = factors(n)
        fs.sort()
        counter = Counter(s)
        m = len(counter.keys())
        if m == 1:
            return 1
        for lf in fs:  # lf 为每个可能的长度
            ct0 = Counter(s[:lf])
            if len(ct0) < m: continue
            flg = True
            for i in range(lf, n, lf):
                ct = Counter(s[i: i + lf])
                if len(ct) < m:
                    flg = False
                    break
                if ct != ct0:
                    flg = False
                    break
            if flg:
                return lf
        return n




so = Solution()
print(so.minAnagramLength("abba"))
print(so.minAnagramLength("cdef"))




