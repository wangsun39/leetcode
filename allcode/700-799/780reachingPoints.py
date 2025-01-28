# 给定四个整数sx,sy，tx和ty，如果通过一系列的转换可以从起点(sx, sy)到达终点(tx, ty)，则返回 true，否则返回false。
#
# 从点(x, y)可以转换到(x, x+y) 或者(x+y, y)。
#
#
#
# 示例 1:
#
# 输入: sx = 1, sy = 1, tx = 3, ty = 5
# 输出: true
# 解释:
# 可以通过以下一系列转换从起点转换到终点：
# (1, 1) -> (1, 2)
# (1, 2) -> (3, 2)
# (3, 2) -> (3, 5)
# 示例 2:
#
# 输入: sx = 1, sy = 1, tx = 2, ty = 2
# 输出: false
# 示例 3:
#
# 输入: sx = 1, sy = 1, tx = 1, ty = 1
# 输出: true
#
#
# 提示:
#
# 1 <= sx, sy, tx, ty <= 109


class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:

        while True:
            if (tx == sx) and (ty == sy):
                return True
            if tx < sx or ty < sy:
                return False
            if tx == sx:
                return (ty - sy) % tx == 0
            if ty == sy:
                return (tx - sx) % ty == 0
            if tx < ty:
                ty = ty % tx
            elif tx > ty:
                tx = tx % ty
            else:
                return False



so = Solution()
print(so.reachingPoints(sx = 9, sy = 10, tx = 9, ty = 19))
print(so.reachingPoints(sx = 1, sy = 1, tx = 3, ty = 5))
print(so.reachingPoints(sx = 1, sy = 1, tx = 2, ty = 2))

