# 给你一个大小为 n x n 二进制矩阵 grid 。最多 只能将一格0 变成1 。
#
# 返回执行此操作后，grid 中最大的岛屿面积是多少？
#
# 岛屿 由一组上、下、左、右四个方向相连的1 形成。
#
# 
#
# 示例 1:
#
# 输入: grid = [[1, 0], [0, 1]]
# 输出: 3
# 解释: 将一格0变成1，最终连通两个小岛得到面积为 3 的岛屿。
# 示例 2:
#
# 输入: grid = [[1, 1], [1, 0]]
# 输出: 4
# 解释: 将一格0变成1，岛屿的面积扩大为 4。
# 示例 3:
#
# 输入: grid = [[1, 1], [1, 1]]
# 输出: 4
# 解释: 没有0可以让我们变成1，面积依然为 4。
# 
#
# 提示：
#
# n == grid.length
# n == grid[i].length
# 1 <= n <= 500
# grid[i][j] 为 0 或 1


from typing import List
from collections import defaultdict
from collections import Counter
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        islands = defaultdict(int)  # 一个格子对应的岛编号
        area = defaultdict(int)  # 岛的面积
        row, col = len(grid), len(grid[0])
        number = 1
        def find(i, j, number):
            if grid[i][j] == 0 or islands[(i, j)] == number:
                return
            islands[(i, j)] = number
            area[number] += 1
            dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for d1, d2 in dir:
                if 0 <= i + d1 < row and 0 <= j + d2 < col:
                    find(i + d1, j + d2, number)

        for i in range(row):
            # print(grid[i])
            for j in range(col):
                if grid[i][j] == 1 and (i, j) not in islands:
                    find(i, j, number)
                    number += 1
        if len(area) == 0:
            return 1
        ans = max(area.values())
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    x = [islands[(i - 1, j)], islands[(i + 1, j)], islands[(i, j - 1)], islands[(i, j + 1)]]
                    cur = 0
                    counter = Counter(x)
                    for k in counter:
                        cur += area[k]
                    ans = max(ans, cur + 1)
        return ans

so = Solution()
print(so.largestIsland([[0,0,0,0,0,0,0],[0,1,1,1,1,0,0],[0,1,0,0,1,0,0],[1,0,1,0,1,0,0],[0,1,0,0,1,0,0],[0,1,0,0,1,0,0],[0,1,1,1,1,0,0]]))  # 18
print(so.largestIsland([[1,0,1],[0,0,0],[0,1,1]]))  # 4
print(so.largestIsland([[0,0],[0,1]]))  # 2
print(so.largestIsland([[0, 0], [0, 0]]))
print(so.largestIsland([[1, 1], [1, 1]]))
print(so.largestIsland(grid = [[1, 0], [0, 1]]))
print(so.largestIsland([[1, 1], [1, 0]]))

