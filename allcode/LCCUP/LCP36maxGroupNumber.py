# 麻将的游戏规则中，共有两种方式凑成「一组牌」：
#
# 顺子：三张牌面数字连续的麻将，例如 [4,5,6]
# 刻子：三张牌面数字相同的麻将，例如 [10,10,10]
# 给定若干数字作为麻将牌的数值（记作一维数组 tiles），请返回所给 tiles 最多可组成的牌组数。
#
# 注意：凑成牌组时，每张牌仅能使用一次。
#
# 示例 1：
#
# 输入：tiles = [2,2,2,3,4]
#
# 输出：1
#
# 解释：最多可以组合出 [2,2,2] 或者 [2,3,4] 其中一组牌。
#
# 示例 2：
#
# 输入：tiles = [2,2,2,3,4,1,3]
#
# 输出：2
#
# 解释：最多可以组合出 [1,2,3] 与 [2,3,4] 两组牌。
#
# 提示：
#
# 1 <= tiles.length <= 10^5
# 1 <= tiles[i] <= 10^9

from leetcode.allcode.competition.mypackage import *

MAX = lambda a, b: b if b > a else a

class Solution:
    def maxGroupNumber(self, tiles: List[int]) -> int:
        tiles.sort()
        n = len(tiles)  # 按牌的种类排序
        # if n == 1: return tiles[0][1] // 3
        # if n == 2: return tiles[0][1] // 3 + tiles[1][1] // 3
        dp = [[[[-1] * 5 for _ in range(5)] for _ in range(5)] for _ in range(n)]
        dp[0][0][0][1] = 0  # i==0时， 只有这种为0，其他的都不存在为-1
        for i in range(1, n):
            for a in range(5):
                for b in range(5):
                    for c in range(5):
                        # 想办法利用 dp[i - 1][a][b][c] 来更新，dp[i] 的某些值
                        if tiles[i - 1] == tiles[i]:
                            # 在与前一张牌面相同时，相同的abc，在多出一张牌时，能够的得分一定不会变小
                            dp[i][a][b][c] = MAX(dp[i][a][b][c], dp[i - 1][a][b][c])

                            if c < 4:
                                # i 时，拥有 c + 1 张tiles[i]，与i -1 时，用c张tiles[i] 是等效的
                                dp[i][a][b][c + 1] = MAX(dp[i][a][b][c + 1], dp[i - 1][a][b][c])
                            if c > 2:
                                # c > 2 时，可以将c组成一个刻子
                                dp[i][a][b][c - 2] = MAX(dp[i][a][b][c - 2], dp[i - 1][a][b][c] + 1)
                            if min(a, b, c + 1) > 0:
                                # 在 dp[i - 1][a][b][c] 的基础上拿出一个a和一个b，再加上tiles[i]的c，组成一个顺子
                                dp[i][a - 1][b - 1][c] = MAX(dp[i][a - 1][b - 1][c], dp[i - 1][a][b][c] + 1)
                        elif tiles[i - 1] + 1 == tiles[i]:
                            dp[i][b][c][1] = MAX(dp[i][b][c][1], dp[i - 1][a][b][c])
                            if min(b, c) > 0:
                                dp[i][b - 1][c - 1][0] = MAX(dp[i][b - 1][c - 1][0], dp[i - 1][a][b][c])
                        elif tiles[i - 1] + 2 == tiles[i]:
                            dp[i][c][0][1] = MAX(dp[i][c][0][1], dp[i - 1][a][b][c])
                        else:
                            dp[i][0][0][1] = MAX(dp[i][0][0][1], dp[i - 1][a][b][c])

        ans = 0
        for a in range(5):
            for b in range(5):
                ans = MAX(ans, max(dp[-1][a][b]))
        return ans


so = Solution()
print(so.maxGroupNumber(tiles = [1,2,2,2,3,4,5]))
print(so.maxGroupNumber(tiles = [2,2,2,3,4]))




