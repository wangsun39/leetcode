# 你的音乐播放器里有 n 首不同的歌，在旅途中，你计划听 goal 首歌（不一定不同，即，允许歌曲重复）。你将会按如下规则创建播放列表：
#
# 每首歌 至少播放一次 。
# 一首歌只有在其他 k 首歌播放完之后才能再次播放。
# 给你 n、goal 和 k ，返回可以满足要求的播放列表的数量。由于答案可能非常大，请返回对 109 + 7 取余 的结果。
#
#
# 示例 1：
#
# 输入：n = 3, goal = 3, k = 1
# 输出：6
# 解释：有 6 种可能的播放列表。[1, 2, 3]，[1, 3, 2]，[2, 1, 3]，[2, 3, 1]，[3, 1, 2]，[3, 2, 1] 。
# 示例 2：
#
# 输入：n = 2, goal = 3, k = 0
# 输出：6
# 解释：有 6 种可能的播放列表。[1, 1, 2]，[1, 2, 1]，[2, 1, 1]，[2, 2, 1]，[2, 1, 2]，[1, 2, 2] 。
# 示例 3：
#
# 输入：n = 2, goal = 3, k = 1
# 输出：2
# 解释：有 2 种可能的播放列表。[1, 2, 1]，[2, 1, 2] 。
#
#
# 提示：
#
# 0 <= k < n <= goal <= 100

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * n for _ in range(goal)]  # 听的前i首歌中，一共有j+1首不同的可能为dp[i][j]
        dp[0][0] = n
        for i in range(1, goal):
            for j in range(n):
                dp[i][j] += dp[i - 1][j] * max(0, j + 1 - k)  # 前i-1首中，已经有j+1首不同了，那最近的k首都不能再选
                if j:
                    dp[i][j] += dp[i - 1][j - 1] * (n - j)  # 前i-1首中，有j首不同，那可以从n-j中再选一首
                dp[i][j] %= MOD
        return dp[-1][-1]


so = Solution()
print(so.numMusicPlaylists(n = 3, goal = 3, k = 1))
print(so.numMusicPlaylists(n = 1, goal = 2, k = 0))




