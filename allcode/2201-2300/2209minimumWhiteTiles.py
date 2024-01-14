# 给你一个下标从 0 开始的 二进制 字符串 floor ，它表示地板上砖块的颜色。
#
# floor[i] = '0' 表示地板上第 i 块砖块的颜色是 黑色 。
# floor[i] = '1' 表示地板上第 i 块砖块的颜色是 白色 。
# 同时给你 numCarpets 和 carpetLen 。你有 numCarpets 条 黑色 的地毯，每一条 黑色 的地毯长度都为 carpetLen 块砖块。请你使用这些地毯去覆盖砖块，使得未被覆盖的剩余 白色 砖块的数目 最小 。地毯相互之间可以覆盖。
#
# 请你返回没被覆盖的白色砖块的 最少 数目。
#
#
#
# 示例 1：
#
#
#
# 输入：floor = "10110101", numCarpets = 2, carpetLen = 2
# 输出：2
# 解释：
# 上图展示了剩余 2 块白色砖块的方案。
# 没有其他方案可以使未被覆盖的白色砖块少于 2 块。
# 示例 2：
#
#
#
# 输入：floor = "11111", numCarpets = 2, carpetLen = 3
# 输出：0
# 解释：
# 上图展示了所有白色砖块都被覆盖的一种方案。
# 注意，地毯相互之间可以覆盖。
#
#
# 提示：
#
# 1 <= carpetLen <= floor.length <= 1000
# floor[i] 要么是 '0' ，要么是 '1' 。
# 1 <= numCarpets <= 1000

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        f = [[0] * n for _ in range(n)]  # f[i][j] 表示用一个地毯覆盖 floor[i: j + 1]，最多盖住多少块白色
        g = [[0] * n for _ in range(n)]  # g[i][j] 表示 floor[i: j + 1] 中有多少白色块
        for i in range(n):
            mx = 0
            cur = 0
            for j in range(i, n):
                if j - carpetLen >= 0:
                    cur += ((floor[j] == '1') - (floor[j - carpetLen] == '1'))
                else:
                    cur += (floor[j - carpetLen] == '1')
                mx = max(mx, cur)
                f[i][j] = mx
                if j == i:
                    g[i][j] = floor[j] == '1'
                else:
                    g[i][j] += g[i][j - 1] + (floor[j] == '1')

        # dp = [[0] * carpetLen for _ in range(n)]  # 用j个地毯覆盖 floor[:i + 1]，最多能盖住多少白色砖块

        @cache
        def dfs(i, j):  # 用j个地毯覆盖 floor[:i + 1]，最多能盖住多少白色砖块
            if j == 0: return 0
            if i == 0: return floor[i] == '1'
            if j == 1: return f[0][i]
            if carpetLen * j >= i + 1:
                r = min(carpetLen * j - 1, i)
                return g[0][r]
            mx = 0
            for k in range(i + 1):
                if k < i:
                    mx = max(mx, dfs(k, j - 1) + f[k + 1][i])
                else:
                    mx = max(mx, dfs(k, j - 1))
            # print(i, j, mx)
            return mx

        return g[0][n - 1] - dfs(n - 1, numCarpets)


so = Solution()
print(so.minimumWhiteTiles(floor = "11111", numCarpets = 2, carpetLen = 3))
print(so.minimumWhiteTiles(floor = "10110101", numCarpets = 2, carpetLen = 2))




