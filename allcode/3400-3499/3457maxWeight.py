# 给你一个长度为 n 的整数数组 pizzas，其中 pizzas[i] 表示第 i 个披萨的重量。每天你会吃 恰好 4 个披萨。由于你的新陈代谢能力惊人，当你吃重量为 W、X、Y 和 Z 的披萨（其中 W <= X <= Y <= Z）时，你只会增加 1 个披萨的重量！体重增加规则如下：
#
# 在 奇数天（按 1 开始计数）你会增加 Z 的重量。
# 在 偶数天，你会增加 Y 的重量。
# 请你设计吃掉 所有 披萨的最优方案，并计算你可以增加的 最大 总重量。
#
# 注意：保证 n 是 4 的倍数，并且每个披萨只吃一次。
#
#
#
# 示例 1：
#
# 输入： pizzas = [1,2,3,4,5,6,7,8]
#
# 输出： 14
#
# 解释：
#
# 第 1 天，你吃掉下标为 [1, 2, 4, 7] = [2, 3, 5, 8] 的披萨。你增加的重量为 8。
# 第 2 天，你吃掉下标为 [0, 3, 5, 6] = [1, 4, 6, 7] 的披萨。你增加的重量为 6。
# 吃掉所有披萨后，你增加的总重量为 8 + 6 = 14。
#
# 示例 2：
#
# 输入： pizzas = [2,1,1,1,1,1,1,1]
#
# 输出： 3
#
# 解释：
#
# 第 1 天，你吃掉下标为 [4, 5, 6, 0] = [1, 1, 1, 2] 的披萨。你增加的重量为 2。
# 第 2 天，你吃掉下标为 [1, 2, 3, 7] = [1, 1, 1, 1] 的披萨。你增加的重量为 1。
# 吃掉所有披萨后，你增加的总重量为 2 + 1 = 3。
#
#
#
# 提示：
#
# 4 <= n == pizzas.length <= 2 * 105
# 1 <= pizzas[i] <= 105
# n 是 4 的倍数。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        n = len(pizzas) // 4
        pizzas.sort(reverse=True)
        odds = (n + 1) // 2
        ans = sum(pizzas[:odds])
        even = n - odds
        for i in range(odds + 1, 4 * n, 2):
            if even == 0: break
            ans += pizzas[i]
            even -= 1
        return ans


so = Solution()
print(so.maxWeight(pizzas = [1,2,3,4,5,6,7,8]))
print(so.maxWeight(pizzas = [2,1,1,1,1,1,1,1]))




