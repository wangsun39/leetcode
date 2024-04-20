# 给你一个 m x n 的网格 grid。网格里的每个单元都代表一条街道。grid[i][j] 的街道可以是：
#
# 1 表示连接左单元格和右单元格的街道。
# 2 表示连接上单元格和下单元格的街道。
# 3 表示连接左单元格和下单元格的街道。
# 4 表示连接右单元格和下单元格的街道。
# 5 表示连接左单元格和上单元格的街道。
# 6 表示连接右单元格和上单元格的街道。
#
#
# 你最开始从左上角的单元格 (0,0) 开始出发，网格中的「有效路径」是指从左上方的单元格 (0,0) 开始、一直到右下方的 (m-1,n-1) 结束的路径。该路径必须只沿着街道走。
#
# 注意：你 不能 变更街道。
#
# 如果网格中存在有效的路径，则返回 true，否则返回 false 。
#
#
#
# 示例 1：
#
#
#
# 输入：grid = [[2,4,3],[6,5,2]]
# 输出：true
# 解释：如图所示，你可以从 (0, 0) 开始，访问网格中的所有单元格并到达 (m - 1, n - 1) 。
# 示例 2：
#
#
#
# 输入：grid = [[1,2,1],[1,2,1]]
# 输出：false
# 解释：如图所示，单元格 (0, 0) 上的街道没有与任何其他单元格上的街道相连，你只会停在 (0, 0) 处。
# 示例 3：
#
# 输入：grid = [[1,1,2]]
# 输出：false
# 解释：你会停在 (0, 1)，而且无法到达 (0, 2) 。
# 示例 4：
#
# 输入：grid = [[1,1,1,1,1,1,3]]
# 输出：true
# 示例 5：
#
# 输入：grid = [[2],[2],[2],[2],[2],[2],[6]]
# 输出：true
#
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# 1 <= grid[i][j] <= 6

from leetcode.allcode.competition.mypackage import *

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        vis = {(0, 0)}
        def nt(x0, y0, x1, y1): # 前面的格子(x0, y0), 当前格子(x1, y1)，返回下个格子
            if y0 < y1:
                if grid[x1][y1] == 1:
                    return [x1, y1 + 1]
                if grid[x1][y1] == 3:
                    return [x1 + 1, y1]
                if grid[x1][y1] == 5:
                    return [x1 - 1, y1]
                return [-1, -1]
            if y0 > y1:
                if grid[x1][y1] == 1:
                    return [x1, y1 - 1]
                if grid[x1][y1] == 4:
                    return [x1 + 1, y1]
                if grid[x1][y1] == 6:
                    return [x1 - 1, y1]
                return [-1, -1]
            if x0 < x1:
                if grid[x1][y1] == 2:
                    return [x1 + 1, y1]
                if grid[x1][y1] == 5:
                    return [x1, y1 - 1]
                if grid[x1][y1] == 6:
                    return [x1, y1 + 1]
                return [-1, -1]
            if x0 > x1:
                if grid[x1][y1] == 2:
                    return [x1 - 1, y1]
                if grid[x1][y1] == 3:
                    return [x1, y1 - 1]
                if grid[x1][y1] == 4:
                    return [x1, y1 + 1]
                return [-1, -1]


        def check(x0, y0, x1, y1):
            while True:
                if 0 <= x1 < r and 0 <= y1 < c:
                    x2, y2 = nt(x0, y0, x1, y1)
                    if (x2, y2) == (r - 1, c - 1):
                        return nt(x1, y1, x2, y2) != [-1, -1]
                    if (x2, y2) in vis:
                        return False
                    vis.add((x2, y2))
                    x0, y0, x1, y1 = x1, y1, x2, y2
                else:
                    return False

        x0 = y0 = 0
        r, c = len(grid), len(grid[0])
        if r == c == 1:
            return True
        if grid[0][0] == 1:
            x1, y1 = 0, 1
            return check(x0, y0, x1, y1)
        elif grid[0][0] == 2:
            x1, y1 = 1, 0
            return check(x0, y0, x1, y1)
        elif grid[0][0] == 3:
            x1, y1 = 1, 0
            return check(x0, y0, x1, y1)
        elif grid[0][0] == 6:
            x1, y1 = 0, 1
            return check(x0, y0, x1, y1)
        elif grid[0][0] == 4:
            return check(0, 0, 1, 0) or check(0, 0, 0, 1)
        else:
            return False



so = Solution()
print(so.hasValidPath([[6,1,1,1,1,1,1,1,1,1,1,1,1,3],[4,1,1,1,1,1,1,1,1,1,1,1,1,5],[6,1,1,1,1,1,1,1,1,1,1,1,1,3],[4,1,1,1,1,1,1,1,1,1,1,1,1,5],[6,1,1,1,1,1,1,1,1,1,1,1,1,3],[4,1,1,1,1,1,1,1,1,1,1,1,1,5],[6,1,1,1,1,1,1,1,1,1,1,1,1,3],[4,1,1,1,1,1,1,1,1,1,1,1,1,5],[6,1,1,1,1,1,1,1,1,1,1,1,1,3],[4,1,1,1,1,1,1,1,1,1,1,1,1,5],[6,1,1,1,1,1,1,1,1,1,1,1,1,3],[4,1,1,1,1,1,1,1,1,1,1,1,1,5],[6,1,1,1,1,1,1,1,1,1,1,1,1,3],[4,1,1,1,1,1,1,1,1,1,1,1,1,5],[6,1,1,1,1,1,1,1,1,1,1,1,1,3]]))
print(so.hasValidPath([[4,1],[6,1]]))
print(so.hasValidPath([[1,1,2]]))
print(so.hasValidPath([[1]]))
print(so.hasValidPath([[2,4,3],[6,5,2]]))
print(so.hasValidPath([[1,2,1],[1,2,1]]))
print(so.hasValidPath([[1,1,1,1,1,1,3]]))
print(so.hasValidPath([[2],[2],[2],[2],[2],[2],[6]]))




