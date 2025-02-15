# 给定一个无向、连通的树。树中有 n 个标记为 0...n-1 的节点以及 n-1 条边 。
#
# 给定整数 n 和数组 edges ， edges[i] = [ai, bi]表示树中的节点 ai 和 bi 之间有一条边。
#
# 返回长度为 n 的数组 answer ，其中 answer[i] 是树中第 i 个节点与所有其他节点之间的距离之和。
#
#
#
# 示例 1:
#
#
#
# 输入: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# 输出: [8,12,6,10,10,10]
# 解释: 树如图所示。
# 我们可以计算出 dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
# 也就是 1 + 1 + 2 + 2 + 2 = 8。 因此，answer[0] = 8，以此类推。
# 示例 2:
#
#
# 输入: n = 1, edges = []
# 输出: [0]
# 示例 3:
#
#
# 输入: n = 2, edges = [[1,0]]
# 输出: [1,1]
#
#
# 提示:
#
# 1 <= n <= 3 * 104
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# 给定的输入保证为有效的树
from leetcode.allcode.competition.mypackage import *
import math
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        son = [0] * n
        def dfs1(node, p):
            res = 0
            for x in g[node]:
                if x == p: continue
                res += (dfs1(x, node) + 1)
            son[node] = res
            return res
        dfs1(0, -1)
        # 将 0 作为根节点，每个节点的i子分支 u 的所有路径和 v 存放在 v_num[i] 中 [u, v]
        v_num = defaultdict(list)
        def dfs(node, p):  # 返回以node为根的子树中，到node的所有路径长度和
            res = 0
            for x in g[node]:
                if x == p: continue
                val = dfs(x, node)
                v_num[node].append([x, val + son[x] + 1])
                res += (val + son[x] + 1)
            return res
        dfs(0, -1)
        # print(son)
        def dfs3(node, p, val):  # 从根节点向下，传入从上方走到node的所有路径和
            v_num[node].append([p, val])
            ss = sum(x for _, x in v_num[node])
            for idx, x in v_num[node]:
                if idx == p: continue
                dfs3(idx, node, ss - x + (n - son[idx] - 1))
        dfs3(0, -1, 0)
        # print(v_num)
        ans = [0] * n
        for i in range(n):
            ss = sum(x for _, x in v_num[i])
            ans[i] = ss

        return ans



so = Solution()
print(so.sumOfDistancesInTree(4, [[1,2],[3,2],[3,0]]))
print(so.sumOfDistancesInTree(n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]))
print(so.sumOfDistancesInTree(n = 1, edges = []))
print(so.sumOfDistancesInTree(n = 2, edges = [[1,0]]))

