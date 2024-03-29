# 给你 n 个城市，编号为从 1 到 n 。同时给你一个大小为 n-1 的数组 edges ，其中 edges[i] = [ui, vi] 表示城市 ui 和 vi 之间有一条双向边。题目保证任意城市之间只有唯一的一条路径。换句话说，所有城市形成了一棵 树 。
#
# 一棵 子树 是城市的一个子集，且子集中任意城市之间可以通过子集中的其他城市和边到达。两个子树被认为不一样的条件是至少有一个城市在其中一棵子树中存在，但在另一棵子树中不存在。
#
# 对于 d 从 1 到 n-1 ，请你找到城市间 最大距离 恰好为 d 的所有子树数目。
#
# 请你返回一个大小为 n-1 的数组，其中第 d 个元素（下标从 1 开始）是城市间 最大距离 恰好等于 d 的子树数目。
#
# 请注意，两个城市间距离定义为它们之间需要经过的边的数目。
#
#
#
# 示例 1：
#
#
#
# 输入：n = 4, edges = [[1,2],[2,3],[2,4]]
# 输出：[3,4,0]
# 解释：
# 子树 {1,2}, {2,3} 和 {2,4} 最大距离都是 1 。
# 子树 {1,2,3}, {1,2,4}, {2,3,4} 和 {1,2,3,4} 最大距离都为 2 。
# 不存在城市间最大距离为 3 的子树。
# 示例 2：
#
# 输入：n = 2, edges = [[1,2]]
# 输出：[1]
# 示例 3：
#
# 输入：n = 3, edges = [[1,2],[2,3]]
# 输出：[2,1]
#
#
# 提示：
#
# 2 <= n <= 15
# edges.length == n-1
# edges[i].length == 2
# 1 <= ui, vi <= n
# 题目保证 (ui, vi) 所表示的边互不相同。



from typing import Optional, List
from collections import deque, defaultdict

# Definition for a binary tree node.


class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for x, y in edges:
            g[x - 1].append(y - 1)
            g[y - 1].append(x - 1)
        ans = [0] * (n - 1)

        # 用 mask 表示一个顶点的子集，也就是一个子图
        def conn(mask):  # 判断一个子图是否是连通的
            # start = mask & (-mask)   # lowbit
            for start in range(n):
                if (1 << start) & mask:
                    break
            res = (1 << start)

            def dfs(x, fa):
                nonlocal res
                for y in g[x]:
                    b = (1 << y)
                    if y != fa and b & mask:
                        res |= (1 << y)
                        dfs(y, x)
            dfs(start, -1)
            return res == mask

        def diam(mask):  # 计算子图 mask 的直径
            # root = i & (-i)  # lowbit
            for root in range(n):
                if (1 << root) & mask:
                    break
            res = 0
            def dfs(x, fa):
                nonlocal res
                length = []
                for y in g[x]:
                    b = (1 << y)
                    if y != fa and b & mask:
                        length.append(dfs(y, x))
                length.sort(reverse=True)
                if len(length) > 1:
                    res = max(res, length[0] + length[1] + 2)
                    return length[0] + 1
                elif len(length) == 1:
                    res = max(res, length[0] + 1)
                    return length[0] + 1
                else:
                    return 0
            dfs(root, -1)
            return res

        for i in range(1, 2 ** n):
            if not conn(i): continue

            d = diam(i)
            # print(i, d)
            if d > 0:
                ans[d - 1] += 1

        return ans


so = Solution()

print(so.countSubgraphsForEachDiameter(n = 4, edges = [[1,2],[2,3],[2,4]]))  # 3,4,0
print(so.countSubgraphsForEachDiameter(n = 2, edges = [[1,2]]))  # 1
print(so.countSubgraphsForEachDiameter(n = 3, edges = [[1,2],[2,3]]))  # 2,1




