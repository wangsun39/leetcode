# 你写下了若干 正整数 ，并将它们连接成了一个字符串 num 。但是你忘记给这些数字之间加逗号了。你只记得这一列数字是 非递减 的且 没有 任何数字有前导 0 。
#
# 请你返回有多少种可能的 正整数数组 可以得到字符串 num 。由于答案可能很大，将结果对 109 + 7 取余 后返回。
#
#
#
# 示例 1：
#
# 输入：num = "327"
# 输出：2
# 解释：以下为可能的方案：
# 3, 27
# 327
# 示例 2：
#
# 输入：num = "094"
# 输出：0
# 解释：不能有数字有前导 0 ，且所有数字均为正数。
# 示例 3：
#
# 输入：num = "0"
# 输出：0
# 解释：不能有数字有前导 0 ，且所有数字均为正数。
# 示例 4：
#
# 输入：num = "9999999999999"
# 输出：101
#
#
# 提示：
#
# 1 <= num.length <= 3500
# num 只含有数字 '0' 到 '9' 。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numberOfCombinations(self, num: str) -> int:
        MOD = 10 ** 9 + 7
        if num[0] == '0': return 0
        n = len(num)
        lcp = [[0] * n for _ in range(n)]  # lcp[i][j] 表示num[i:] 与num[j:]的最长公共前缀
        for i in range(n):
            lcp[i][i] = n - 1 - i
        for i in range(n - 2, -1, -1):
            for j in range(n - 1, i, -1):
                if num[i] == num[j]:
                    if j < n - 1:
                        lcp[i][j] = lcp[j][i] = lcp[i + 1][j + 1] + 1
                    else:
                        lcp[i][j] = lcp[j][i] = 1
                else:
                    lcp[i][j] = lcp[j][i] = 0

        dp = [[0] * n for _ in range(n)]  # dp[i][j] 表示最后一段为[i,j]的数字时，最多有多少种分割
        dp[0] = [1] * n
        ans = 1  # 完整的num
        for i in range(1, n):
            if num[i] == '0': continue
            s = 0  # 记录前缀和
            for j in range(i, n):
                if 2 * i - j - 1 >= 0:
                    # i...j  与  2i-j-1...i-1  比较
                    dp[i][j] = s
                    l1 = j - i + 1
                    l2 = lcp[i][2 * i - j - 1]
                    if l2 >= l1 or num[2 * i - j - 1 + l2] <= num[i + l2]:
                        dp[i][j] += dp[2 * i - j - 1][i - 1]
                    s += dp[2 * i - j - 1][i - 1]
                else:
                    dp[i][j] = s
                dp[i][j] %= MOD
                if j == n - 1:
                    ans += dp[i][j]

        return ans % MOD


so = Solution()
print(so.numberOfCombinations("1023"))   # 2
print(so.numberOfCombinations("1203"))   # 2
print(so.numberOfCombinations("327"))   # 2
print(so.numberOfCombinations("9999999999999"))   # 101



