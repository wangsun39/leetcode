# 给你一个大小为 n x n 的整数方阵 grid。返回一个经过如下调整的矩阵：
#
# 左下角三角形（包括中间对角线）的对角线按 非递增顺序 排序。
# 右上角三角形 的对角线按 非递减顺序 排序。
#
#
# 示例 1：
#
# 输入： grid = [[1,7,3],[9,8,2],[4,5,6]]
#
# 输出： [[8,2,3],[9,6,7],[4,5,1]]
#
# 解释：
#
#
#
# 标有黑色箭头的对角线（左下角三角形）应按非递增顺序排序：
#
# [1, 8, 6] 变为 [8, 6, 1]。
# [9, 5] 和 [4] 保持不变。
# 标有蓝色箭头的对角线（右上角三角形）应按非递减顺序排序：
#
# [7, 2] 变为 [2, 7]。
# [3] 保持不变。
# 示例 2：
#
# 输入： grid = [[0,1],[1,2]]
#
# 输出： [[2,1],[1,0]]
#
# 解释：
#
#
#
# 标有黑色箭头的对角线必须按非递增顺序排序，因此 [0, 2] 变为 [2, 0]。其他对角线已经符合要求。
#
# 示例 3：
#
# 输入： grid = [[1]]
#
# 输出： [[1]]
#
# 解释：
#
# 只有一个元素的对角线已经符合要求，因此无需修改。
#
#
#
# 提示：
#
# grid.length == grid[i].length == n
# 1 <= n <= 10
# -105 <= grid[i][j] <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for i in range(n - 1, 0, -1):
            l = [grid[j][i + j] for j in range(n - i)]
            l.sort()
            for j in range(n - i):
                grid[j][i + j] = l[j]
        for i in range(n):
            l = [grid[i + j][j] for j in range(n - i)]
            l.sort(reverse=True)
            for j in range(n - i):
                grid[i + j][j] = l[j]
        return grid


so = Solution()
print(so.sortMatrix(grid = [[1,7,3],[9,8,2],[4,5,6]]))




