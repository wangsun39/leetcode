# 给你两个字符串 coordinate1 和 coordinate2，代表 8 x 8 国际象棋棋盘上的两个方格的坐标。
#
# 以下是棋盘的参考图。
#
#
#
# 如果这两个方格颜色相同，返回 true，否则返回 false。
#
# 坐标总是表示有效的棋盘方格。坐标的格式总是先字母（表示列），再数字（表示行）。
#
#
#
# 示例 1：
#
# 输入： coordinate1 = "a1", coordinate2 = "c3"
#
# 输出： true
#
# 解释：
#
# 两个方格均为黑色。
#
# 示例 2：
#
# 输入： coordinate1 = "a1", coordinate2 = "h3"
#
# 输出： false
#
# 解释：
#
# 方格 "a1" 是黑色，而 "h3" 是白色。
#
#
#
# 提示：
#
# coordinate1.length == coordinate2.length == 2
# 'a' <= coordinate1[0], coordinate2[0] <= 'h'
# '1' <= coordinate1[1], coordinate2[1] <= '8'

from leetcode.allcode.competition.mypackage import *

class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        c2i = {c: i for i, c in enumerate(ascii_lowercase)}
        x1, y1 = coordinate1[0], coordinate1[1]
        x2, y2 = coordinate2[0], coordinate2[1]
        x1 = c2i[x1]
        x2 = c2i[x2]
        y1 = int(y1)
        y2 = int(y2)
        d1, d2 = abs(x1 - x2), abs(y1 - y2)
        if d1 & 1 == d2 & 1:
            return True
        return False



so = Solution()
print(so.checkTwoChessboards(coordinate1 = "a1", coordinate2 = "c3"))
print(so.checkTwoChessboards(coordinate1 = "a1", coordinate2 = "h3"))
print(so.checkTwoChessboards(coordinate1 = "a1", coordinate2 = "c3"))




