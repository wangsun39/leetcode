# 在一个 106 x 106 的网格中，每个网格上方格的坐标为 (x, y) 。
#
# 现在从源方格 source = [sx, sy] 开始出发，意图赶往目标方格 target = [tx, ty] 。数组 blocked 是封锁的方格列表，其中每个 blocked[i] = [xi, yi] 表示坐标为 (xi, yi) 的方格是禁止通行的。
#
# 每次移动，都可以走到网格中在四个方向上相邻的方格，只要该方格 不 在给出的封锁列表 blocked 上。同时，不允许走出网格。
#
# 只有在可以通过一系列的移动从源方格 source 到达目标方格 target 时才返回 true。否则，返回 false。
#
#
#
# 示例 1：
#
# 输入：blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
# 输出：false
# 解释：
# 从源方格无法到达目标方格，因为我们无法在网格中移动。
# 无法向北或者向东移动是因为方格禁止通行。
# 无法向南或者向西移动是因为不能走出网格。
# 示例 2：
#
# 输入：blocked = [], source = [0,0], target = [999999,999999]
# 输出：true
# 解释：
# 因为没有方格被封锁，所以一定可以到达目标方格。
#
#
# 提示：
#
# 0 <= blocked.length <= 200
# blocked[i].length == 2
# 0 <= xi, yi < 106
# source.length == target.length == 2
# 0 <= sx, sy, tx, ty < 106
# source != target
# 题目数据保证 source 和 target 不在封锁列表内

from leetcode.allcode.competition.mypackage import *

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        row, col = set(), set()
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        # 根据blocked + [source] + [target] 中所有点，及其左右上下的行列，简化网格
        # 其他的点实际是没有用的，在使用并查集
        for x, y in blocked + [source] + [target]:
            row.add(x)
            if x > 0:
                row.add(x - 1)
            if x < 10 ** 6 - 1:
                row.add(x + 1)
            col.add(y)
            if y > 0:
                col.add(y - 1)
            if y < 10 ** 6 - 1:
                col.add(y + 1)
        blocked = set((x, y) for x, y in blocked)
        row, col = list(row), list(col)
        row.sort()
        col.sort()
        r, c = len(row), len(col)
        grid = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if (row[i], col[j]) in blocked:
                    grid[i][j] = 1
                if [row[i], col[j]] == source:
                    src = [i, j]
                if [row[i], col[j]] == target:
                    dst = [i, j]

        n = r * c
        fa = list(range(n))
        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]
        def union(x, y):
            fa[find(y)] = find(x)

        for i in range(r):
            for j in range(c):
                for x0, y0 in dir:
                    u, v = i + x0, j + y0
                    if 0 <= u < r and 0 <= v < c and grid[i][j] == grid[u][v] == 0:
                        union(i * c + j, u * c + v)
        return find(src[0] * c + src[1]) == find(dst[0] * c + dst[1])


so = Solution()
print(so.isEscapePossible(blocked = [[0,4],[2,4],[3,1],[3,3],[4,0],[4,2]], source = [2,2], target = [7,3]))
print(so.isEscapePossible(blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]))
print(so.isEscapePossible(blocked = [], source = [0,0], target = [999999,999999]))




