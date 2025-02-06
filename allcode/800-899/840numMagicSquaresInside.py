# 3 x 3 的幻方是一个填充有 从 1 到 9  的不同数字的 3 x 3 矩阵，其中每行，每列以及两条对角线上的各数之和都相等。
#
# 给定一个由整数组成的row x col 的 grid，其中有多少个 3 × 3 的 “幻方” 子矩阵？
#
# 注意：虽然幻方只能包含 1 到 9 的数字，但 grid 可以包含最多15的数字。
#
#
#
# 示例 1：
#
#
#
# 输入: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]
# 输出: 1
# 解释:
# 下面的子矩阵是一个 3 x 3 的幻方：
#
# 而这一个不是：
#
# 总的来说，在本示例所给定的矩阵中只有一个 3 x 3 的幻方子矩阵。
# 示例 2:
#
# 输入: grid = [[8]]
# 输出: 0
#
#
# 提示:
#
# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 10
# 0 <= grid[i][j] <= 15

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        def check(a, b):
            u = set()
            for i in range(3):
                for j in range(3):
                    if grid[a + i][b + j] > 9 or grid[a + i][b + j] == 0: return False
                    u.add(grid[a + i][b + j])
            if len(u) != 9: return False
            s = sum(grid[a][b: b + 3])
            if sum(grid[a + 1][b: b + 3]) != s or s != sum(grid[a + 2][b: b + 3]):
                return False
            if grid[a][b] + grid[a + 1][b + 1] + grid[a + 2][b + 2] != s: return False
            if grid[a + 2][b] + grid[a + 1][b + 1] + grid[a][b + 2] != s: return False
            for j in range(3):
                ss = 0
                for i in range(3):
                    ss += grid[a + i][b + j]
                if ss != s:
                    return False

            return True


        ans = 0
        for i in range(r - 2):
            for j in range(c - 2):
                if check(i, j):
                    ans += 1
        return ans

so = Solution()
print(so.numMagicSquaresInside(grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]))

