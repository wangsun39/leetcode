# 给出两个字符串 str1 和 str2，返回同时以 str1 和 str2 作为子序列的最短字符串。如果答案不止一个，则可以返回满足条件的任意一个答案。
#
# （如果从字符串 T 中删除一些字符（也可能不删除，并且选出的这些字符可以位于 T 中的 任意位置），可以得到字符串 S，那么 S 就是 T 的子序列）
#
#
#
# 示例：
#
# 输入：str1 = "abac", str2 = "cab"
# 输出："cabac"
# 解释：
# str1 = "abac" 是 "cabac" 的一个子串，因为我们可以删去 "cabac" 的第一个 "c"得到 "abac"。
# str2 = "cab" 是 "cabac" 的一个子串，因为我们可以删去 "cabac" 末尾的 "ac" 得到 "cab"。
# 最终我们给出的答案是满足上述属性的最短字符串。
#
#
# 提示：
#
# 1 <= str1.length, str2.length <= 1000
# str1 和 str2 都由小写英文字母组成。

from typing import List

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[0] * n for _ in range(m)]  # 以 str1[i] 和 str2[j] 结尾的最长公共子序列
        mx = 0
        x = y = 0
        for i in range(m):
            for j in range(n):
                if str1[i] == str2[j]:
                    if i > 0 and j > 0:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = 1
                else:
                    if i > 0 and j > 0:
                        dp[i][j] = dp[i - 1][j - 1]
                if i > 0 and dp[i][j] < dp[i - 1][j]:
                    dp[i][j] = dp[i - 1][j]
                if j > 0 and dp[i][j] < dp[i][j - 1]:
                    dp[i][j] = dp[i][j - 1]
                if dp[i][j] > mx:
                    mx = dp[i][j]
                    x, y = i, j
        print(dp)
        common = []  # 求出最长公共子序列
        for i in range(x, -1, -1):
            for j in range(y, -1, -1):
                if dp[i][j] == mx and str1[i] == str2[j]:
                    common.insert(0, str1[i])
                    y = j - 1
                    mx -= 1
                    break
            if mx == 0:
                break

        common = ''.join(common)
        print(common)
        ans = []
        i = j = k = 0
        # 把不在公共子序列中的字符加入答案
        while k < len(common):
            while str2[j] != common[k]:
                ans.append(str2[j])
                j += 1
            while str1[i] != common[k]:
                ans.append(str1[i])
                i += 1
            ans.append(common[k])
            i += 1
            k += 1
            j += 1
        while j < n:
            ans.append(str2[j])
            j += 1
        while i < m:
            ans.append(str1[i])
            i += 1
        return ''.join(ans)





obj = Solution()
print(obj.shortestCommonSupersequence("bbbaaaba","bbababbb"))
print(obj.shortestCommonSupersequence(str1 = "aa", str2 = "aa"))
print(obj.shortestCommonSupersequence(str1 = "abac", str2 = "cab"))

