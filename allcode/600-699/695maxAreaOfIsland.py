# 给你一个大小为 m x n 的二进制矩阵 grid 。
#
# 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。
#
# 岛屿的面积是岛上值为 1 的单元格的数目。
#
# 计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。
#
#
#
# 示例 1：
#
#
# 输入：grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 输出：6
# 解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。
# 示例 2：
#
# 输入：grid = [[0,0,0,0,0,0,0,0]]
# 输出：0
#
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] 为 0 或 1

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

    def max_block(self):
        counter = Counter(self._fa)
        return max(counter.values())

class Solution:
    def maxAreaOfIsland1(self, grid):
        self.grid = grid
        self.row, self.column = len(grid), len(grid[0])
        self.checkMatrix = [[0] * (self.column) for _ in range(self.row)]
        maxArea = 0
        for i in range(self.row):
            for j in range(self.column):
                if grid[i][j] == 1 and self.checkMatrix[i][j] == 0:
                    maxArea = max(self.GetAreaOfPoint(i, j, 0), maxArea)
        return maxArea
    def GetAreaOfPoint(self, i, j, Area):
        if i >= self.row or j >= self.column or i < 0 or j < 0 \
            or self.checkMatrix[i][j] == 1 or self.grid[i][j] == 0:
            return Area
        self.checkMatrix[i][j] = 1
        Area += 1
        Area = self.GetAreaOfPoint(i+1, j, Area)
        Area = self.GetAreaOfPoint(i, j+1, Area)
        Area = self.GetAreaOfPoint(i-1, j, Area)
        Area = self.GetAreaOfPoint(i, j-1, Area)
        return Area


    def maxAreaOfIsland(self, grid):
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        r, c = len(grid), len(grid[0])
        fa = {}  # 另一种写法，x不连续
        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]
        def union(x, y):
            fa[find(y)] = find(x)

        for i in range(r):
            for j in range(c):
                if grid[i][j]: fa[i * c + j] = i * c + j
        for i in range(r):
            start = 0 if (i & 1) == 0 else 1
            for j in range(start, c, 2):
                if grid[i][j] == 0: continue
                for di, dj in dir:
                    x, y = i + di, j + dj
                    if 0 <= x < r and 0 <= y < c and grid[x][y] == 1:
                        union(i * c + j, x * c + y)
        if len(fa) == 0: return 0
        for x in fa:
            find(x)
        counter = Counter(fa.values())
        return max(counter.values())



so = Solution()
print(so.maxAreaOfIsland([[0,1],[0,1]]))
print(so.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]))
