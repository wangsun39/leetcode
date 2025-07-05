# 初始化：将图中的所有边按照权值从小到大排序。
# 构建最小生成树：
# 从权值最小的边开始，依次选择边。
# 每次选择一条边时，判断该边的两个顶点是否已经在同一个连通分量中。
# 如果不在同一个连通分量中，则将这条边加入到最小生成树中，同时将这两个顶点所在的连通分量合并。
# 如果已经在同一个连通分量中，则跳过这条边，避免形成环。
# 重复上述过程，直到最小生成树包含所有顶点，且边数为顶点数减1。


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


def kruskal(n, edges):
    ans = 0
    edges.sort(key=lambda x:x[2])
    uf = UnionFind(n)
    for x, y, w in edges:
        if uf.merge(x, y):
            ans += w
    return ans if (uf.cc == 1) else inf
