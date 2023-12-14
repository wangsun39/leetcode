# 给你一个 m x n 的二进制矩阵 grid ，每个格子要么为 0 （空）要么为 1 （被占据）。
#
# 给你邮票的尺寸为 stampHeight x stampWidth 。我们想将邮票贴进二进制矩阵中，且满足以下 限制 和 要求 ：
#
# 覆盖所有 空 格子。
# 不覆盖任何 被占据 的格子。
# 我们可以放入任意数目的邮票。
# 邮票可以相互有 重叠 部分。
# 邮票不允许 旋转 。
# 邮票必须完全在矩阵 内 。
# 如果在满足上述要求的前提下，可以放入邮票，请返回 true ，否则返回 false 。
#
#
#
# 示例 1：
#
#
#
# 输入：grid = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]], stampHeight = 4, stampWidth = 3
# 输出：true
# 解释：我们放入两个有重叠部分的邮票（图中标号为 1 和 2），它们能覆盖所有与空格子。
# 示例 2：
#
#
#
# 输入：grid = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], stampHeight = 2, stampWidth = 2
# 输出：false
# 解释：没办法放入邮票覆盖所有的空格子，且邮票不超出网格图以外。
#
#
# 提示：
#
# m == grid.length
# n == grid[r].length
# 1 <= m, n <= 105
# 1 <= m * n <= 2 * 105
# grid[r][c] 要么是 0 ，要么是 1 。
# 1 <= stampHeight, stampWidth <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        r, c = len(grid), len(grid[0])
        s = [[0] * c for _ in range(r)]  # 前缀和
        for i in range(r):
            for j in range(c):
                if i == j == 0:
                    s[i][j] = grid[0][0]
                    continue
                if i == 0:
                    s[i][j] = s[i][j - 1] + grid[i][j]
                    continue
                if j == 0:
                    s[i][j] = s[i - 1][j] + grid[i][j]
                    continue
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + grid[i][j]

        def can_post(i, j):
            res = s[i + stampHeight - 1][j + stampWidth - 1]
            if i > 0:
                res -= s[i - 1][j + stampWidth - 1]
            if j > 0:
                res -= s[i + stampHeight - 1][j - 1]
            if i > 0 and j > 0:
                res += s[i - 1][j - 1]
            return 0 == res

        diff = [[0] * c for _ in range(r)]  # 贴了邮票后的差分数组
        for i in range(r - stampHeight + 1):
            for j in range(c - stampWidth + 1):
                if grid[i][j]: continue
                if can_post(i, j):
                    diff[i][j] += 1
                    if i + stampHeight < r:
                        diff[i + stampHeight][j] -= 1
                    if j + stampWidth < c:
                        diff[i][j + stampWidth] -= 1
                    if i + stampHeight < r and j + stampWidth < c:
                        diff[i + stampHeight][j + stampWidth] += 1

        ss = [[0] * c for _ in range(r)]  # diff 的前缀和， 每个格子贴的邮票数
        for i in range(r):
            for j in range(c):
                if i == j == 0:
                    ss[i][j] = diff[0][0]
                    continue
                if i == 0:
                    ss[i][j] = ss[i][j - 1] + diff[i][j]
                    continue
                if j == 0:
                    ss[i][j] = ss[i - 1][j] + diff[i][j]
                    continue
                ss[i][j] = ss[i - 1][j] + ss[i][j - 1] - ss[i - 1][j - 1] + diff[i][j]

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0 and ss[i][j] == 0:
                    return False
        return True


so = Solution()
print(so.possibleToStamp(grid = [[0,0,1],[0,0,1],[0,1,1]], stampHeight = 2, stampWidth = 2))
print(so.possibleToStamp(grid = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], stampHeight = 2, stampWidth = 2))
print(so.possibleToStamp(grid = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]], stampHeight = 4, stampWidth = 3))






