# 给你一个无向图，整数 n 表示图中节点的数目，edges 数组表示图中的边，其中 edges[i] = [ui, vi] ，表示 ui 和 vi 之间有一条无向边。
#
# 一个 连通三元组 指的是 三个 节点组成的集合且这三个点之间 两两 有边。
#
# 连通三元组的度数 是所有满足此条件的边的数目：一个顶点在这个三元组内，而另一个顶点不在这个三元组内。
#
# 请你返回所有连通三元组中度数的 最小值 ，如果图中没有连通三元组，那么返回 -1 。
#
#
#
# 示例 1：
#
#
# 输入：n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
# 输出：3
# 解释：只有一个三元组 [1,2,3] 。构成度数的边在上图中已被加粗。
# 示例 2：
#
#
# 输入：n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]
# 输出：0
# 解释：有 3 个三元组：
# 1) [1,4,3]，度数为 0 。
# 2) [2,5,6]，度数为 2 。
# 3) [5,6,7]，度数为 2 。
#
#
# 提示：
#
# 2 <= n <= 400
# edges[i].length == 2
# 1 <= edges.length <= n * (n-1) / 2
# 1 <= ui, vi <= n
# ui != vi
# 图中没有重复的边。
import bisect
from cmath import inf
from leetcode.allcode.competition.mypackage import *


class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        deg = [0] * n
        g = defaultdict(list)
        s = set((x - 1, y - 1) for x, y in edges)
        for x, y in edges:
            x, y = sorted([x, y])
            deg[x - 1] += 1
            deg[y - 1] += 1
            g[x - 1].append(y - 1)
        ans = inf
        for i in range(n):
            li = g[i]
            m = len(g[i])
            for j in range(m):
                nj = li[j]
                for k in range(j + 1, m):
                    nk = li[k]
                    if (nj, nk) in s or (nk, nj) in s:
                        ans = min(ans, deg[i] + deg[nj] + deg[nk] - 6)
        return ans if ans < inf else -1


so = Solution()

print(so.minTrioDegree(n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]))
print(so.minTrioDegree(n = 6, edges = [[6,5],[4,3],[5,1],[1,4],[2,3],[4,5],[2,6],[1,3]]))
print(so.minTrioDegree(n = 17, edges = [[12,10],[12,16],[4,9],[4,6],[14,1],[9,2],[17,6],[17,12],[8,9],[11,14],[13,5],[8,15],[13,11],[15,11],[15,14],[6,8],[12,15],[14,12],[9,1],[9,10],[10,5],[1,11],[2,10],[15,1],[7,9],[14,2],[4,1],[17,7],[3,17],[8,1],[17,13],[10,13],[8,13],[1,7],[2,6],[13,6],[7,2],[1,16],[6,3],[6,9],[16,17],[7,14]]))

print(so.minTrioDegree(n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]))




