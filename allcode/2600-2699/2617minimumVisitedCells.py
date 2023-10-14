# 给你一个下标从 0 开始的 m x n 整数矩阵 grid 。你一开始的位置在 左上角 格子 (0, 0) 。
#
# 当你在格子 (i, j) 的时候，你可以移动到以下格子之一：
#
# 满足 j < k <= grid[i][j] + j 的格子 (i, k) （向右移动），或者
# 满足 i < k <= grid[i][j] + i 的格子 (k, j) （向下移动）。
# 请你返回到达 右下角 格子 (m - 1, n - 1) 需要经过的最少移动格子数，如果无法到达右下角格子，请你返回 -1 。
#
#
#
# 示例 1：
#
#
#
# 输入：grid = [[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]
# 输出：4
# 解释：上图展示了到达右下角格子经过的 4 个格子。
# 示例 2：
#
#
#
# 输入：grid = [[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]]
# 输出：3
# 解释：上图展示了到达右下角格子经过的 3 个格子。
# 示例 3：
#
#
#
# 输入：grid = [[2,1,0],[1,0,0]]
# 输出：-1
# 解释：无法到达右下角格子。
#
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 105
# 1 <= m * n <= 105
# 0 <= grid[i][j] < m * n
# grid[m - 1][n - 1] == 0

from leetcode.allcode.competition.mypackage import *


class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        if r == 1 and c == 1: return 1
        q1 = deque()
        q1.append((0, 0))
        vis_r = [0] * c  # 每行最右端访问到哪个节点
        vis_c = [0] * r  # 每列最下端访问到哪个节点
        vis = {(0, 0)}
        ans = 1
        while len(q1):
            q2 = deque()
            while len(q1):
                x, y = q1.popleft()
                if x == r - 1 and y == c - 1:
                    return ans
                if grid[0][0] == 0: continue

                if vis_c[x] < c - 1:
                    right = min((max(vis_c[x], grid[x][y] + y), c - 1))
                    if x == r - 1 and right == c - 1:
                        return ans + 1
                    for i in range(max(y + 1, vis_c[x] + 1), right + 1):
                        # 这个地方 max(y + 1, vis_c[x] + 1) 很关键，
                        # 比赛就是直接从 vis_c[x] + 1 开始，实际是错误的，
                        # y 有可能 比 vis_c[x] 大，此时 vis_c[x] 前面的节点不一定都访问到
                        # 但这并不影响结构，假如后面访问到 vis_c[x] 前面节点的可以继续处理，
                        if (x, i) in vis: continue  # 用 vis，避免重复放入队列，不用也是可以的
                        q2.append((x, i))
                        vis.add((x, i))
                    vis_c[x] = right
                if vis_r[y] < r - 1:
                    down = min(max(vis_r[y], grid[x][y] + x), r - 1)
                    if y == c - 1 and down == r - 1:
                        return ans + 1
                    for i in range(max(x + 1, vis_r[y] + 1), down + 1):
                        if (i, y) in vis: continue
                        q2.append((i, y))
                        vis.add((i, y))
                    vis_r[y] = down
            q1 = q2
            ans += 1

        return -1



so = Solution()

print(so.minimumVisitedCells([[13,16,10,4,7,17,17,0,8,15,13,15,8,13,3,7,13,12,11,3,0,3,3,5,5,1,5,1,9,3,5,5,3,11,3,5,11,6,7,8,4,0,0,5,5,6,0,3,5,1,3,2,7,2,7,5,0,4,5,3,1,2,1,3,4,3,1,1,4,0,0,4,2,3,2,0,3,0,1,2,0,0,2,2,1],[17,5,14,2,16,5,0,16,9,14,5,1,10,5,3,3,5,6,13,10,12,13,3,12,8,3,2,6,8,1,10,2,6,4,4,5,4,7,3,4,3,4,6,9,3,7,1,3,1,8,4,0,6,3,2,2,6,6,1,4,1,3,5,1,2,0,0,3,4,1,1,0,1,0,3,1,0,1,0,0,2,2,2,1,1],[2,3,7,16,7,4,1,15,2,4,4,4,14,12,15,10,4,1,1,2,4,5,1,5,9,9,8,0,10,10,1,1,2,6,0,6,4,8,10,9,8,5,8,4,8,5,3,5,8,6,3,2,0,6,5,3,3,0,6,1,2,1,4,0,5,4,3,1,2,3,0,2,1,2,2,1,1,1,2,0,1,1,1,0,0]]))
print(so.minimumVisitedCells([[1,1,0],[0,1,0]]))
print(so.minimumVisitedCells([[0,1,0]]))
print(so.minimumVisitedCells([[1,0]]))
print(so.minimumVisitedCells([[0]]))
print(so.minimumVisitedCells([[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]))
print(so.minimumVisitedCells([[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]]))
print(so.minimumVisitedCells([[2,1,0],[1,0,0]]))




