# 你有一块棋盘，棋盘上有一些格子已经坏掉了。你还有无穷块大小为1 * 2的多米诺骨牌，你想把这些骨牌不重叠地覆盖在完好的格子上，请找出你最多能在棋盘上放多少块骨牌？这些骨牌可以横着或者竖着放。
#
#
#
# 输入：n, m代表棋盘的大小；broken是一个b * 2的二维数组，其中每个元素代表棋盘上每一个坏掉的格子的位置。
#
# 输出：一个整数，代表最多能在棋盘上放的骨牌数。
#
#
#
# 示例 1：
#
# 输入：n = 2, m = 3, broken = [[1, 0], [1, 1]]
# 输出：2
# 解释：我们最多可以放两块骨牌：[[0, 0], [0, 1]]以及[[0, 2], [1, 2]]。（见下图）
#
#
#
#
# 示例 2：
#
# 输入：n = 3, m = 3, broken = []
# 输出：4
# 解释：下图是其中一种可行的摆放方式
#
#
#
#
# 限制：
#
# 1 <= n <= 8
# 1 <= m <= 8
# 0 <= b <= n * m

from leetcode.allcode.competition.mypackage import *

class Solution:
    def domino(self, n: int, m: int, broken: List[List[int]]) -> int:
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        match = {}  # 记录匹配的点对
        br = set(tuple(x) for x in broken)
        ans = 0

        def dfs(node):
            # 从点node出发找一条增广路径
            x, y = node
            vis.add(node)
            for dx, dy in dir:
                u, v = x + dx, y + dy  # (u, v) 是node的匹配点
                if 0 <= u < n and 0 <= v < m and (u, v) not in br:
                    if (u, v) in match and match[(u, v)] in vis: continue
                    if (u, v) not in match or dfs(match[(u, v)]):
                        # match[(u, v)] 与 node在二分图的同侧
                        match[node] = (u, v)
                        match[(u, v)] = node
                        return True
            return False

        for i in range(n):
            for j in range(m):
                if (i + j) & 1 and (i, j) not in br:
                    vis = set()  # vis 中只存 (i,j)侧的点
                    if dfs((i, j)):
                        ans += 1
        return ans




so = Solution()
print(so.domino(n = 3, m = 2, broken = [[1, 0], [2, 0]]))
print(so.domino(n = 3, m = 3, broken = []))
print(so.domino(n = 2, m = 3, broken = [[1, 0], [1, 1]]))
print(so.domino(n = 8, m = 8, broken = []))




