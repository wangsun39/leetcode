# 存在一个由 n 个节点组成的无向连通图，图中的节点按从 0 到 n - 1 编号。
#
# 给你一个数组 graph 表示这个图。其中，graph[i] 是一个列表，由所有与节点 i 直接相连的节点组成。
#
# 返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。
#
#
#
# 示例 1：
#
#
# 输入：graph = [[1,2,3],[0],[0],[0]]
# 输出：4
# 解释：一种可能的路径为 [1,0,2,0,3]
# 示例 2：
#
#
#
# 输入：graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
# 输出：4
# 解释：一种可能的路径为 [0,1,4,2,3]
#
#
# 提示：
#
# n == graph.length
# 1 <= n <= 12
# 0 <= graph[i].length < n
# graph[i] 不包含 i
# 如果 graph[a] 包含 b ，那么 graph[b] 也包含 a
# 输入的图总是连通图

from leetcode.allcode.competition.mypackage import *

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)

        @cache
        def dfs(x, val, mask, dep):
            if mask == (1 << n) - 1: return val
            if dep >= n * 2 + 1: return inf
            res = inf
            for y in graph[x]:
                res = min(res, dfs(y, val + 1, mask | (1 << y), dep + 1))
            return res

        return min(dfs(i, 0, 1 << i, 0) for i in range(n))


so = Solution()
print(so.shortestPathLength(graph = [[2],[3],[3,4,5,6,7,8,9,10,11,0],[2,4,5,6,7,8,9,10,11,1],[2,3,5,6,7,8,9,10,11],[2,3,4,6,7,8,9,10,11],[2,3,4,5,7,8,9,10,11],[2,3,4,5,6,8,9,10,11],[2,3,4,5,6,7,9,10,11],[2,3,4,5,6,7,8,10,11],[2,3,4,5,6,7,8,9,11],[2,3,4,5,6,7,8,9,10]]))
print(so.shortestPathLength(graph = [[1,2,3],[0],[0],[0]]))
print(so.shortestPathLength(graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]))




