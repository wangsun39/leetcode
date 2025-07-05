# 给你一个 n 个点的带权无向连通图，节点编号为 0 到 n-1 ，同时还有一个数组 edges ，其中 edges[i] = [fromi, toi, weighti] 表示在 fromi 和 toi 节点之间有一条带权无向边。最小生成树 (MST) 是给定图中边的一个子集，它连接了所有节点且没有环，而且这些边的权值和最小。
#
# 请你找到给定图中最小生成树的所有关键边和伪关键边。如果从图中删去某条边，会导致最小生成树的权值和增加，那么我们就说它是一条关键边。伪关键边则是可能会出现在某些最小生成树中但不会出现在所有最小生成树中的边。
#
# 请注意，你可以分别以任意顺序返回关键边的下标和伪关键边的下标。
#
#
#
# 示例 1：
#
#
#
# 输入：n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
# 输出：[[0,1],[2,3,4,5]]
# 解释：上图描述了给定图。
# 下图是所有的最小生成树。
#
# 注意到第 0 条边和第 1 条边出现在了所有最小生成树中，所以它们是关键边，我们将这两个下标作为输出的第一个列表。
# 边 2，3，4 和 5 是所有 MST 的剩余边，所以它们是伪关键边。我们将它们作为输出的第二个列表。
# 示例 2 ：
#
#
#
# 输入：n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
# 输出：[[],[0,1,2,3]]
# 解释：可以观察到 4 条边都有相同的权值，任选它们中的 3 条可以形成一棵 MST 。所以 4 条边都是伪关键边。
#
#
# 提示：
#
# 2 <= n <= 100
# 1 <= edges.length <= min(200, n * (n - 1) / 2)
# edges[i].length == 3
# 0 <= fromi < toi < n
# 1 <= weighti <= 1000
# 所有 (fromi, toi) 数对都是互不相同的。



from leetcode.allcode.competition.mypackage import *

class UnionFind:
    def __init__(self, n: int):
        # 一开始有 n 个集合 {0}, {1}, ..., {n-1}
        # 集合 i 的代表元是自己
        self._fa = list(range(n))  # 代表元
        self.cc = n  # 连通块个数

    # 返回 x 所在集合的代表元
    # 同时做路径压缩，也就是把 x 所在集合中的所有元素的 fa 都改成代表元
    def find(self, x: int) -> int:
        # 如果 fa[x] == x，则表示 x 是代表元
        if self._fa[x] != x:
            self._fa[x] = self.find(self._fa[x])  # fa 改成代表元
        return self._fa[x]

    # 把 from 所在集合合并到 to 所在集合中
    # 返回是否合并成功
    def merge(self, from_: int, to: int) -> bool:
        x, y = self.find(from_), self.find(to)
        if x == y:  # from 和 to 在同一个集合，不做合并
            return False
        self._fa[x] = y  # 合并集合。修改后就可以认为 from 和 to 在同一个集合了
        self.cc -= 1  # 成功合并，连通块个数减一
        return True



class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        def kruskal(n, edges):
            ans = 0
            # edges.sort(key=lambda x:x[2])  已经在外面排序了
            uf = UnionFind(n)
            for x, y, w in edges:
                if uf.merge(x, y):
                    ans += w
            return ans if (uf.cc == 1) else inf

        def kruskal2(n, edges, test_edge):
            # test_edge 必须在最小生成树中
            # edges.sort(key=lambda x:x[2])  已经在外面排序了
            uf = UnionFind(n)
            uf.merge(test_edge[0], test_edge[1])
            ans = test_edge[2]
            for x, y, w in edges:
                if uf.merge(x, y):
                    ans += w
            return ans if (uf.cc == 1) else inf
        idx_map = {tuple(e): i for i, e in enumerate(edges)}
        edges.sort(key=lambda x: x[2])
        mn = kruskal(n, edges)
        l1, l2 = [], []  # 关键路径和伪关键路径

        for i, edge in enumerate(edges):
            if kruskal2(n, edges, edge) == mn:
                if kruskal(n, edges[:i] + edges[i + 1:]) > mn:
                    l1.append(idx_map[tuple(edge)])
                else:
                    l2.append(idx_map[tuple(edge)])
        return [l1, l2]



so = Solution()
print(so.findCriticalAndPseudoCriticalEdges(n = 6, edges = [[2,3,4],[0,1,1],[1,2,1],[0,2,1],[3,4,2],[3,5,2],[4,5,2]]))
print(so.findCriticalAndPseudoCriticalEdges(n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]))




