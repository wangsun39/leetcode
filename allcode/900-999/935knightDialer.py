# 象棋骑士有一个独特的移动方式，它可以垂直移动两个方格，水平移动一个方格，或者水平移动两个方格，垂直移动一个方格(两者都形成一个 L 的形状)。
#
# 象棋骑士可能的移动方式如下图所示:
#
#
#
# 我们有一个象棋骑士和一个电话垫，如下所示，骑士只能站在一个数字单元格上(即蓝色单元格)。
#
#
#
# 给定一个整数 n，返回我们可以拨多少个长度为 n 的不同电话号码。
#
# 你可以将骑士放置在任何数字单元格上，然后你应该执行 n - 1 次移动来获得长度为 n 的号码。所有的跳跃应该是有效的骑士跳跃。
#
# 因为答案可能很大，所以输出答案模 109 + 7.
#
#
#
# 示例 1：
#
# 输入：n = 1
# 输出：10
# 解释：我们需要拨一个长度为1的数字，所以把骑士放在10个单元格中的任何一个数字单元格上都能满足条件。
# 示例 2：
#
# 输入：n = 2
# 输出：20
# 解释：我们可以拨打的所有有效号码为[04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]
# 示例 3：
#
# 输入：n = 3131
# 输出：136006598
# 解释：注意取模
#
#
# 提示：
#
# 1 <= n <= 5000


class Solution:
    def knightDialer1(self, N: int):
        if 1 == N:
            return 10
        self.nextNums = {1: {6, 8}, 2: {7, 9}, 3: {4, 8}, 4: {3, 9, 0}, 5: set(), 6: {1, 7, 0}, 7: {2, 6}, 8: {1, 3}, 9: {2, 4}, 0: {4, 6}}
        nDict_pre = {i: 1 for i in range(10)}
        for j in range(N-1):
            nDict_cur = {i: 0 for i in range(10)}
            for key in nDict_pre:
                for i in self.nextNums[key]:
                    nDict_cur[i] += nDict_pre[key]
                    nDict_cur[i] %= 1000000007
            nDict_pre = nDict_cur
        res = 0
        for i in nDict_cur:
            res += nDict_cur[i]
        return res % 1000000007

    def knightDialer(self, N: int) -> int:
        # 2024/12/10
        MOD = 10 ** 9 + 7
        if 1 == N:
            return 10
        nextNums = {1: {6, 8}, 2: {7, 9}, 3: {4, 8}, 4: {3, 9, 0}, 5: set(), 6: {1, 7, 0}, 7: {2, 6}, 8: {1, 3}, 9: {2, 4}, 0: {4, 6}}
        dp1 = [1] * 10
        for i in range(N - 1):
            dp2 = [0] * 10
            for k, v in nextNums.items():
                for x in v:
                    dp2[x] += dp1[k]
                    dp2[x] %= MOD
            dp1 = dp2[:]
        return sum(dp1) % MOD

so = Solution()
print(so.knightDialer(3))
print(so.knightDialer(3660))
'''so.knightDialer(3)
so.knightDialer(4)
so.knightDialer(5)'''
