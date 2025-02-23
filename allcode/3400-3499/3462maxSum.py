# 给你一个大小为 n x m 的二维矩阵 grid ，以及一个长度为 n 的整数数组 limits ，和一个整数 k 。你的目标是从矩阵 grid 中提取出 至多 k 个元素，并计算这些元素的最大总和，提取时需满足以下限制：
#
# 从 grid 的第 i 行提取的元素数量不超过 limits[i] 。
#
# 返回最大总和。
#
#
#
# 示例 1：
#
# 输入：grid = [[1,2],[3,4]], limits = [1,2], k = 2
#
# 输出：7
#
# 解释：
#
# 从第 2 行提取至多 2 个元素，取出 4 和 3 。
# 至多提取 2 个元素时的最大总和 4 + 3 = 7 。
# 示例 2：
#
# 输入：grid = [[5,3,7],[8,2,6]], limits = [2,2], k = 3
#
# 输出：21
#
# 解释：
#
# 从第 1 行提取至多 2 个元素，取出 7 。
# 从第 2 行提取至多 2 个元素，取出 8 和 6 。
# 至多提取 3 个元素时的最大总和 7 + 8 + 6 = 21 。
#
#
# 提示：
#
# n == grid.length == limits.length
# m == grid[i].length
# 1 <= n, m <= 500
# 0 <= grid[i][j] <= 105
# 0 <= limits[i] <= m
# 0 <= k <= min(n * m, sum(limits))

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        n, m = len(grid), len(grid[0])
        cnt = [0] * n
        elements = []
        for i in range(n):
            for j in range(m):
                elements.append([grid[i][j], i])
        elements.sort(reverse=True)
        ans = 0
        for x, r in elements:
            if cnt[r] >= limits[r]: continue
            ans += x
            k -= 1
            cnt[r] += 1
            if k == 0:
                return ans
        return 0



so = Solution()
print(so.maxSum(grid = [[7,10,3,3,7,7,0],[5,5,9,2,10,5,2]], limits = [3,7], k = 7))
print(so.maxSum(grid = [[0,1]], limits = [0], k = 0))
print(so.maxSum(grid = [[1,2],[3,4]], limits = [1,2], k = 2))




