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

class Solution:
    def maxGroupNumber(self, tiles: List[int]) -> int:
        counter = Counter(tiles)
        tiles = [[k, v] for k, v in counter.items()]
        tiles.sort()
        n = len(tiles)  # 按牌的种类排序
        if n == 1: return tiles[0][1] // 3
        if n == 2: return tiles[0][1] // 3 + tiles[1][1] // 3
        dp = [[[[0] * 5 for _ in range(5)] for _ in range(5)] for _ in range(n)]
        # dp[i][a][b][c]  表示处理到第i种牌时，牌面为 tiles[i][0]-2,tiles[i][0]-1,tiles[i][0] 的牌的数量分别为a/b/c张时，总得分最大值
        if tiles[0][0] + 1 == tiles[1][0]:
            for i in range(min(tiles[0][1], 5)):
                dp[0][0][0][i] = tiles[0][1] // 3
                for j in range(min(tiles[1][1], 5)):
                    dp[1][0][i][j] = tiles[0][1] // 3 + tiles[1][1] // 3
        else:
            for i in range(min(tiles[1][1], 5)):
                dp[1][0][0][i] = tiles[1][1] // 3

        for i in range(2, n):
            if tiles[i - 1][0] + 1 != tiles[i][0]:
                for c in range(min(tiles[i][1], 5)):
                    dp[1][0][0][c] = tiles[i][1] // 3



so = Solution()
print(so.maxGroupNumber(tiles = [2,2,2,3,4]))




