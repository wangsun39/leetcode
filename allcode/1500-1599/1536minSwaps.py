# 给你一个 n x n 的二进制网格 grid，每一次操作中，你可以选择网格的 相邻两行 进行交换。
#
# 一个符合要求的网格需要满足主对角线以上的格子全部都是 0 。
#
# 请你返回使网格满足要求的最少操作次数，如果无法使网格符合要求，请你返回 -1 。
#
# 主对角线指的是从 (1, 1) 到 (n, n) 的这些格子。
#
#
#
# 示例 1：
#
#
#
# 输入：grid = [[0,0,1],[1,1,0],[1,0,0]]
# 输出：3
# 示例 2：
#
#
#
# 输入：grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
# 输出：-1
# 解释：所有行都是一样的，交换相邻行无法使网格符合要求。
# 示例 3：
#
#
#
# 输入：grid = [[1,0,0],[1,1,0],[1,1,1]]
# 输出：0
#
#
# 提示：
#
# n == grid.length
# n == grid[i].length
# 1 <= n <= 200
# grid[i][j] 要么是 0 要么是 1 。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zero_cnt = [0] * n  # 计算每行最右侧有多个连续0
        for i in range(n):
            c = 0
            for j in range(n - 1, 0, -1):
                if grid[i][j] != 0:
                    break
                else:
                    c += 1
                    zero_cnt[i] = c
        ans = 0
        for i in range(n):
            if zero_cnt[i] < n - i - 1:  # 对于不满足条件的行，用冒泡的方式从下方换一行上来
                # 不能从上方换，因为不可能满足上面行的条件
                isOk = False
                for j in range(i + 1, n):
                    if zero_cnt[j] >= n - i - 1:
                        ans += j - i
                        zero_cnt[i + 1: j + 1] = zero_cnt[i: j]
                        isOk = True
                        break
                if not isOk:
                    return -1

        return ans


so = Solution()
print(so.minSwaps(grid = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]))
print(so.minSwaps(grid = [[0,0,1],[1,1,0],[1,0,0]]))
print(so.minSwaps(grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]))
print(so.minSwaps(grid = [[1,0,0],[1,1,0],[1,1,1]]))




