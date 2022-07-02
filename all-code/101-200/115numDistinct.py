class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.calced_pair = {}  # 记录曾经计算过的[len(s), len(t)]的对的距离
    def numDistinct(self, s: str, t: str) -> int:
        len1 = len(s)
        len2 = len(t)
        if len1 == 0 or len2 == 0:
            return 0
        if str(s) + "_" + str(t) in self.calced_pair:
            return self.calced_pair[str(s) + "_" + str(t)]
        total_num = 0
        for i in range(len1):
            if s[i] == t[0]:
                if 1 == len2:
                    total_num += 1
                else:
                    total_num += self.numDistinct(s[i+1:], t[1:])
        self.calced_pair[str(s) + "_" + str(t)] = total_num
        return total_num

class Solution1:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        if m == 0 or n == 0 or m < n:
            return 0
        # 动态规划，M[j][i]记录s[:j]和t[:i]的numDistinct
        M = [[0] * n for _ in range(m)]
        M[0][0] = 1 if s[0] == t[0] else 0
        for i in range(1, m):
            if s[i] == t[0]:
                M[i][0] = M[i-1][0] + 1
            else:
                M[i][0] = M[i - 1][0]
        for i in range(1, n):
            for j in range(i, m):
                if s[j] != t[i]:
                    M[j][i] = M[j-1][i]
                else:
                    M[j][i] = M[j-1][i] + M[j-1][i-1]
        print(M)
        return M[-1][-1]

so = Solution()
print(so.numDistinct("rabbbit", "rabbit"))
print(so.numDistinct("babgbag", "bag"))

so = Solution1()
print(so.numDistinct("rabbbit", "rabbit"))
print(so.numDistinct("babgbag", "bag"))
