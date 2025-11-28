# 用以太网线缆将 n 台计算机连接成一个网络，计算机的编号从 0 到 n-1。线缆用 connections 表示，其中 connections[i] = [a, b] 连接了计算机 a 和 b。
#
# 网络中的任何一台计算机都可以通过网络直接或者间接访问同一个网络中其他任意一台计算机。
#
# 给你这个计算机网络的初始布线 connections，你可以拔开任意两台直连计算机之间的线缆，并用它连接一对未直连的计算机。请你计算并返回使所有计算机都连通所需的最少操作次数。如果不可能，则返回 -1 。
#
#
#
# 示例 1：
#
#
#
# 输入：n = 4, connections = [[0,1],[0,2],[1,2]]
# 输出：1
# 解释：拔下计算机 1 和 2 之间的线缆，并将它插到计算机 1 和 3 上。
# 示例 2：
#
#
#
# 输入：n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
# 输出：2
# 示例 3：
#
# 输入：n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
# 输出：-1
# 解释：线缆数量不足。
# 示例 4：
#
# 输入：n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]
# 输出：0
#
#
# 提示：
#
# 1 <= n <= 10^5
# 1 <= connections.length <= min(n*(n-1)/2, 10^5)
# connections[i].length == 2
# 0 <= connections[i][0], connections[i][1] < n
# connections[i][0] != connections[i][1]
# 没有重复的连接。
# 两台计算机不会通过多条线缆连接。

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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        m = len(connections)
        if m < n - 1: return -1
        uf = UnionFind(n)
        for x, y in connections:
            uf.merge(x, y)

        return uf.cc - 1


so = Solution()
print(so.makeConnected(n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]))


