# 设想有个机器人坐在一个网格的左上角，网格 r 行 c 列。机器人只能向下或向右移动，但不能走到一些被禁止的网格（有障碍物）。设计一种算法，寻找机器人从左上角移动到右下角的路径。
#
#
#
# 网格中的障碍物和空位置分别用 1 和 0 来表示。
#
# 返回一条可行的路径，路径由经过的网格的行号和列号组成。左上角为 0 行 0 列。如果没有可行的路径，返回空数组。
#
# 示例 1：
#
# 输入：[[0,0,0],[0,1,0],[0,0,0]]
# 输出：[[0,0],[0,1],[0,2],[1,2],[2,2]]
# 解释：
# 输入中标粗的位置即为输出表示的路径，即
# 0 行 0 列（左上角） -> 0 行 1 列 -> 0 行 2 列 -> 1 行 2 列 -> 2 行 2 列（右下角）
# 说明：r 和 c 的值均不超过 100。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        r, c = len(obstacleGrid), len(obstacleGrid[0])

        @cache
        def dfs(x, y):
            if obstacleGrid[x][y]: return []
            if [x, y] == [r - 1, c - 1]:
                return [[x, y]]
            if x + 1 < r:
                res = dfs(x + 1, y)
                if len(res):
                    return [[x, y]] + res
            if y + 1 < c:
                res = dfs(x, y + 1)
                if len(res):
                    return [[x, y]] + res
            return []

        return dfs(0, 0)



so = Solution()




