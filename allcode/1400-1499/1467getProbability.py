# 桌面上有 2n 个颜色不完全相同的球，球上的颜色共有 k 种。给你一个大小为 k 的整数数组 balls ，其中 balls[i] 是颜色为 i 的球的数量。
#
# 所有的球都已经 随机打乱顺序 ，前 n 个球放入第一个盒子，后 n 个球放入另一个盒子（请认真阅读示例 2 的解释部分）。
#
# 注意：这两个盒子是不同的。例如，两个球颜色分别为 a 和 b，盒子分别为 [] 和 ()，那么 [a] (b) 和 [b] (a) 这两种分配方式是不同的（请认真阅读示例的解释部分）。
#
# 请返回「两个盒子中球的颜色数相同」的情况的概率。答案与真实值误差在 10^-5 以内，则被视为正确答案
#
#
#
# 示例 1：
#
# 输入：balls = [1,1]
# 输出：1.00000
# 解释：球平均分配的方式只有两种：
# - 颜色为 1 的球放入第一个盒子，颜色为 2 的球放入第二个盒子
# - 颜色为 2 的球放入第一个盒子，颜色为 1 的球放入第二个盒子
# 这两种分配，两个盒子中球的颜色数都相同。所以概率为 2/2 = 1 。
# 示例 2：
#
# 输入：balls = [2,1,1]
# 输出：0.66667
# 解释：球的列表为 [1, 1, 2, 3]
# 随机打乱，得到 12 种等概率的不同打乱方案，每种方案概率为 1/12 ：
# [1,1 / 2,3], [1,1 / 3,2], [1,2 / 1,3], [1,2 / 3,1], [1,3 / 1,2], [1,3 / 2,1], [2,1 / 1,3], [2,1 / 3,1], [2,3 / 1,1], [3,1 / 1,2], [3,1 / 2,1], [3,2 / 1,1]
# 然后，我们将前两个球放入第一个盒子，后两个球放入第二个盒子。
# 这 12 种可能的随机打乱方式中的 8 种满足「两个盒子中球的颜色数相同」。
# 概率 = 8/12 = 0.66667
# 示例 3：
#
# 输入：balls = [1,2,1,2]
# 输出：0.60000
# 解释：球的列表为 [1, 2, 2, 3, 4, 4]。要想显示所有 180 种随机打乱方案是很难的，但只检查「两个盒子中球的颜色数相同」的 108 种情况是比较容易的。
# 概率 = 108 / 180 = 0.6 。
#
#
# 提示：
#
# 1 <= balls.length <= 8
# 1 <= balls[i] <= 6
# sum(balls) 是偶数
import math

from leetcode.allcode.competition.mypackage import *

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        n = len(balls)
        s = sum(balls)
        tot = comb(s, s // 2)

        def dfs(idx, l):  # 从第idx个盒子开始，l表示左盒子已选的球
            if sum(l) > s // 2: return 0
            if idx == n:
                if sum(l) != s // 2: return 0
                l2 = [balls[i] - x for i, x in enumerate(l)]
                if sum(1 for x in l if x) != sum(1 for x in l2 if x): return 0
                return 1
            res = 0
            for i in range(balls[idx] + 1):  # balls[idx] 个里面取 i 个
                l[idx] = i
                res += dfs(idx + 1, l) * comb(balls[idx], i)
                l[idx] = 0
            return res
        v = dfs(0, [0] * n)
        return v / tot


so = Solution()
print(so.getProbability([2,1,1]))
print(so.getProbability([3,2,1]))  # 0.3
print(so.getProbability([1,1]))
print(so.getProbability([1,2,1,2]))




