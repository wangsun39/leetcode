# 有两种形状的瓷砖：一种是 2 x 1 的多米诺形，另一种是形如 "L" 的托米诺形。两种形状都可以旋转。
#
#
#
# 给定整数 n ，返回可以平铺 2 x n 的面板的方法的数量。返回对 109 + 7 取模 的值。
#
# 平铺指的是每个正方形都必须有瓷砖覆盖。两个平铺不同，当且仅当面板上有四个方向上的相邻单元中的两个，使得恰好有一个平铺有一个瓷砖占据两个正方形。
#
#
#
# 示例 1:
#
#
#
# 输入: n = 3
# 输出: 5
# 解释: 五种不同的方法如上所示。
# 示例 2:
#
# 输入: n = 1
# 输出: 1
#
#
# 提示：
#
# 1 <= n <= 1000

class Solution:
    def numTilings(self, n: int) -> int:
        f, g = [0] * n, [0] * n
        MOD = int(1e9) + 7
        f[0], g[0] = 1, 0
        if n > 1: f[1], g[1] = 2, 1
        for i in range(2, n):
            f[i] = f[i - 1] + f[i - 2] + g[i - 1] * 2
            f[i] %= MOD
            g[i] = f[i - 2] + g[i - 1]
            g[i] %= MOD
        return f[-1]



so = Solution()
print(so.numTilings(4))
print(so.numTilings(3))
print(so.numTilings(1))

