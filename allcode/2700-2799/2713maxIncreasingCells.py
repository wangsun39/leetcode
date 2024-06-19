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
        g = defaultdict(list)
        r, c = len(mat), len(mat[0])
        for i in range(r):
            for j in range(c):
                g[mat[i][j]].append((i, j))
        row = [0] * r  # 第i行的当前最大的递增个数
        col = [0] * c  # 第j列的当前最大的递增个数
        ans = 0
        for v, pairs in sorted(g.items()):
            map = {}
            for i, j in pairs:
                map[(i, j)] = max(row[i], col[j]) + 1
                ans = max(ans, map[(i, j)])
            for i, j in pairs:
                row[i] = max(row[i], map[(i, j)])
                col[j] = max(col[j], map[(i, j)])
        return ans



so = Solution()
print(so.maxIncreasingCells([[-4,8,-3,2,-4,-8,7,5,-2],[-5,5,-7,-2,6,-6,-8,-4,-4]]))
print(so.maxIncreasingCells([[7,6,3],[-7,-5,6],[-7,0,-4],[6,6,0],[-8,6,0]]))
print(so.maxIncreasingCells([[1,1],[1,1]]))
print(so.maxIncreasingCells([[3,1,6],[-9,5,7]]))
print(so.maxIncreasingCells([[3, 1], [3, 4]]))
