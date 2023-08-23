# 给你一个无向图，无向图由整数 n  ，表示图中节点的数目，和 edges 组成，其中 edges[i] = [ui, vi] 表示 ui 和 vi 之间有一条无向边。同时给你一个代表查询的整数数组 queries 。
#
# 第 j 个查询的答案是满足如下条件的点对 (a, b) 的数目：
#
# a < b
# cnt 是与 a 或者 b 相连的边的数目，且 cnt 严格大于 queries[j] 。
# 请你返回一个数组 answers ，其中 answers.length == queries.length 且 answers[j] 是第 j 个查询的答案。
#
# 请注意，图中可能会有 重复边 。
#
#
#
# 示例 1：
#
#
# 输入：n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]
# 输出：[6,5]
# 解释：每个点对中，与至少一个点相连的边的数目如上图所示。
# answers[0] = 6。所有的点对(a, b)中边数和都大于2，故有6个；
# answers[1] = 5。所有的点对(a, b)中除了(3,4)边数等于3，其它点对边数和都大于3，故有5个。
# 示例 2：
#
# 输入：n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], queries = [1,2,3,4,5]
# 输出：[10,10,9,8,6]
#
#
# 提示：
#
# 2 <= n <= 2 * 104
# 1 <= edges.length <= 105
# 1 <= ui, vi <= n
# ui != vi
# 1 <= queries.length <= 20
# 0 <= queries[j] < edges.length
from bisect import bisect_left
from typing import List
from collections import defaultdict, Counter
from math import inf

class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        d = defaultdict(int)
        cnt = Counter()
        for x, y in edges:
            d[x] += 1
            d[y] += 1
            if x < y:
                cnt[(x, y)] += 1
            else:
                cnt[(y, x)] += 1
        deg = sorted(d.values())
        deg = [0] * (n - len(deg)) + deg
        # print(sl)
        ans = [0] * len(queries)
        for i, q in enumerate(queries):
            res = 0
            first, second = 0, n - 1
            while first < second and deg[first] + deg[second] <= q:
                first += 1
            while first < second:
                while second > first and deg[first] + deg[second] > q:
                    second -= 1
                res += (n - second - 1)   # 计算所有可能的点对，可能会多
                first += 1
            while first < n:
                res += (n - first - 1)
                first += 1
            for (x, y), t in cnt.items():  # 减去多加的点对，多加的点对只会出现的在一条边上
                if d[x] + d[y] > q >= d[x] + d[y] - t:
                    res -= 1
            ans[i] = res

        return ans


so = Solution()
print(so.countPairs(n = 5, edges = [[4,5],[1,3],[1,4]], queries = [0,1,0,0,1,1,0,0,0,0,1,0,0,1,0,1,1,2]))
print(so.countPairs(n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]))
print(so.countPairs(n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], queries = [1,2,3,4,5]))




