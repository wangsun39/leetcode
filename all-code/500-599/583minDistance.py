class Solution:
    def minDistance(self, word1, word2):
        r = len(word1)
        c = len(word2)
        d = [[0] * (c+1) for _ in range(r+1)]
        # d[i][j]表示word1的前i个字符和word2的前j个字符的minDistance
        for i in range(0, c+1):
            d[0][i] = i
        for i in range(0, r+1):
            d[i][0] = i
        for i in range(1, r+1):
            for j in range(1, c+1):
                if word1[i-1] == word2[j-1]:
                    d[i][j] = d[i-1][j-1]
                    continue
                d[i][j] = min(d[i][j-1], d[i-1][j]) + 1
        return d[r][c]


so = Solution()
print(so.minDistance("sea", "eat"))

