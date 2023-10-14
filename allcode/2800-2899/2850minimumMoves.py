# 给你一个大小为 3 * 3 ，下标从 0 开始的二维整数矩阵 grid ，分别表示每一个格子里石头的数目。网格图中总共恰好有 9 个石头，一个格子里可能会有 多个 石头。
#
# 每一次操作中，你可以将一个石头从它当前所在格子移动到一个至少有一条公共边的相邻格子。
#
# 请你返回每个格子恰好有一个石头的 最少移动次数 。
#
#
#
# 示例 1：
#
#
#
# 输入：grid = [[1,1,0],[1,1,1],[1,2,1]]
# 输出：3
# 解释：让每个格子都有一个石头的一个操作序列为：
# 1 - 将一个石头从格子 (2,1) 移动到 (2,2) 。
# 2 - 将一个石头从格子 (2,2) 移动到 (1,2) 。
# 3 - 将一个石头从格子 (1,2) 移动到 (0,2) 。
# 总共需要 3 次操作让每个格子都有一个石头。
# 让每个格子都有一个石头的最少操作次数为 3 。
# 示例 2：
#
#
#
# 输入：grid = [[1,3,0],[1,0,0],[1,0,3]]
# 输出：4
# 解释：让每个格子都有一个石头的一个操作序列为：
# 1 - 将一个石头从格子 (0,1) 移动到 (0,2) 。
# 2 - 将一个石头从格子 (0,1) 移动到 (1,1) 。
# 3 - 将一个石头从格子 (2,2) 移动到 (1,2) 。
# 4 - 将一个石头从格子 (2,2) 移动到 (2,1) 。
# 总共需要 4 次操作让每个格子都有一个石头。
# 让每个格子都有一个石头的最少操作次数为 4 。
#
#
# 提示：
#
# grid.length == grid[i].length == 3
# 0 <= grid[i][j] <= 9
# grid 中元素之和为 9 。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        l1, l2 = [], []
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    l1.append([i, j, 1])
                elif grid[i][j] > 1:
                    l2.append([i, j, grid[i][j]])

        def dfs(l1, l2):
            res = inf
            x = y = -1
            for i, [x, y, n2] in enumerate(l2):
                if n2 == 1:
                    continue
                break
            if x == -1: return 0
            l2[i][2] -= 1
            for j, [u, v, n1] in enumerate(l1):
                if n1 == 0:
                    continue
                d = abs(x - u) + abs(y - v)
                l1[j][2] -= 1
                res = min(res, d + dfs(l1, l2))
                l1[j][2] += 1
            # l2[i][2] += 1
            if res < inf:
                return res
            else:
                return 0
        return dfs(l1, l2)




so = Solution()
print(so.minimumMoves(grid = [[2,2,0],[1,1,0],[0,3,0]]))
print(so.minimumMoves(grid = [[3,2,0],[0,1,0],[0,3,0]]))
print(so.minimumMoves(grid = [[1,1,0],[1,1,1],[1,2,1]]))
print(so.minimumMoves(grid = [[1,3,0],[1,0,0],[1,0,3]]))




