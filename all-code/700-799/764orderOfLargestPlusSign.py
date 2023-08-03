# 在一个 n x n 的矩阵 grid 中，除了在数组 mines 中给出的元素为 0，其他每个元素都为 1。mines[i] = [xi, yi]表示 grid[xi][yi] == 0
#
# 返回  grid 中包含 1 的最大的 轴对齐 加号标志的阶数 。如果未找到加号标志，则返回 0 。
#
# 一个 k 阶由 1 组成的 “轴对称”加号标志 具有中心网格 grid[r][c] == 1 ，以及4个从中心向上、向下、向左、向右延伸，长度为 k-1，由 1 组成的臂。注意，只有加号标志的所有网格要求为 1 ，别的网格可能为 0 也可能为 1 。
#
#
#
# 示例 1：
#
#
#
# 输入: n = 5, mines = [[4, 2]]
# 输出: 2
# 解释: 在上面的网格中，最大加号标志的阶只能是2。一个标志已在图中标出。
# 示例 2：
#
#
#
# 输入: n = 1, mines = [[0, 0]]
# 输出: 0
# 解释: 没有加号标志，返回 0 。
#
#
# 提示：
#
# 1 <= n <= 500
# 1 <= mines.length <= 5000
# 0 <= xi, yi < n
# 每一对 (xi, yi) 都 不重复
from copy import deepcopy
from typing import List


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        s = set((x, y) for x, y in mines)
        M = [[1] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if (i, j) in s:
                    M[i][j] = 0
        left, right = deepcopy(M), deepcopy(M)
        up, down = deepcopy(M), deepcopy(M)
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                if M[i][j]:
                    left[i][j] = left[i][j - 1] + 1
                if M[i][n - 1 - j]:
                    right[i][n - 1 - j] = right[i][n - j] + 1
        for j in range(1, n - 1):
            for i in range(1, n - 1):
                if M[i][j]:
                    up[i][j] = up[i - 1][j] + 1
                if M[n - 1 - i][j]:
                    down[n - 1 - i][j] = down[n - i][j] + 1
        # print(left, right)
        # print(up, down)
        # print(M)
        ans = 0
        for i in range(n):
            for j in range(n):
                if min(left[i][j], right[i][j], up[i][j], down[i][j]) == 2:
                    print(i, j)
                ans = max(min(left[i][j], right[i][j], up[i][j], down[i][j]), ans)
        return ans



so = Solution()
print(so.orderOfLargestPlusSign(n = 5, mines = [[0,0],[0,3],[1,1],[1,4],[2,3],[3,0],[4,2]]))  # 1
print(so.orderOfLargestPlusSign(n = 2, mines = [[0,0],[0,1],[1,0]]))  # 1
print(so.orderOfLargestPlusSign(n = 5, mines = [[4, 2]]))  # 2
print(so.orderOfLargestPlusSign(n = 1, mines = [[0, 0]]))  # 0

