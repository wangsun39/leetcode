# 给定一个数组 coordinates ，其中 coordinates[i] = [x, y] ， [x, y] 表示横坐标为 x、纵坐标为 y 的点。请你来判断，这些点是否在该坐标系中属于同一条直线上。
#
#
#
# 示例 1：
#
#
#
# 输入：coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# 输出：true
# 示例 2：
#
#
#
# 输入：coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# 输出：false
#
#
# 提示：
#
# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# coordinates 中不含重复的点

from leetcode.allcode.competition.mypackage import *


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n == 2: return True
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        for x, y in coordinates[2:]:
            if (y - y0) * (x1 - x0) != (x - x0) * (y1 - y0):
                return False
        return True

so = Solution()
print(so.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))





