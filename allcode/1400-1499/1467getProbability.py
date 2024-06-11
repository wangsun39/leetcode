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
        # 这题只需要考虑所有的组合数即可
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

    def getProbability2(self, balls: List[int]) -> float:
        # 另一种dp的写法效率高
        # 只需要考虑一个盒子的情况即可，另一个盒子是对称的，概率相同。
        # 一个盒子中的组合总数为C(2n, n)，现在还需要找到这些组合中组合颜色数量和剩余颜色数量相同的组合数。
        # 颜色相同组合数 / 总组合数 就是要求的概率。
        # 要颜色相同的最理想状态下就是每一种颜色的球都分到了两个盒子中。
        # 当一种颜色的球全部都被分到一个盒子中，那么这个盒子的颜色数量会+1
        # 当一种颜色的球全部都没有分到一个盒子中，那么这个盒子的颜色数量会-1.
        # 当一种颜色的球分到了两个盒子中，那么这个盒子的颜色数量保持不变。
        # 这时候问题就变成了背包问题，在每个颜色的球中选多少个可以在选完球后球的数量等于n，且颜色数量无变化。
        # 构建深搜，参数分别为当前选择的颜色，已选球数量，颜色变化。
        # 当颜色选择完后，如果已选球数量等于n且颜色无变化则返回1，否则返回0.
        # 颜色未选择完时，假设当前颜色球数量为n，分别选择[0, n]之间的i个球后继续深搜即可求解。（这里选择i个球后需要乘以C(n, i)，因为选择i个球有C(n, i)种方式)

        def combine(x, y):  # 组合数
            return math.factorial(x) // math.factorial(y) // math.factorial(x - y)

        s = sum(balls)  # 球总数
        l = len(balls)  # 颜色总数

        @lru_cache(None)
        def dfs(i, c, t):
            if i == l:  # 如果颜色选完了
                return int(t == 0 and c == s // 2)  # 选了1/2的球数量且颜色无变化
            res = dfs(i + 1, c, t + 1) + dfs(i + 1, c + balls[i], t - 1)  # 不选和全选组合数都为1，直接相加即可，需要更新颜色变化
            for j in range(1, balls[i]):  # 其他情况，颜色无变化
                res += dfs(i + 1, c + j, t) * combine(balls[i], j)
            return res

        res = dfs(0, 0, 0)
        return res / combine(s, s // 2)




so = Solution()
print(so.getProbability([2,1,1]))
print(so.getProbability([3,2,1]))  # 0.3
print(so.getProbability([1,1]))
print(so.getProbability([1,2,1,2]))




