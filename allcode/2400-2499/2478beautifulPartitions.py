# 给你一个字符串 s ，每个字符是数字 '1' 到 '9' ，再给你两个整数 k 和 minLength 。
#
# 如果对 s 的分割满足以下条件，那么我们认为它是一个 完美 分割：
#
# s 被分成 k 段互不相交的子字符串。
# 每个子字符串长度都 至少 为 minLength 。
# 每个子字符串的第一个字符都是一个 质数 数字，最后一个字符都是一个 非质数 数字。质数数字为 '2' ，'3' ，'5' 和 '7' ，剩下的都是非质数数字。
# 请你返回 s 的 完美 分割数目。由于答案可能很大，请返回答案对 109 + 7 取余 后的结果。
#
# 一个 子字符串 是字符串中一段连续字符串序列。
#
#
#
# 示例 1：
#
# 输入：s = "23542185131", k = 3, minLength = 2
# 输出：3
# 解释：存在 3 种完美分割方案：
# "2354 | 218 | 5131"
# "2354 | 21851 | 31"
# "2354218 | 51 | 31"
# 示例 2：
#
# 输入：s = "23542185131", k = 3, minLength = 3
# 输出：1
# 解释：存在一种完美分割方案："2354 | 218 | 5131" 。
# 示例 3：
#
# 输入：s = "3312958", k = 3, minLength = 1
# 输出：1
# 解释：存在一种完美分割方案："331 | 29 | 58" 。
#
#
# 提示：
#
# 1 <= k, minLength <= s.length <= 1000
# s 每个字符都为数字 '1' 到 '9' 之一。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        MOD = int(1e9 + 7)
        n = len(s)
        if s[0] not in '2357' or s[-1] in '2357':
            return 0
        A = [0]  # 所有可能的分界点
        for i in range(n - 1):
            if s[i] not in '2357' and s[i + 1] in '2357':
                A.append(i)
        A.append(n - 1)
        m = len(A)
        print(A)
        dp = [[0] * m for _ in range(k)]  # dp[i][j] 表示 s[:A[:j+1]]中分i+1段的最大数量
        for i in range(1, m):
            if A[i] + 1 >= minLength:
                dp[0][i] = 1
        for i in range(1, k):
            ss = 0  # 前缀和
            idx = 0  # 前缀和加到了idx项
            for j in range(1, m):
                for t in range(idx, j):
                    if A[j] - A[t] >= minLength:
                        ss += dp[i - 1][t]
                        ss %= MOD
                        idx += 1
                dp[i][j] = ss
        print(dp)
        return dp[-1][-1]

so = Solution()
print(so.beautifulPartitions(s = "22", k = 1, minLength = 1))  # 0
print(so.beautifulPartitions(s = "3312958", k = 3, minLength = 1))  # 1
print(so.beautifulPartitions(s = "23542185131", k = 3, minLength = 2))  # 3
print(so.beautifulPartitions(s = "23542185131", k = 3, minLength = 3))  # 1




