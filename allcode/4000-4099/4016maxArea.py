# 给你一个大小为 m × n 的二维整数矩阵 mat，其中：
#
# mat[r][c] == 1 表示位于行 r 和列 c 的单元格是可用的。
# mat[r][c] == 0 表示它不可用。
# 你的任务是找到满足以下条件的 两个子矩阵 ：
#
# 这两个子矩阵都必须是边长为 k 的正方形。
# 这两个子矩阵不能共享任何单元格。
# 每个子矩阵只能覆盖 mat[r][c] == 1 的单元格。
# 返回单个正方形的最大可能面积。如果无法选择两个这样的正方形，则返回 0。
#
# 一个 子矩阵 (x1, y1, x2, y2) 包括所有满足 x1 <= x <= x2 且 y1 <= y <= y2 的单元格 mat[x][y] 。
#
#
#
# 示例 1：
#
#
#
# 输入： mat = [[1,1,1,0],[1,1,1,1],[0,0,1,1]]
#
# 输出： 4
#
# 解释：
#
# 最大且相等的无重叠正方形的边长为 k = 2，面积为 4。
#
# 第一个正方形从左上角 (0, 0) 开始，覆盖单元格 (0, 0)、(0, 1)、(1, 0) 和 (1, 1)。
# 第二个正方形从左上角 (1, 2) 开始，覆盖单元格 (1, 2)、(1, 3)、(2, 2) 和 (2, 3)。
# 因此，答案是 4。
#
# 示例 2：
#
#
#
# 输入： mat = [[0,1],[1,0]]
#
# 输出： 1
#
# 解释：
#
# 最大且相等的无重叠正方形的边长为 k = 1，面积为 1。
#
# 第一个正方形从左上角 (0, 1) 开始，覆盖单元格 (0, 1)。
# 第二个正方形从左上角 (1, 0) 开始，覆盖单元格 (1, 0)。
# 因此，答案是 1。
#
# 示例 3：
#
#
#
# 输入： mat = [[0,0],[0,1]]
#
# 输出： 0
#
# 解释：
#
# 只有一个可用的单元格，因此无法选择两个无重叠的正方形。因此，答案是 0。
#
#
#
# 提示：
#
# mat.length == m
# mat[i].length == n
# 1 <= m, n <= 500
# mat[i][j] 是 0 或 1。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxArea(self, mat: List[List[int]]) -> int:
        r, c = len(mat), len(mat[0])

        # 1. 计算 grid 的二维前缀和
        s = [[0] * (c + 1) for _ in range(r + 1)]
        for i, row in enumerate(mat):
            for j, v in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + v

        # 2. 计算任意矩形区域和
        def sumRegion(row1: int, col1: int, sz: int) -> int:
            return s[row1 + sz][col1 + sz] - s[row1][col1 + sz] - s[row1 + sz][col1] + s[row1][col1]

        def check(val):
            # isCovered = [[0] * (c - val + 1) for _ in range(r - val + 1)]
            row = [0] * r  # 前i行是否有covered正方形
            col = [0] * c  # 前i列是否有covered正方形
            for i in range(r - val + 1):
                # [i, i + val)  i + val <= r
                for j in range(c - val + 1):
                    if sumRegion(i, j, val) == val * val:
                        if i > 0 and row[i - 1]:
                            return True
                        if j > 0 and col[j - 1]:
                            return True
                        row[i + val - 1] = 1
                        col[j + val - 1] = 1
                        # isCovered[i][j] = 1
                    if j > 0:
                        col[j] |= col[j - 1]
                if i > 0:
                    row[i] |= row[i - 1]
            for i in range(r - val + 1):
                for j in range(val, c - val + 1):
                    if sumRegion(i, j, val) == val * val:
                        if col[j - 1]:
                            return True
            return False

        if not check(1):
            return 0
        lo, hi = 1, min(r, c) + 1
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid
        return lo * lo





so = Solution()
print(so.maxArea(mat = [[0,1,1,1,1,1,1,0],[1,1,1,1,0,1,0,1],[1,1,0,0,1,1,1,1]]))
print(so.maxArea(mat = [[1,1,1,1],[1,1,1,1]]))
print(so.maxArea(mat = [[1,0,1]]))
print(so.maxArea(mat = [[1,1,1,0],[1,1,1,1],[0,0,1,1]]))



