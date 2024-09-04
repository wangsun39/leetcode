# 给你一个由正整数构成的二维矩阵 grid。
#
# 你需要从矩阵中选择 一个或多个 单元格，选中的单元格应满足以下条件：
#
# 所选单元格中的任意两个单元格都不会处于矩阵的 同一行。
# 所选单元格的值 互不相同。
# 你的得分为所选单元格值的总和。
#
# 返回你能获得的 最大 得分。
#
#
#
# 示例 1：
#
# 输入： grid = [[1,2,3],[4,3,2],[1,1,1]]
#
# 输出： 8
#
# 解释：
#
#
#
# 选择上图中用彩色标记的单元格，对应的值分别为 1、3 和 4 。
#
# 示例 2：
#
# 输入： grid = [[8,7,6],[8,3,2]]
#
# 输出： 15
#
# 解释：
#
#
#
# 选择上图中用彩色标记的单元格，对应的值分别为 7 和 8 。
#
#
#
# 提示：
#
# 1 <= grid.length, grid[i].length <= 10
# 1 <= grid[i][j] <= 100

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        dic = defaultdict(set)  # 表示一个val在哪些行
        for i in range(r):
            for j in range(c):
                dic[grid[i][j]].add(i)
        l = [[k, v] for k, v in dic.items()]
        n = len(l)  # 不同元素的个数

        @cache
        def dfs(i, mask):  # i 表示 l 的下标，mask: 之前选过的行的掩码
            if i == n: return 0
            res = dfs(i + 1, mask)
            val, rows = l[i]
            for j in rows:
                if mask & (1 << j): continue
                res = max(res, val + dfs(i + 1, mask ^ (1 << j)))
            return res

        return dfs(0, 0)


so = Solution()
print(so.maxScore(grid = [[1,5,20,18],[19,6,17,3],[12,10,6,3],[1,20,12,15]]))  # 69
print(so.maxScore(grid = [[5,5],[5,5],[11,5]]))  # 16
print(so.maxScore(grid = [[1,2,3],[4,3,2],[1,1,1]]))
print(so.maxScore(grid = [[8,7,6],[8,3,2]]))




