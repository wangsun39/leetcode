# 给定2D空间中四个点的坐标p1,p2,p3和p4，如果这四个点构成一个正方形，则返回 true 。
#
# 点的坐标pi 表示为 [xi, yi] 。输入 不是 按任何顺序给出的。
#
# 一个 有效的正方形 有四条等边和四个等角(90度角)。
#
#
#
# 示例 1:
#
# 输入: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# 输出: True
# 示例 2:
#
# 输入：p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
# 输出：false
# 示例 3:
#
# 输入：p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
# 输出：true
#
#
# 提示:
#
# p1.length == p2.length == p3.length == p4.length == 2
# -104<= xi, yi<= 104



from typing import List
import collections

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        p = [p1, p2, p3, p4]
        p.sort()
        def dd(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

        return dd(p[0], p[1]) * 2 == dd(p[0], p[2]) * 2 == dd(p[3], p[1]) * 2 == dd(p[3], p[2]) * 2 == dd(p[0], p[3]) > 0




so = Solution()

print('ret = ', so.validSquare([0,0],[0,0],[0,0],[0,0]))
print('ret = ', so.validSquare([1,1],[5,3],[3,5],[7,7]))
print('ret = ', so.validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]))
print('ret = ', so.validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]))
print('ret = ', so.validSquare(p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]))


