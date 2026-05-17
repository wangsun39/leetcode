# 给你一个 n x m 的整数矩阵 matrix ，所有元素均为非负整数。
#
# 一个 非零 单元格 (row, col) 会按如下方式检查其附近的单元格：
#
# 令 x = matrix[row][col] 。
# 考虑在 (row, col) 的 x 行和 x 列范围内的每个单元格。
# 忽略矩阵外的单元格。
# 忽略行距离和列距离都恰好等于 x 的 单元格。
# 如果单元格 (row, col) 是 非零 的，并且所有考虑的单元格中没有一个值 大于 x ，那么该单元格就是一个 局部最大值 。
#
# 返回一个整数，表示 matrix 中 局部最大值 的数量。
#
#
#
# 示例 1：
#
# 输入： matrix = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,2,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
#
# 输出： 1
#
#
#
# 解释：
#
# 对于非零单元格 (3, 3) ，x = matrix[3][3] = 2 。
# 高亮的单元格是在 (3, 3) 的 x 行和 x 列范围内被考虑的单元格。
# 行距离和列距离都等于 x = 2 的四个单元格被忽略。
# 没有一个被考虑的单元格的值大于 2 ，因此 (3, 3) 是一个局部最大值。
# 没有其他非零单元格，所以答案是 1 。
# 示例 2：
#
# 输入： matrix = [[1,2],[3,4]]
#
# 输出： 1
#
# 解释：
#
# 只有值为 4 的单元格是局部最大值。其他每个非零单元格都考虑到了一个具有更大值的单元格。
#
# 示例 3：
#
# 输入： matrix = [[1,0,1],[0,1,0],[1,0,1]]
#
# 输出： 5
#
# 解释：
#
# 对于值为 1 的单元格，考虑的单元格是其自身及其在矩阵内的 4 个方向上相邻的单元格。
# 这五个值为 1 的单元格中，每一个都只考虑到值为 0 或 1 的单元格，所以这五个单元格都是局部最大值。
# 示例 4：
#
# 输入： matrix = [[1,1],[1,1]]
#
# 输出： 4
#
# 解释：
#
# 所有单元格都具有相同的值。因此，没有任何一个单元格会考虑到具有更大值的其他单元格，所以所有 4 个单元格都是局部最大值。
#
#
#
# 提示：
#
# 1 <= n == matrix.length <= 200
# 1 <= m == matrix[i].length <= 200
# 0 <= matrix[i][j] <= 200

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countLocalMaximums(self, matrix: List[List[int]]) -> int:
        r, c = len(matrix), len(matrix[0])
        mx = max(max(a) for a in matrix)

        prefix = [[[0] * (c + 1) for _ in range(r + 1)] for _ in range(mx + 1)]

        for t in range(mx + 1):
            for i in range(1, r + 1):
                for j in range(1, c + 1):
                    prefix[t][i][j] = (prefix[t][i-1][j] +
                                       prefix[t][i][j-1] -
                                       prefix[t][i-1][j-1] +
                                       (1 if matrix[i-1][j-1] > t else 0))

        def count_greater(r1, c1, r2, c2, x):
            if r1 > r2 or c1 > c2:
                return 0
            return (prefix[x][r2+1][c2+1] - prefix[x][r1][c2+1] -
                    prefix[x][r2+1][c1] + prefix[x][r1][c1])

        ans = 0
        for i in range(r):
            for j in range(c):
                x = matrix[i][j]
                if x == 0:
                    continue

                r1, r2 = max(0, i - x), min(r - 1, i + x)
                c1, c2 = max(0, j - x), min(c - 1, j + x)

                total = count_greater(r1, c1, r2, c2, x)

                corners = 0
                for dr, dc in [(-x, -x), (-x, x), (x, -x), (x, x)]:
                    nr, nc = i + dr, j + dc
                    if r1 <= nr <= r2 and c1 <= nc <= c2:
                        if matrix[nr][nc] > x:
                            corners += 1

                if total - corners == 0:
                    ans += 1

        return ans


so = Solution()
print(so.countLocalMaximums(matrix = [[1,2]]))
print(so.countLocalMaximums(matrix = [[1,0,1],[0,1,0],[1,0,1]]))




