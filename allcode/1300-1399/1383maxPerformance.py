# 给定两个整数 n 和 k，以及两个长度为 n 的整数数组 speed 和 efficiency。现有 n 名工程师，编号从 1 到 n。其中 speed[i] 和 efficiency[i] 分别代表第 i 位工程师的速度和效率。
#
# 从这 n 名工程师中最多选择 k 名不同的工程师，使其组成的团队具有最大的团队表现值。
#
# 团队表现值 的定义为：一个团队中「所有工程师速度的和」乘以他们「效率值中的最小值」。
#
# 请你返回该团队的​​​​​​最大团队表现值，由于答案可能很大，请你返回结果对 10^9 + 7 取余后的结果。
#
#
#
# 示例 1：
#
# 输入：n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
# 输出：60
# 解释：
# 我们选择工程师 2（speed=10 且 efficiency=4）和工程师 5（speed=5 且 efficiency=7）。他们的团队表现值为 performance = (10 + 5) * min(4, 7) = 60 。
# 示例 2：
#
# 输入：n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
# 输出：68
# 解释：
# 此示例与第一个示例相同，除了 k = 3 。我们可以选择工程师 1 ，工程师 2 和工程师 5 得到最大的团队表现值。表现值为 performance = (2 + 10 + 5) * min(5, 4, 7) = 68 。
# 示例 3：
#
# 输入：n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
# 输出：72
#
#
# 提示：
#
# 1 <= k <= n <= 10^5
# speed.length == n
# efficiency.length == n
# 1 <= speed[i] <= 10^5
# 1 <= efficiency[i] <= 10^8

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        comb = sorted(zip(efficiency, speed), reverse=True)  # 按 efficiency 降序排序
        shp = 0
        hp = []
        ans = 0
        for e, s in comb:
            if len(hp) == k:
                if hp[0] < s:
                    x = heappop(hp)
                    heappush(hp, s)
                    shp += (s - x)
            else:
                heappush(hp, s)
                shp += s
            ans = max(ans, shp * e)
        return ans % MOD




so = Solution()
print(so.maxPerformance(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2))  # 60
print(so.maxPerformance(n = 3, speed = [2,8,2], efficiency = [2,7,1], k = 2))  # 56
print(so.maxPerformance(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3))  # 68
print(so.maxPerformance(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4))  # 72





