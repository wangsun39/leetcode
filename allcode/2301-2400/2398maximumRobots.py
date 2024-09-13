# 你有 n 个机器人，给你两个下标从 0 开始的整数数组 chargeTimes 和 runningCosts ，两者长度都为 n 。第 i 个机器人充电时间为 chargeTimes[i] 单位时间，花费 runningCosts[i] 单位时间运行。再给你一个整数 budget 。
#
# 运行 k 个机器人 总开销 是 max(chargeTimes) + k * sum(runningCosts) ，其中 max(chargeTimes) 是这 k 个机器人中最大充电时间，sum(runningCosts) 是这 k 个机器人的运行时间之和。
#
# 请你返回在 不超过 budget 的前提下，你 最多 可以 连续 运行的机器人数目为多少。
#
#
#
# 示例 1：
#
# 输入：chargeTimes = [3,6,1,3,4], runningCosts = [2,1,3,4,5], budget = 25
# 输出：3
# 解释：
# 可以在 budget 以内运行所有单个机器人或者连续运行 2 个机器人。
# 选择前 3 个机器人，可以得到答案最大值 3 。总开销是 max(3,6,1) + 3 * sum(2,1,3) = 6 + 3 * 6 = 24 ，小于 25 。
# 可以看出无法在 budget 以内连续运行超过 3 个机器人，所以我们返回 3 。
# 示例 2：
#
# 输入：chargeTimes = [11,12,19], runningCosts = [10,8,7], budget = 19
# 输出：0
# 解释：即使运行任何一个单个机器人，还是会超出 budget，所以我们返回 0 。
#
#
# 提示：
#
# chargeTimes.length == runningCosts.length == n
# 1 <= n <= 5 * 104
# 1 <= chargeTimes[i], runningCosts[i] <= 105
# 1 <= budget <= 1015

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        r = 0
        ans = 0
        hp = []
        pre_del = defaultdict(int)  # 预删除
        s = 0
        for l in range(n):
            while hp and pre_del[-hp[0]]:
                x = -heappop(hp)
                pre_del[x] -= 1
            v = -hp[0] + (r - l) * s if hp else 0
            if v <= budget:
                ans = max(ans, r - l)
                while r < n:
                    heappush(hp, -chargeTimes[r])
                    s += runningCosts[r]
                    r += 1
                    v = -hp[0] + (r - l) * s
                    if v <= budget:
                        ans = max(ans, r - l)
                    else:
                        break
            s -= runningCosts[l]
            pre_del[chargeTimes[l]] += 1

        return ans


so = Solution()
print(so.maximumRobots(chargeTimes = [79,25], runningCosts = [8,42], budget = 85))  # 1
print(so.maximumRobots(chargeTimes = [8,76,74,9,75,71,71,42,15,58,88,38,56,59,10,11], runningCosts = [1,92,41,63,22,37,37,8,68,97,39,59,45,50,29,37], budget = 412))  # 3
print(so.maximumRobots(chargeTimes = [3,6,1,3,4], runningCosts = [2,1,3,4,5], budget = 25))  # 3
print(so.maximumRobots(chargeTimes = [11,12,19], runningCosts = [10,8,7], budget = 19))  # 0




