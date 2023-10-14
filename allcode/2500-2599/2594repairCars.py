# 给你一个整数数组 ranks ，表示一些机械工的 能力值 。ranksi 是第 i 位机械工的能力值。能力值为 r 的机械工可以在 r * n2 分钟内修好 n 辆车。
#
# 同时给你一个整数 cars ，表示总共需要修理的汽车数目。
#
# 请你返回修理所有汽车 最少 需要多少时间。
#
# 注意：所有机械工可以同时修理汽车。
#
#
#
# 示例 1：
#
# 输入：ranks = [4,2,3,1], cars = 10
# 输出：16
# 解释：
# - 第一位机械工修 2 辆车，需要 4 * 2 * 2 = 16 分钟。
# - 第二位机械工修 2 辆车，需要 2 * 2 * 2 = 8 分钟。
# - 第三位机械工修 2 辆车，需要 3 * 2 * 2 = 12 分钟。
# - 第四位机械工修 4 辆车，需要 1 * 4 * 4 = 16 分钟。
# 16 分钟是修理完所有车需要的最少时间。
# 示例 2：
#
# 输入：ranks = [5,1,8], cars = 6
# 输出：16
# 解释：
# - 第一位机械工修 1 辆车，需要 5 * 1 * 1 = 5 分钟。
# - 第二位机械工修 4 辆车，需要 1 * 4 * 4 = 16 分钟。
# - 第三位机械工修 1 辆车，需要 8 * 1 * 1 = 8 分钟。
# 16 分钟时修理完所有车需要的最少时间。
#
#
# 提示：
#
# 1 <= ranks.length <= 105
# 1 <= ranks[i] <= 100
# 1 <= cars <= 106

from leetcode.allcode.competition.mypackage import *

class Solution:
    def repairCars1(self, ranks: List[int], cars: int) -> int:
        def check(val): # 给定一个时间，计算是否能修完所有汽车
            s = sum(int((val / x) ** 0.5) for x in ranks)
            return s >= cars
        lo, hi = 0, ranks[0] * cars * cars
        while lo < hi - 1:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid
        return hi

    def repairCars(self, ranks: List[int], cars: int) -> int:
        counter = Counter(ranks)
        def check(val): # 给定一个时间，计算是否能修完所有汽车
            ncar = 0
            for r, k in counter.items():
                ncar += int((val // r) ** 0.5) * k
            return ncar >= cars
        lo, hi = 0, ranks[0] * cars * cars
        while lo < hi - 1:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid
        return hi



so = Solution()
print(so.repairCars(ranks = [4,2,3,1], cars = 10))
print(so.repairCars(ranks = [5,1,8], cars = 6))




