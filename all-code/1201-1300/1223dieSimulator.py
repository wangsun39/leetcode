# 有一个骰子模拟器会每次投掷的时候生成一个 1 到 6 的随机数。
#
# 不过我们在使用它时有个约束，就是使得投掷骰子时，连续 掷出数字 i 的次数不能超过 rollMax[i]（i 从 1 开始编号）。
#
# 现在，给你一个整数数组 rollMax 和一个整数 n，请你来计算掷 n 次骰子可得到的不同点数序列的数量。
#
# 假如两个序列中至少存在一个元素不同，就认为这两个序列是不同的。由于答案可能很大，所以请返回 模 10^9 + 7 之后的结果。
#
#
#
# 示例 1：
#
# 输入：n = 2, rollMax = [1,1,2,2,2,3]
# 输出：34
# 解释：我们掷 2 次骰子，如果没有约束的话，共有 6 * 6 = 36 种可能的组合。但是根据 rollMax 数组，数字 1 和 2 最多连续出现一次，所以不会出现序列 (1,1) 和 (2,2)。因此，最终答案是 36-2 = 34。
# 示例 2：
#
# 输入：n = 2, rollMax = [1,1,1,1,1,1]
# 输出：30
# 示例 3：
#
# 输入：n = 3, rollMax = [1,1,1,2,2,3]
# 输出：181
#
#
# 提示：
#
# 1 <= n <= 5000
# rollMax.length == 6
# 1 <= rollMax[i] <= 15

from typing import List
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * 6 for _ in range(n)]  # dp[i][j] 长度为 i + 1， 以 j 结尾的有效序列个数
        for j in range(6):
            dp[0][j] = 1
        for i in range(1, n):
            for j in range(6):
                for t in range(1, rollMax[j] + 1):
                    if i - t < 0: break
                    for k in range(6):
                        if k == j: continue
                        dp[i][j] += dp[i - t][k]
                        dp[i][j] %= MOD
                if i + 1 <= rollMax[j]:   # 长度不足 rollMax[j] 时， 补上全是 j 的一个
                    dp[i][j] += 1
        print(dp)
        return sum(dp[-1]) % MOD


obj = Solution()
print(obj.dieSimulator(n = 2, rollMax = [1,1,2,2,2,3]))   # 34
print(obj.dieSimulator(n = 3, rollMax = [1,1,1,1,1,3]))   # 161
print(obj.dieSimulator(n = 3, rollMax = [1,1,1,2,2,3]))   # 181
print(obj.dieSimulator(n = 2, rollMax = [1,1,1,1,1,1]))   # 30
