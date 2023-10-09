# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
#
# 你可以对一个单词进行如下三种操作：
#
# 插入一个字符
# 删除一个字符
# 替换一个字符
#  
#
# 示例 1：
#
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
# 示例 2：
#
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
#  
#
# 提示：
#
# 0 <= word1.length, word2.length <= 500
# word1 和 word2 由小写英文字母组成


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def helper(start1, start2):
            if (start1, start2) in pair_dict:
                return pair_dict[(start1, start2)]
            if N2 == start2:
                pair_dict[(start1, start2)] = N1 - start1
                return N1 - start1
            if N1 == start1:
                pair_dict[(start1, start2)] = N2 - start2
                return N2 - start2
            res = 1 + helper(start1, start2 + 1)
            for i, e in enumerate(word1[start1:]):
                if e == word2[start2]:
                    res = min(res, i + helper(start1 + i + 1, start2 + 1))
                else:
                    res = min(res, i + 1 + helper(start1 + i + 1, start2 + 1))
            pair_dict[(start1, start2)] = res
            return res
        N1, N2 = len(word1), len(word2)
        pair_dict = {}

        return helper(0, 0)

    def minDistance(self, word1: str, word2: str) -> int:
        N1, N2 = len(word1), len(word2)
        dp = [[0 for _ in range(N1+1)] for _ in range(N2+1)]
        for i in range(N1 + 1):
            dp[0][i] = i
        for i in range(N2 + 1):
            dp[i][0] = i
        for i in range(1, N1 + 1):
            for j in range(1, N2 + 1):
                if word1[i-1] == word2[j-1]:
                    dp[j][i] = dp[j-1][i-1]
                else:
                    dp[j][i] = min(dp[j - 1][i - 1], dp[j-1][i], dp[j][i-1]) + 1
        # print(dp)
        return dp[N2][N1]




so = Solution()
print(so.minDistance("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdef",
"bcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefg"))  # 2
print(so.minDistance("rs", "ro"))  # 1
print(so.minDistance("horse", "ros"))  # 3
print(so.minDistance("intention", "execution"))  # 5
