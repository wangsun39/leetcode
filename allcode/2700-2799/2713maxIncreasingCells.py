# 给你一个下标从 1 开始、大小为 m x n 的整数矩阵 mat，你可以选择任一单元格作为 起始单元格 。
#
# 从起始单元格出发，你可以移动到 同一行或同一列 中的任何其他单元格，但前提是目标单元格的值 严格大于 当前单元格的值。
#
# 你可以多次重复这一过程，从一个单元格移动到另一个单元格，直到无法再进行任何移动。
#
# 请你找出从某个单元开始访问矩阵所能访问的 单元格的最大数量 。
#
# 返回一个表示可访问单元格最大数量的整数。
#
#
#
# 示例 1：
#
#
#
# 输入：mat = [[3,1],[3,4]]
# 输出：2
# 解释：上图展示了从第 1 行、第 2 列的单元格开始，可以访问 2 个单元格。可以证明，无论从哪个单元格开始，最多只能访问 2 个单元格，因此答案是 2 。
# 示例 2：
#
#
#
# 输入：mat = [[1,1],[1,1]]
# 输出：1
# 解释：由于目标单元格必须严格大于当前单元格，在本示例中只能访问 1 个单元格。
# 示例 3：
#
#
#
# 输入：mat = [[3,1,6],[-9,5,7]]
# 输出：4
# 解释：上图展示了从第 2 行、第 1 列的单元格开始，可以访问 4 个单元格。可以证明，无论从哪个单元格开始，最多只能访问 4 个单元格，因此答案是 4 。
#
#
# 提示：
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 105
# 1 <= m * n <= 105
# -105 <= mat[i][j] <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        nt = [[[-1] * 2 for _ in range(m)] for _ in range(n)]  # next 矩阵
        for i, r in enumerate(mat):
            row = [[j, rr] for j, rr in enumerate(r)]
            row.sort(key=lambda x: x[1])
            start = 0
            for kk, [k, v] in enumerate(row[1:], 1):
                if v > row[start][1]:
                    nt[i][row[start][0]][0] = k
                    start = kk
        xmat = list(zip(*mat))  # mat转置
        # print(xmat)
        for i, r in enumerate(xmat):
            row = [[j, rr] for j, rr in enumerate(r)]
            row.sort(key=lambda x: x[1])
            start = 0
            for kk, [k, v] in enumerate(row[1:], 1):
                if v > row[start][1]:
                    nt[row[start][0]][i][1] = k
                    start = kk

        print(nt)



        # @cache
        # def dfs(x, y):
        #     if nt[x][y][0] == nt[x][y][1] == -1:
        #         print(x, y, 1)
        #         return 1
        #     res = 0
        #     if nt[x][y][0] != -1:
        #         res = max(res, dfs(x, nt[x][y][0]) + 1)
        #     if nt[x][y][1] != -1:
        #         res = max(res, dfs(nt[x][y][1], y) + 1)
        #     print(x, y, res)
        #     return res
        #
        # ans = 0
        # for i in range(n):
        #     for j in range(m):
        #         ans = max(ans, dfs(i, j))

        return ans


so = Solution()
print(so.maxIncreasingCells([[7,6,3],[-7,-5,6],[-7,0,-4],[6,6,0],[-8,6,0]]))
print(so.maxIncreasingCells([[3,1,6],[-9,5,7]]))
print(so.maxIncreasingCells([[3, 1], [3, 4]]))
print(so.maxIncreasingCells([[1,1],[1,1]]))
