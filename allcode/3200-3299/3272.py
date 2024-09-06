import math

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        vis = set()
        half = (n + 1) // 2
        orders = [math.factorial(i) for i in range(n + 1)]
        def trans(x):
            ss = str(x)
            ss = '0' * (n - len(ss)) + ss
            res = [0] * 10
            counter = Counter(ss)
            for k, v in counter.items():
                res[int(k)] = v
            return tuple(res)
        for x in range(1, half + 1):
            v1 = str(x) + str(x)[::-1]  # 偶数长度
            v2 = int(v1)
            if len(v1) <= n and v2 % k == 0:
                tu = trans(x)
                vis.add(tu)
            v1 = str(x)[:-1] + str(x)[::-1]  # 奇数长度
            v2 = int(v1)
            if v2 % k == 0:
                tu = trans(x)
                vis.add(tu)

        def calc(tu):
            n_zero = tu[0]
            total = orders[n - 1] * (n - n_zero)
            res = total
            for i in range(n):
                res //= tu[i]
            return res

        ans = 0
        for tu in vis:
            ans += calc(tu)
        return ans

so = Solution()
print(so.countGoodIntegers(n = 3, k = 5))
print(so.countGoodIntegers(n = 1, k = 4))




