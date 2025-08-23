# 三步问题。有个小孩正在上楼梯，楼梯有 n 阶台阶，小孩一次可以上 1 阶、2 阶或 3 阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模 1000000007。
#
# 示例 1：
#
#  输入：n = 3
#  输出：4
#  说明：有四种走法
# 示例 2：
#
#  输入：n = 5
#  输出：13
# 提示:
#
# n 范围在[1, 1000000]之间

N = 10 ** 6
MOD = 10 ** 9 + 7
dp = [0] * (N + 1)
dp[0] = dp[1] = 1
dp[2] = 2
for i in range(3, N + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD

class Solution:
    def waysToStep(self, n: int) -> int:
        return dp[n]



so = Solution()
print(so.waysToStep(3))




