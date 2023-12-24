# 给你一个用无限二维网格表示的花园，每一个 整数坐标处都有一棵苹果树。整数坐标 (i, j) 处的苹果树有 |i| + |j| 个苹果。
#
# 你将会买下正中心坐标是 (0, 0) 的一块 正方形土地 ，且每条边都与两条坐标轴之一平行。
#
# 给你一个整数 neededApples ，请你返回土地的 最小周长 ，使得 至少 有 neededApples 个苹果在土地 里面或者边缘上。
#
# |x| 的值定义为：
#
# 如果 x >= 0 ，那么值为 x
# 如果 x < 0 ，那么值为 -x
#
#
# 示例 1：
#
#
# 输入：neededApples = 1
# 输出：8
# 解释：边长长度为 1 的正方形不包含任何苹果。
# 但是边长为 2 的正方形包含 12 个苹果（如上图所示）。
# 周长为 2 * 4 = 8 。
# 示例 2：
#
# 输入：neededApples = 13
# 输出：16
# 示例 3：
#
# 输入：neededApples = 1000000000
# 输出：5040
#
#
# 提示：
#
# 1 <= neededApples <= 1015

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:

        def calc(x):  # 计算顶点在(x,x)的正方形内的苹果数量
            # 经过计算，这个正方形边缘的苹果数为 12*n*n
            # 因此所有的苹果数为
            return x * (x + 1) * (2 * x + 1) * 2

        lo, hi = 0, 10 ** 5
        while lo < hi - 1:
            mid = (lo + hi) // 2
            num = calc(mid)
            if num == neededApples:
                return mid * 8
            if num < neededApples:
                lo = mid
            else:
                hi = mid
        return 8 * hi



so = Solution()
print(so.minimumPerimeter(1))
print(so.minimumPerimeter(13))
print(so.minimumPerimeter(1000000000))




