# 给你一个由正整数组成的 m x n 矩阵 grid。你的任务是判断是否可以通过 一条水平或一条垂直分割线 将矩阵分割成两部分，使得：
#
# 分割后形成的每个部分都是 非空 的。
# 两个部分中所有元素的和 相等 ，或者总共 最多移除一个单元格 （从其中一个部分中）的情况下可以使它们相等。
# 如果移除某个单元格，剩余部分必须保持 连通 。
# 如果存在这样的分割，返回 true；否则，返回 false。
#
# 注意： 如果一个部分中的每个单元格都可以通过向上、向下、向左或向右移动到达同一部分中的其他单元格，则认为这一部分是 连通 的。
#
#
#
# 示例 1：
#
# 输入： grid = [[1,4],[2,3]]
#
# 输出： true
#
# 解释：
#
#
#
# 在第 0 行和第 1 行之间进行水平分割，结果两部分的元素和为 1 + 4 = 5 和 2 + 3 = 5，相等。因此答案是 true。
# 示例 2：
#
# 输入： grid = [[1,2],[3,4]]
#
# 输出： true
#
# 解释：
#
#
#
# 在第 0 列和第 1 列之间进行垂直分割，结果两部分的元素和为 1 + 3 = 4 和 2 + 4 = 6。
# 通过从右侧部分移除 2 （6 - 2 = 4），两部分的元素和相等，并且两部分保持连通。因此答案是 true。
# 示例 3：
#
# 输入： grid = [[1,2,4],[2,3,5]]
#
# 输出： false
#
# 解释：
#
#
#
# 在第 0 行和第 1 行之间进行水平分割，结果两部分的元素和为 1 + 2 + 4 = 7 和 2 + 3 + 5 = 10。
# 通过从底部部分移除 3 （10 - 3 = 7），两部分的元素和相等，但底部部分不再连通（分裂为 [2] 和 [5]）。因此答案是 false。
# 示例 4：
#
# 输入： grid = [[4,1,8],[3,2,6]]
#
# 输出： false
#
# 解释：
#
# 不存在有效的分割，因此答案是 false。
#
#
#
# 提示：
#
# 1 <= m == grid.length <= 105
# 1 <= n == grid[i].length <= 105
# 2 <= m * n <= 105
# 1 <= grid[i][j] <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        s = sum(sum(r) for r in grid)
        gt = list(zip(*grid))

        def check(g):
            r = len(g)
            res = 0
            for i in range(r):
                res += sum(g[i])
                if res * 2 == s:
                    return True
            return False

        if check(grid) or check(gt):
            return True

        def check2(g):
            r, c = len(g), len(g[0])
            if r == 1: return False
            ds = defaultdict(set)
            for i in range(r):
                for j in range(c):
                    if i == r - 1 and j != 0 and j != c - 1: continue
                    ds[g[i][j]].add((i, j))
            res = 0
            for i in range(r - 1):
                res += sum(g[i])
                for j in range(c):
                    ds[g[i][j]].remove((i, j))
                if res * 2 > s: break
                obj = s - res * 2
                if len(ds[obj]):
                    if c > 1: return True
                    if (i + 1, 0) in ds[obj] or (r - 1, 0) in ds[obj]:
                        return True
            return False

        def check3(g):
            return check2(g) or check2(g[::-1])

        if check3(grid) or check3(gt):
            return True

        return False


so = Solution()
print(so.canPartitionGrid(grid = [[1, 2, 1, 2, 1, 2]]))
print(so.canPartitionGrid(grid = [[1,4],[2,3]]))
print(so.canPartitionGrid(grid = [[1,2],[3,4]]))
print(so.canPartitionGrid(grid = [[1,2,4],[2,3,5]]))
print(so.canPartitionGrid(grid = [[1,2,4],[2,5,3]]))  # True
print(so.canPartitionGrid(grid = [[4,1,8],[3,2,6]]))




