# 给你一个 n 个节点的无向无根图，节点编号为 0 到 n - 1 。给你一个整数 n 和一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间有一条边。
#
# 每个节点都有一个价值。给你一个整数数组 price ，其中 price[i] 是第 i 个节点的价值。
#
# 一条路径的 价值和 是这条路径上所有节点的价值之和。
#
# 你可以选择树中任意一个节点作为根节点 root 。选择 root 为根的 开销 是以 root 为起点的所有路径中，价值和 最大的一条路径与最小的一条路径的差值。
#
# 请你返回所有节点作为根节点的选择中，最大 的 开销 为多少。
#
#
#
# 示例 1：
#
#
#
# 输入：n = 6, edges = [[0,1],[1,2],[1,3],[3,4],[3,5]], price = [9,8,7,6,10,5]
# 输出：24
# 解释：上图展示了以节点 2 为根的树。左图（红色的节点）是最大价值和路径，右图（蓝色的节点）是最小价值和路径。
# - 第一条路径节点为 [2,1,3,4]：价值为 [7,8,6,10] ，价值和为 31 。
# - 第二条路径节点为 [2] ，价值为 [7] 。
# 最大路径和与最小路径和的差值为 24 。24 是所有方案中的最大开销。
# 示例 2：
#
#
#
# 输入：n = 3, edges = [[0,1],[1,2]], price = [1,1,1]
# 输出：2
# 解释：上图展示了以节点 0 为根的树。左图（红色的节点）是最大价值和路径，右图（蓝色的节点）是最小价值和路径。
# - 第一条路径包含节点 [0,1,2]：价值为 [1,1,1] ，价值和为 3 。
# - 第二条路径节点为 [0] ，价值为 [1] 。
# 最大路径和与最小路径和的差值为 2 。2 是所有方案中的最大开销。
#
#
# 提示：
#
# 1 <= n <= 105
# edges.length == n - 1
# 0 <= ai, bi <= n - 1
# edges 表示一棵符合题面要求的树。
# price.length == n
# 1 <= price[i] <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        graph = defaultdict(set)
        for x, y in edges:
            graph[x].add(y)
            graph[y].add(x)
        ans = 0
        def dfs1(x, fa):  # 如果计算的是一条完整的链，可以用这个方法
            nonlocal ans
            h1 = h2 = 0  # 分别表示 x 的价值最大的两个链 (从 x 到叶子)
            for y in graph[x]:
                if y == fa: continue
                sr, sh = dfs(y, x)
                [h1, h2, sh] = sorted([h1, h2, sh], reverse=True)
            r = price[x] + h1 + h2  # 分别表示 x 的子树上最长价值路径
            ans = max(ans, r)
            return r, price[x] + h1
        def dfs(x, fa):
            nonlocal ans
            s1, s2 = price[x], 0  # 分别表示包含端点的最大价值链和不包含端点的最大价值链
            for y in graph[x]:
                if y == fa: continue
                ss1, ss2 = dfs(y, x)
                ans = max(ans, s1 + ss2, s2 + ss1)
                s1 = max(s1, ss1 + price[x])
                s2 = max(s2, ss2 + price[x])
            return s1, s2
        dfs(0, -1)
        return ans


so = Solution()
print(so.maxOutput(n = 6, edges = [[0,1],[1,2],[1,3],[3,4],[3,5]], price = [9,8,7,6,10,5]))
print(so.maxOutput(n = 3, edges = [[0,1],[1,2]], price = [1,1,1]))




