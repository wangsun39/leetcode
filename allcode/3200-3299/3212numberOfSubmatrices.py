# 给你一个正整数 n。
#
# 如果一个二进制字符串 x 的所有长度为 2 的
# 子字符串
# 中包含 至少 一个 "1"，则称 x 是一个 有效 字符串。
#
# 返回所有长度为 n 的 有效 字符串，可以以任意顺序排列。
#
#
#
# 示例 1：
#
# 输入： n = 3
#
# 输出： ["010","011","101","110","111"]
#
# 解释：
#
# 长度为 3 的有效字符串有："010"、"011"、"101"、"110" 和 "111"。
#
# 示例 2：
#
# 输入： n = 1
#
# 输出： ["0","1"]
#
# 解释：
#
# 长度为 1 的有效字符串有："0" 和 "1"。
#
#
#
# 提示：
#
# 1 <= n <= 18

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        sx = [[] for _ in range(r)]
        sy = [[] for _ in range(r)]
        for i in range(r):
            if grid[i][0] == 'X':
                sx[i].append(1)
                sy[i].append(0)
            elif grid[i][0] == 'Y':
                sx[i].append(0)
                sy[i].append(1)
            else:
                sx[i].append(0)
                sy[i].append(0)
            for j in range(1, c):
                if grid[i][j] == 'X':
                    sx[i].append(sx[i][-1] + 1)
                    sy[i].append(sy[i][-1])
                elif grid[i][j] == 'Y':
                    sx[i].append(sx[i][-1])
                    sy[i].append(sy[i][-1] + 1)
                else:
                    sx[i].append(sx[i][-1])
                    sy[i].append(sy[i][-1])
        ssx = [0] * c
        ssy = [0] * c
        ans = 0
        for i in range(r):
            for j in range(c):
                ssx[j] += sx[i][j]
                ssy[j] += sy[i][j]
                if ssx[j] == ssy[j] != 0:
                    ans += 1
        return ans


so = Solution()
print(so.numberOfSubmatrices(grid = [["X","Y","."],["Y",".","."]]))
print(so.numberOfSubmatrices(grid = [["X","X"],["X","Y"]]))
print(so.numberOfSubmatrices(grid = [[".","."],[".","."]]))




