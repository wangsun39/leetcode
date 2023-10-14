# 给你一个下标从 0 开始、大小为 m x n 的二维矩阵 grid ，请你求解大小同样为 m x n 的答案矩阵 answer 。
#
# 矩阵 answer 中每个单元格 (r, c) 的值可以按下述方式进行计算：
#
# 令 topLeft[r][c] 为矩阵 grid 中单元格 (r, c) 左上角对角线上 不同值 的数量。
# 令 bottomRight[r][c] 为矩阵 grid 中单元格 (r, c) 右下角对角线上 不同值 的数量。
# 然后 answer[r][c] = |topLeft[r][c] - bottomRight[r][c]| 。
#
# 返回矩阵 answer 。
#
# 矩阵对角线 是从最顶行或最左列的某个单元格开始，向右下方向走到矩阵末尾的对角线。
#
# 如果单元格 (r1, c1) 和单元格 (r, c) 属于同一条对角线且 r1 < r ，则单元格 (r1, c1) 属于单元格 (r, c) 的左上对角线。类似地，可以定义右下对角线。
#
#
#
# 示例 1：
#
#
# 输入：grid = [[1,2,3],[3,1,5],[3,2,1]]
# 输出：[[1,1,0],[1,0,1],[0,1,1]]
# 解释：第 1 个图表示最初的矩阵 grid 。
# 第 2 个图表示对单元格 (0,0) 计算，其中蓝色单元格是位于右下对角线的单元格。
# 第 3 个图表示对单元格 (1,2) 计算，其中红色单元格是位于左上对角线的单元格。
# 第 4 个图表示对单元格 (1,1) 计算，其中蓝色单元格是位于右下对角线的单元格，红色单元格是位于左上对角线的单元格。
# - 单元格 (0,0) 的右下对角线包含 [1,1] ，而左上对角线包含 [] 。对应答案是 |1 - 0| = 1 。
# - 单元格 (1,2) 的右下对角线包含 [] ，而左上对角线包含 [2] 。对应答案是 |0 - 1| = 1 。
# - 单元格 (1,1) 的右下对角线包含 [1] ，而左上对角线包含 [1] 。对应答案是 |1 - 1| = 0 。
# 其他单元格的对应答案也可以按照这样的流程进行计算。
# 示例 2：
#
# 输入：grid = [[1]]
# 输出：[[0]]
# 解释：- 单元格 (0,0) 的右下对角线包含 [] ，左上对角线包含 [] 。对应答案是 |0 - 0| = 0 。
#
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n, grid[i][j] <= 50
from leetcode.allcode.competition.mypackage import *

class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        r, c = len(grid), len(grid[0])
        ans = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                s1, s2 = set(), set()
                for k in range(1, min(i + 1, j + 1)):
                    s1.add(grid[i-k][j-k])
                x = len(s1)
                for k in range(1, min(r - i, c - j)):
                    s2.add(grid[i+k][j+k])
                y = len(s2)
                ans[i][j] = abs(x - y)
        return ans


so = Solution()
print(so.differenceOfDistinctValues(grid = [[1,2,3],[3,1,5],[3,2,1]]))
print(so.differenceOfDistinctValues(grid = [[1]]))




