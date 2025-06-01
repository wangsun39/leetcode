# 给你一个 m x n 的整数矩阵 grid 和一个整数 k。
#
# 对于矩阵 grid 中的每个连续的 k x k 子矩阵，计算其中任意两个 不同值 之间的 最小绝对差 。
#
# 返回一个大小为 (m - k + 1) x (n - k + 1) 的二维数组 ans，其中 ans[i][j] 表示以 grid 中坐标 (i, j) 为左上角的子矩阵的最小绝对差。
#
# 注意：如果子矩阵中的所有元素都相同，则答案为 0。
#
# 子矩阵 (x1, y1, x2, y2) 是一个由选择矩阵中所有满足 x1 <= x <= x2 且 y1 <= y <= y2 的单元格 matrix[x][y] 组成的矩阵。
#
#
#
# 示例 1：
#
# 输入： grid = [[1,8],[3,-2]], k = 2
#
# 输出： [[2]]
#
# 解释：
#
# 只有一个可能的 k x k 子矩阵：[[1, 8], [3, -2]]。
# 子矩阵中的不同值为 [1, 8, 3, -2]。
# 子矩阵中的最小绝对差为 |1 - 3| = 2。因此，答案为 [[2]]。
# 示例 2：
#
# 输入： grid = [[3,-1]], k = 1
#
# 输出： [[0,0]]
#
# 解释：
#
# 每个 k x k 子矩阵中只有一个不同的元素。
# 因此，答案为 [[0, 0]]。
# 示例 3：
#
# 输入： grid = [[1,-2,3],[2,3,5]], k = 2
#
# 输出： [[1,2]]
#
# 解释：
#
# 有两个可能的 k × k 子矩阵：
# 以 (0, 0) 为起点的子矩阵：[[1, -2], [2, 3]]。
# 子矩阵中的不同值为 [1, -2, 2, 3]。
# 子矩阵中的最小绝对差为 |1 - 2| = 1。
# 以 (0, 1) 为起点的子矩阵：[[-2, 3], [3, 5]]。
# 子矩阵中的不同值为 [-2, 3, 5]。
# 子矩阵中的最小绝对差为 |3 - 5| = 2。
# 因此，答案为 [[1, 2]]。
#
#
# 提示：
#
# 1 <= m == grid.length <= 30
# 1 <= n == grid[i].length <= 30
# -105 <= grid[i][j] <= 105
# 1 <= k <= min(m, n)

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        if k == 1:
            return ans

        def calc(r, c):
            arr = []
            for i in range(r, r + k):
                for j in range(c, c + k):
                    arr.append(grid[i][j])
            arr.sort()
            if arr[0] == arr[-1]: return 0
            return min(abs(x - y) for x, y in pairwise(arr) if x != y)

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                ans[i][j] = calc(i, j)
        return ans



so = Solution()
print(so.minAbsDiff(grid = [[1,-2,3],[2,3,5]], k = 2))
print(so.minAbsDiff(grid = [[1,8],[3,-2]], k = 2))




