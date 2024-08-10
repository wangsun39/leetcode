# 给你一个整数 n ，表示在一个游戏中的玩家数目。同时给你一个二维整数数组 pick ，其中 pick[i] = [xi, yi] 表示玩家 xi 获得了一个颜色为 yi 的球。
#
# 如果玩家 i 获得的球中任何一种颜色球的数目 严格大于 i 个，那么我们说玩家 i 是胜利玩家。换句话说：
#
# 如果玩家 0 获得了任何的球，那么玩家 0 是胜利玩家。
# 如果玩家 1 获得了至少 2 个相同颜色的球，那么玩家 1 是胜利玩家。
# ...
# 如果玩家 i 获得了至少 i + 1 个相同颜色的球，那么玩家 i 是胜利玩家。
# 请你返回游戏中 胜利玩家 的数目。
#
# 注意，可能有多个玩家是胜利玩家。
#
#
#
# 示例 1：
#
# 输入：n = 4, pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]
#
# 输出：2
#
# 解释：
#
# 玩家 0 和玩家 1 是胜利玩家，玩家 2 和玩家 3 不是胜利玩家。
#
# 示例 2：
#
# 输入：n = 5, pick = [[1,1],[1,2],[1,3],[1,4]]
#
# 输出：0
#
# 解释：
#
# 没有胜利玩家。
#
# 示例 3：
#
# 输入：n = 5, pick = [[1,1],[2,4],[2,4],[2,4]]
#
# 输出：1
#
# 解释：
#
# 玩家 2 是胜利玩家，因为玩家 2 获得了 3 个颜色为 4 的球。
#
#
#
# 提示：
#
# 2 <= n <= 10
# 1 <= pick.length <= 100
# pick[i].length == 2
# 0 <= xi <= n - 1
# 0 <= yi <= 10

from leetcode.allcode.competition.mypackage import *

class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        counter = defaultdict(Counter)
        for i, j in pick:
            counter[i][j] += 1
        ans = 0
        for i, c in counter.items():
            if any(x > i for x in c.values()):
                ans += 1
        return ans



so = Solution()
print(so.winningPlayerCount(n = 4, pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]))
print(so.winningPlayerCount(n = 5, pick = [[1,1],[1,2],[1,3],[1,4]]))
print(so.winningPlayerCount(n = 5, pick = [[1,1],[2,4],[2,4],[2,4]]))




