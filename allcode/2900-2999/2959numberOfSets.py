# 一个公司在全国有 n 个分部，它们之间有的有道路连接。一开始，所有分部通过这些道路两两之间互相可以到达。
#
# 公司意识到在分部之间旅行花费了太多时间，所以它们决定关闭一些分部（也可能不关闭任何分部），同时保证剩下的分部之间两两互相可以到达且最远距离不超过 maxDistance 。
#
# 两个分部之间的 距离 是通过道路长度之和的 最小值 。
#
# 给你整数 n ，maxDistance 和下标从 0 开始的二维整数数组 roads ，其中 roads[i] = [ui, vi, wi] 表示一条从 ui 到 vi 长度为 wi的 无向 道路。
#
# 请你返回关闭分部的可行方案数目，满足每个方案里剩余分部之间的最远距离不超过 maxDistance。
#
# 注意，关闭一个分部后，与之相连的所有道路不可通行。
#
# 注意，两个分部之间可能会有多条道路。
#
#
#
# 示例 1：
#
#
#
# 输入：n = 3, maxDistance = 5, roads = [[0,1,2],[1,2,10],[0,2,10]]
# 输出：5
# 解释：可行的关闭分部方案有：
# - 关闭分部集合 [2] ，剩余分部为 [0,1] ，它们之间的距离为 2 。
# - 关闭分部集合 [0,1] ，剩余分部为 [2] 。
# - 关闭分部集合 [1,2] ，剩余分部为 [0] 。
# - 关闭分部集合 [0,2] ，剩余分部为 [1] 。
# - 关闭分部集合 [0,1,2] ，关闭后没有剩余分部。
# 总共有 5 种可行的关闭方案。
# 示例 2：
#
#
#
# 输入：n = 3, maxDistance = 5, roads = [[0,1,20],[0,1,10],[1,2,2],[0,2,2]]
# 输出：7
# 解释：可行的关闭分部方案有：
# - 关闭分部集合 [] ，剩余分部为 [0,1,2] ，它们之间的最远距离为 4 。
# - 关闭分部集合 [0] ，剩余分部为 [1,2] ，它们之间的距离为 2 。
# - 关闭分部集合 [1] ，剩余分部为 [0,2] ，它们之间的距离为 2 。
# - 关闭分部集合 [0,1] ，剩余分部为 [2] 。
# - 关闭分部集合 [1,2] ，剩余分部为 [0] 。
# - 关闭分部集合 [0,2] ，剩余分部为 [1] 。
# - 关闭分部集合 [0,1,2] ，关闭后没有剩余分部。
# 总共有 7 种可行的关闭方案。
# 示例 3：
#
# 输入：n = 1, maxDistance = 10, roads = []
# 输出：2
# 解释：可行的关闭分部方案有：
# - 关闭分部集合 [] ，剩余分部为 [0] 。
# - 关闭分部集合 [0] ，关闭后没有剩余分部。
# 总共有 2 种可行的关闭方案。
#
#
# 提示：
#
# 1 <= n <= 10
# 1 <= maxDistance <= 105
# 0 <= roads.length <= 1000
# roads[i].length == 3
# 0 <= ui, vi <= n - 1
# ui != vi
# 1 <= wi <= 1000
# 一开始所有分部之间通过道路互相可以到达。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        g = [[inf] * n for _ in range(n)]
        for x, y, wt in roads:
            g[x][y] = g[y][x] = min(wt, g[x][y])

        def floyd(bits):
            @cache
            def dfs(k: int, i: int, j: int) -> int:
                if k < 0:  # 递归边界
                    return g[i][j]
                if (bits >> k) & 1 == 0:
                    return dfs(k - 1, i, j)
                return min(dfs(k - 1, i, j), dfs(k - 1, i, k) + dfs(k - 1, k, j))

            f = [[inf] * n for _ in range(n)]  # f[i][j] 表示 i 到 j 的最小距离
            for i in range(n):
                if (bits >> i) & 1:
                    f[i][i] = 0
                    for j in range(i + 1, n):
                        if (bits >> j) & 1:
                            f[i][j] = f[j][i] = dfs(n - 1, i, j)

            return f

        ans = 0
        for bits in range(1 << n):
            f = floyd(bits)
            fit = True
            for i in range(n):
                if (bits >> i) & 1 == 0: continue
                for j in range(n):
                    if i == j or (bits >> j) & 1 == 0: continue
                    if f[i][j] > maxDistance:
                        fit = False
                        break
                if not fit:
                    break
            if fit:
                ans += 1
        return ans





so = Solution()
print(so.numberOfSets(n = 4, maxDistance = 29, roads = [[2,1,3],[3,0,19],[2,0,17],[3,1,4],[2,0,16]]))
print(so.numberOfSets(n = 3, maxDistance = 12, roads = [[1,0,11],[1,0,16],[0,2,13]]))
print(so.numberOfSets(n = 3, maxDistance = 5, roads = [[0,1,2],[1,2,10],[0,2,10]]))
print(so.numberOfSets(n = 3, maxDistance = 5, roads = [[0,1,20],[0,1,10],[1,2,2],[0,2,2]]))
print(so.numberOfSets(n = 1, maxDistance = 10, roads = []))




