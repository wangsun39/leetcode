

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        if c - e == d - f:
            if a - c != b - d or not (c < a < e or e < a < c):  # 车不在对角线或不在对角线的中间
                return 1
            return 2
        if c - e == -(d - f):
            if a - c != -(b - d) or not (c < a < e or e < a < c):  # 车不在对角线或不在对角线的中间
                return 1
            return 2
        if a == e:
            if c != e or not (b < d < f or f < d < b):
                return 1
            return 2
        if b == f:
            if d != f or not (a < c < e or e < c < a):
                return 1
            return 2
        return 2


so = Solution()
print(so.minMovesToCaptureTheQueen(a = 4, b = 3, c = 3, d = 4, e = 2, f = 5))
print(so.minMovesToCaptureTheQueen(a = 1, b = 1, c = 8, d = 8, e = 2, f = 3))
print(so.minMovesToCaptureTheQueen(a = 5, b = 3, c = 3, d = 4, e = 5, f = 2))




