# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
#
# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
#
# 你可以认为每种硬币的数量是无限的。
#
#
#
# 示例 1：
#
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1
# 示例 2：
#
# 输入：coins = [2], amount = 3
# 输出：-1
# 示例 3：
#
# 输入：coins = [1], amount = 0
# 输出：0
#
#
# 提示：
#
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104

from functools import cache
from math import inf
from typing import List
class Solution:
    def coinChange2(self, coins: List[int], amount: int) -> int:
        min_num = [0] + [-1 for _ in range(max(amount, 2))]
        if 1 in coins:
            min_num[1], min_num[2] = 1, 2
        if 2 in coins:
            min_num[2] = 1
        if amount < 3:
            return min_num[amount]
        for e in range(3, amount+1):
            if e in coins:
                min_num[e] = 1
                continue
            for i in range(1, e):
                if i > e - i:
                    break
                if -1 != min_num[i] and -1 != min_num[e - i]:
                    if -1 == min_num[e] or min_num[e] > min_num[i] + min_num[e - i]:
                        min_num[e] = min_num[i] + min_num[e - i]
        print(min_num)
        return min_num[amount]

    def coinChange1(self, coins: List[int], amount: int) -> int:
        min_num = [0] + [-1 for _ in range(max(amount, 2))]
        if 1 in coins:
            min_num[1], min_num[2] = 1, 2
        if 2 in coins:
            min_num[2] = 1
        if amount < 3:
            return min_num[amount]
        for e in range(max(3, min(coins)), amount+1):
            if e in coins:
                min_num[e] = 1
                continue
            for i in coins:
                if i >= e:
                    continue
                if -1 != min_num[e - i]:
                    if -1 == min_num[e]:
                        min_num[e] = min_num[e - i] + 1
                    else:
                        min_num[e] = min(min_num[e], min_num[e - i] + 1)
        print(min_num)
        return min_num[amount]


    def coinChange(self, coins: List[int], amount: int) -> int:
        # 2023/5/21 记忆化搜索
        n = len(coins)

        @cache
        def dfs(idx, c):  # 前 idx 项，组成 c 的最少硬币数
            if c == 0: return 0
            if idx == 0:
                return inf if c % coins[0] else c // coins[0]
            ans = dfs(idx - 1, c)
            if c >= coins[idx]:
                ans = min(ans, dfs(idx, c - coins[idx]) + 1)

            return ans
        ans = dfs(n - 1, amount)
        return ans if ans != inf else -1

so = Solution()
print('res =', so.coinChange([205,21,66,115,396,469,202,442,364], 5563))
print('res =', so.coinChange([1, 2, 5], 11))
print('res =', so.coinChange1([1,2,5,10], 20))
print('res =', so.coinChange1([431,62,88,428], 9084))
print('res =', so.coinChange([1], 0))
print('res =', so.coinChange([1], 1))
print('res =', so.coinChange([2], 3))

print('res =', so.coinChange1([474,83,404,3], 264))


