

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        n = len(ranges)
        fa = list(range(n))
        # fa = {x: x for x in nums}  # 另一种写法，x不连续
        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]
        def union(x, y):
            fa[find(y)] = find(x)

        ranges.sort()
        max_right = ranges[0][1]
        for i in range(n - 1):
            if max_right < ranges[i + 1][0]:  # 无交集
                max_right = ranges[i + 1][1]
                continue
            union(i, i + 1)
            max_right = max(max_right, ranges[i + 1][1])
        for i in range(n):
            find(i)
        m = len(set(fa))
        return pow(2, m, MOD)



so = Solution()
print(so.countWays(ranges = [[1,3],[10,20],[2,5],[4,8]]))
print(so.countWays(ranges = [[34,56],[28,29],[12,16],[11,48],[28,54],[22,55],[28,41],[41,44]]))
print(so.countWays(ranges = [[6,10],[5,15]]))




