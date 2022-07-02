# 给你两个整数 m 和 n 表示一个下标从 0 开始的 m x n 网格图。同时给你两个二维整数数组 guards 和 walls ，其中 guards[i] = [rowi, coli] 且 walls[j] = [rowj, colj] ，分别表示第 i 个警卫和第 j 座墙所在的位置。
#
# 一个警卫能看到 4 个坐标轴方向（即东、南、西、北）的 所有 格子，除非他们被一座墙或者另外一个警卫 挡住 了视线。如果一个格子能被 至少 一个警卫看到，那么我们说这个格子被 保卫 了。
#
# 请你返回空格子中，有多少个格子是 没被保卫 的。
#
#  
#
# 示例 1：
#
#
#
# 输入：m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
# 输出：7
# 解释：上图中，被保卫和没有被保卫的格子分别用红色和绿色表示。
# 总共有 7 个没有被保卫的格子，所以我们返回 7 。
# 示例 2：
#
#
#
# 输入：m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
# 输出：4
# 解释：上图中，没有被保卫的格子用绿色表示。
# 总共有 4 个没有被保卫的格子，所以我们返回 4 。
#  
#
# 提示：
#
# 1 <= m, n <= 105
# 2 <= m * n <= 105
# 1 <= guards.length, walls.length <= 5 * 104
# 2 <= guards.length + walls.length <= m * n
# guards[i].length == walls[j].length == 2
# 0 <= rowi, rowj < m
# 0 <= coli, colj < n
# guards 和 walls 中所有位置 互不相同 。


from typing import List
from collections import deque
# Definition for a binary tree node.
from collections import Counter
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        Map = [['U' for _ in range(n)] for _ in range(m)]
        for x, y in guards:
            Map[x][y] = 'G'
        for x, y in walls:
            Map[x][y] = 'W'
        def handleRow(i):
            nonlocal Map
            pos, state = 0, 'U'
            for j in range(n):
                if Map[i][j] == 'G':
                    state = 'S'
                    for k in range(pos, j):
                        Map[i][k] = 'S'
                    pos = j + 1
                elif Map[i][j] == 'W':
                    state = 'U'
                    pos = j + 1
                else:
                    if Map[i][j] != 'S' and state == 'S':
                        Map[i][j] = 'S'
                        pos += 1
            return
        def handleCol(j):
            nonlocal Map
            pos, state = 0, 'U'
            for i in range(m):
                if Map[i][j] == 'G':
                    state = 'S'
                    for k in range(pos, i):
                        Map[k][j] = 'S'
                    pos = i + 1
                elif Map[i][j] == 'W':
                    state = 'U'
                    pos = i + 1
                else:
                    if Map[i][j] != 'S' and state == 'S':
                        Map[i][j] = 'S'
                        pos += 1
            return
        for i in range(m):
            handleRow(i)
        for j in range(n):
            handleCol(j)
        print(Map)
        ans = 0
        for i in range(m):
            for j in range(n):
                if Map[i][j] == 'U':
                    ans += 1
        return ans

so = Solution()
print(so.countUnguarded(m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]))
print(so.countUnguarded(m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]))

