# 在一个 n x n 的整数矩阵 grid 中，每一个方格的值 grid[i][j] 表示位置 (i, j) 的平台高度。
#
# 当开始下雨时，在时间为 t 时，水池中的水位为 t 。你可以从一个平台游向四周相邻的任意一个平台，但是前提是此时水位必须同时淹没这两个平台。假定你可以瞬间移动无限距离，也就是默认在方格内部游动是不耗时的。当然，在你游泳的时候你必须待在坐标方格里面。
#
# 你从坐标方格的左上平台 (0，0) 出发。返回 你到达坐标方格的右下平台 (n-1, n-1) 所需的最少时间 。
#
#
#
# 示例 1:
#
#
#
# 输入: grid = [[0,2],[1,3]]
# 输出: 3
# 解释:
# 时间为0时，你位于坐标方格的位置为 (0, 0)。
# 此时你不能游向任意方向，因为四个相邻方向平台的高度都大于当前时间为 0 时的水位。
# 等时间到达 3 时，你才可以游向平台 (1, 1). 因为此时的水位是 3，坐标方格中的平台没有比水位 3 更高的，所以你可以游向坐标方格中的任意位置
# 示例 2:
#
#
#
# 输入: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
# 输出: 16
# 解释: 最终的路线用加粗进行了标记。
# 我们必须等到时间为 16，此时才能保证平台 (0, 0) 和 (4, 4) 是连通的
#
#
# 提示:
#
# n == grid.length
# n == grid[i].length
# 1 <= n <= 50
# 0 <= grid[i][j] < n2
# grid[i][j] 中每个值 均无重复
from collections import deque
from typing import List
from heapq import *

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        hq = [[grid[0][0], 0, 0]]
        vis = [[0] * n for _ in range(n)]
        vis[0][0] = 1
        ans = grid[0][0]
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while len(hq):
            t, i, j = heappop(hq)
            ans = max(ans, t)
            for u, v in dir:
                x, y = i + u, j + v
                if 0 <= x < n and 0 <= y < n and not vis[x][y]:
                    if x == n - 1 and y == n - 1:
                        return max(grid[x][y], ans)
                    vis[x][y] = 1
                    heappush(hq, [grid[x][y], x, y])
        return ans

    def swimInWater2(self, grid: List[List[int]]) -> int:
        # 2023/6/11 BFS
        r, c = len(grid), len(grid[0])
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        vis = [[0] * c for _ in range(c)]

        dq = deque()
        dq2 = deque()
        t = grid[0][0]
        dq.append([0, 0])
        vis[0][0] = 1
        while dq:
            while dq:
                x, y = dq.popleft()
                if grid[x][y] > t:
                    dq2.append([x, y])
                    continue
                if x == r - 1 and y == c - 1:
                    return t
                for dx, dy in dir:
                    u, v = x + dx, y + dy
                    if 0 <= u < r and 0 <= v < c and 0 == vis[u][v]:
                        if grid[u][v] <= t:
                            if u == r - 1 and v == c - 1:
                                return t
                            dq.append([u, v])
                        else:
                            dq2.append([u, v])
                        vis[u][v] = 1
            dq, dq2 = dq2, deque()
            t += 1

    def swimInWater(self, grid: List[List[int]]) -> int:
        # 2023/6/11 二分
        n = len(grid)
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def check(val):
            if grid[0][0] > val:
                return False
            vis = [[0] * n for _ in range(n)]
            vis[0][0] = 1
            dq = deque([[0, 0]])
            while dq:
                x, y = dq.popleft()
                if x == n - 1 == y:
                    return True
                for dx, dy in dir:
                    u, v = x + dx, y + dy
                    if 0 <= u < n and 0 <= v < n and 0 == vis[u][v] and grid[u][v] <= val:
                        dq.append([u, v])
                        vis[u][v] = 1
            return False

        lo, hi = -1, n * n
        while lo < hi - 1:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid
        return hi



so = Solution()
print(so.swimInWater(grid = [[0]]))  # 0
print(so.swimInWater(grid = [[3,2],[0,1]]))  # 3
print(so.swimInWater(grid = [[0,2],[1,3]]))  # 3
print(so.swimInWater(grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))  # 16

