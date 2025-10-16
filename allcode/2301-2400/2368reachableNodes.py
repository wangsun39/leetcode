# 现有一棵由 n 个节点组成的无向树，节点编号从 0 到 n - 1 ，共有 n - 1 条边。
#
# 给你一个二维整数数组 edges ，长度为 n - 1 ，其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条边。另给你一个整数数组 restricted 表示 受限 节点。
#
# 在不访问受限节点的前提下，返回你可以从节点 0 到达的 最多 节点数目。
#
# 注意，节点 0 不 会标记为受限节点。
#
# 
#
# 示例 1：
#
#
# 输入：n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5]
# 输出：4
# 解释：上图所示正是这棵树。
# 在不访问受限节点的前提下，只有节点 [0,1,2,3] 可以从节点 0 到达。
# 示例 2：
#
#
# 输入：n = 7, edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], restricted = [4,2,1]
# 输出：3
# 解释：上图所示正是这棵树。
# 在不访问受限节点的前提下，只有节点 [0,5,6] 可以从节点 0 到达。
# 
#
# 提示：
#
# 2 <= n <= 105
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# edges 表示一棵有效的树
# 1 <= restricted.length < n
# 1 <= restricted[i] < n
# restricted 中的所有值 互不相同

from leetcode.allcode.competition.mypackage import *

class Solution:
    def reachableNodes1(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        d = defaultdict(set)
        restricted = set(restricted)
        for e in edges:
            d[e[0]].add(e[1])
            d[e[1]].add(e[0])
        ans = set()
        queue = [0]
        while len(queue) > 0:
            node = queue.pop(0)
            if node not in ans and node not in restricted:
                for n in d[node]:
                    if n not in ans and node not in restricted:
                        queue.append(n)
                ans.add(node)
        return len(ans)

    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        # 2024/3/2 DFS写法
        g = defaultdict(list)
        restricted = set(restricted)
        for x, y  in edges:
            g[x].append(y)
            g[y].append(x)
        def dfs(x, fa):
            if x in restricted:
                return 0
            res = 1
            for y in g[x]:
                if y != fa:
                    res += dfs(y, x)
            return res
        return dfs(0, -1)


so = Solution()
print(so.reachableNodes(n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5]))
print(so.reachableNodes(n = 7, edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], restricted = [4,2,1]))




