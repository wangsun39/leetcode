# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
#
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
#
#
#
# 网格中的障碍物和空位置分别用 1 和 0 来表示。
#
#  
#
# 示例 1：
#
#
# 输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# 输出：2
# 解释：
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
# 示例 2：
#
#
# 输入：obstacleGrid = [[0,1],[0,0]]
# 输出：1
#  
#
# 提示：
#
# m == obstacleGrid.length
# n == obstacleGrid[i].length
# 1 <= m, n <= 100
# obstacleGrid[i][j] 为 0 或 1

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        for i in range(M):
            for j in range(N):
                if i == j == 0:
                    obstacleGrid[i][j] = 1 - obstacleGrid[i][j]
                    continue
                if 1 == obstacleGrid[i][j]:
                    obstacleGrid[i][j] = 0
                else:
                    if 0 == i:
                        obstacleGrid[i][j] = obstacleGrid[i][j - 1] if j > 0 else obstacleGrid[i][j]
                    elif 0 == j:
                        obstacleGrid[i][j] = obstacleGrid[i - 1][j] if i > 0 else obstacleGrid[i][j]
                    else:
                        obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]

        print(obstacleGrid)
        return obstacleGrid[M - 1][N - 1]

so = Solution()

print(so.uniquePathsWithObstacles( [[0,0],[0,1]]))
print(so.uniquePathsWithObstacles( [[0,0,0],[0,1,0],[0,0,0]]))
print(so.uniquePathsWithObstacles( [[0,1],[0,0]]))
