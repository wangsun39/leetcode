# 给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。
#
# 请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。
#
# 假设每一种面额的硬币有无限个。 
#
# 题目数据保证结果符合 32 位带符号整数。
#
#  
#
# 示例 1：
#
# 输入：amount = 5, coins = [1, 2, 5]
# 输出：4
# 解释：有四种方式可以凑成总金额：
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# 示例 2：
#
# 输入：amount = 3, coins = [2]
# 输出：0
# 解释：只用面额 2 的硬币不能凑成总金额 3 。
# 示例 3：
#
# 输入：amount = 10, coins = [10]
# 输出：1
#  
#
# 提示：
#
# 1 <= coins.length <= 300
# 1 <= coins[i] <= 5000
# coins 中的所有值 互不相同
# 0 <= amount <= 5000

from typing import List

class Solution:
    def change1(self, amount: int, coins: List[int]) -> int:
        # 这个方法可以通过，性能比较差
        if amount == 0:
            return 1
        N = len(coins)
        dp = [[0] * (amount + 1) for _ in range(N + 1)]  # dp[i][j] 表示只用前i个元素组成数量为j的不同组合
        coins.sort()
        coins.insert(0, 0)
        for i in range(1, N + 1):
            if coins[i] > amount:
                break
            dp[i][coins[i]] = 1
        for i in range(1, N + 1):    #  用前 i 个元素
            for j in range(1, amount + 1):  # total
                if coins[i] > j:
                    dp[i][j] = dp[i - 1][j]
                    continue
                for k in range(1, i + 1):
                    dp[i][j] += dp[k][j - coins[k]]

        print(dp)
        return dp[-1][-1]
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i]: 金额为i时的方法数
        #
        # 第一层循环：针对每一个硬币
        # 第二层循环：需要更新比这个硬币面额大的数额
        #
        # 新的方法数 = 不采用这个硬币的方法数（之前的） + 采用这个硬币的方法数
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[-1]



so = Solution()
print(so.change(0, [7]))   # 1
print(so.change(5, [1, 2, 5]))
print(so.change(3, [2]))
print(so.change(10, [10]))

