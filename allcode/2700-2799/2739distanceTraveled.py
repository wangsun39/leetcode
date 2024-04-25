# 卡车有两个油箱。给你两个整数，mainTank 表示主油箱中的燃料（以升为单位），additionalTank 表示副油箱中的燃料（以升为单位）。
#
# 该卡车每耗费 1 升燃料都可以行驶 10 km。每当主油箱使用了 5 升燃料时，如果副油箱至少有 1 升燃料，则会将 1 升燃料从副油箱转移到主油箱。
#
# 返回卡车可以行驶的最大距离。
#
# 注意：从副油箱向主油箱注入燃料不是连续行为。这一事件会在每消耗 5 升燃料时突然且立即发生。
#
#
#
# 示例 1：
#
# 输入：mainTank = 5, additionalTank = 10
# 输出：60
# 解释：
# 在用掉 5 升燃料后，主油箱中燃料还剩下 (5 - 5 + 1) = 1 升，行驶距离为 50km 。
# 在用掉剩下的 1 升燃料后，没有新的燃料注入到主油箱中，主油箱变为空。
# 总行驶距离为 60km 。
# 示例 2：
#
# 输入：mainTank = 1, additionalTank = 2
# 输出：10
# 解释：
# 在用掉 1 升燃料后，主油箱变为空。
# 总行驶距离为 10km 。
#
#
# 提示：
#
# 1 <= mainTank, additionalTank <= 100

from leetcode.allcode.competition.mypackage import *

class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        ans = 0
        consume = 0
        while mainTank:
            consume += 1
            mainTank -= 1
            ans += 10
            if consume % 5 == 0 and additionalTank:
                additionalTank -= 1
                mainTank += 1
        return ans

    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # 2024/4/25 数学的方法
        # 解方程 设x为additionalTank中最多可以放到mainTank中的数量
        # (mainTank + x) // 5 == x  其中 0 <= x <= additionalTank ,带取整的方程
        # 设 mainTank + x = 5x + r (0<=r<5，为余数)
        # x = (mainTank - r) // 4
        # 枚举 r ，得到x后，需要验证 0 <= x <= additionalTank 条件
        # 为了保证能够用mainTank兑换additionalTank x次，还需要满足
        # 兑换1次需要满足 mainTank >= 5， 之后变成 mainTank - 4
        # 兑换2次需要满足 mainTank - 4 >= 5， 之后变成 mainTank - 4*2
        # 兑换3次需要满足 mainTank - 4*2 >= 5， 之后变成 mainTank - 4*3
        # 兑换x次需要满足 mainTank - 4*(x-1) >= 5， 之后变成 mainTank - 4*x
        # 因此要满足 mainTank - 4*(x-1) >= 5 就能换出x个additionalTank

        # additionalTank 可以全换走
        if mainTank - 4*(additionalTank-1) >= 5:
            return (mainTank + additionalTank) * 10
        # 剩下的情况，是不可能换出所有 additionalTank 的
        # 也就不用再判断 0 <= x <= additionalTank 条件
        for r in range(5):
            x = (mainTank - r) // 4
            if mainTank - (x - 1) * 4 >= 5:
                return (mainTank + x) * 10


so = Solution()
print(so.distanceTraveled(mainTank = 5, additionalTank = 10))
print(so.distanceTraveled(mainTank = 1, additionalTank = 2))




