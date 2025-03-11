# 在本问题中，有根树指满足以下条件的有向图。该树只有一个根节点，所有其他节点都是该根节点的后继。每一个节点只有一个父节点，除了根节点没有父节点。
#
# 输入一个有向图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。
#
# 结果图是一个以边组成的二维数组。 每一个边 的元素是一对 [u, v]，用以表示有向图中连接顶点 u 和顶点 v 的边，其中 u 是 v 的一个父节点。
#
# 返回一条能删除的边，使得剩下的图是有N个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。
#
# 示例1:
#
# 输入: [[1,2], [1,3], [2,3]]
# 输出: [2,3]
# 解释: 给定的有向图如下:
#   1
#  / \
# v   v
# 2-->3
# 示例 2:
#
# 输入: [[1,2], [2,3], [3,4], [4,1], [1,5]]
# 输出: [4,1]
# 解释: 给定的有向图如下:
# 5 <- 1 -> 2
#      ^    |
#      |    v
#      4 <- 3
# 注意:
#
# 二维数组大小的在3到1000范围内。
# 二维数组中的每个整数在1到N之间，其中 N 是二维数组的大小。

from leetcode.allcode.competition.mypackage import *

class UnionFind:
    def __init__(self, n):
        self.ids = []
        for i in range(n+1):
            self.ids.append(i)
    def union(self, u, v):
        u_id = self.find(u)
        # v_id = self.find(v)
        # if v == u_id:
        #     return False
        self.ids[v] = u_id
        # for i in range(len(self.ids)):
        #     if self.ids[i] == v:
        #         self.ids[i] = u_id
    def find(self, p):
        if p == self.ids[p]:
            return p
        self.ids[p] = self.find(self.ids[p])
        return self.ids[p]

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        uf = UnionFind(len(edges))
        v1 = None
        for [u, v] in edges:
            if v == parent[v]:
                parent[v] = u
                if v == uf.find(u):
                    v4, v5 = u, v  # 此时 [v4, v5] 在一各有向圈内
                else:
                    uf.union(u, v)
            else:
                v1, v2, v3 = parent[v], u, v # v3 的入度为 2 （仅有一个这种点）
                if uf.find(u) == uf.find(v):  # 存在两条从u到v的有向边，此时v入度为2，删除任意一条入度边都可以
                    return [u, v]
                # uf.union(u, v)
        print(uf.ids)
        if v1 is None:   # 此时没有入度为2的节点，那么肯定有有向圈，删除有向圈上任意一条边都可以
            return [v4, v5]
        else:
            if uf.find(v3) == uf.find(v2):  # 存在两条从v2到v3的有向边，此时v2入度为2，删除任意一条入度边都可以
                return [v2, v3]
        if v5 == uf.find(v1):
            return [v1, v3]
        return [v2, v3]


so = Solution()

print(so.findRedundantDirectedConnection([[1,4], [2,1], [4,2], [3,1], [5,3]]))   # [2, 1]
print(so.findRedundantDirectedConnection([[5,2],[5,1],[3,1],[3,4],[3,5]]))    # [3, 1]
print(so.findRedundantDirectedConnection([[1,2], [1,3], [2,3]]))    # [2, 3]
print(so.findRedundantDirectedConnection([[2,1],[3,1],[4,2],[1,4]]))   # [2, 1]
print(so.findRedundantDirectedConnection([[1,4], [2,1], [4,2], [3,1], [5,3]]))   # [2, 1]
print(so.findRedundantDirectedConnection([[4,2],[1,5],[5,2],[5,3],[2,4]]))
print(so.findRedundantDirectedConnection([[1,2], [2,3], [3,4], [4,1], [1,5]]))
