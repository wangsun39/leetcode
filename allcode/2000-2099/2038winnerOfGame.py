# 总共有 n个颜色片段排成一列，每个颜色片段要么是'A'要么是'B'。给你一个长度为n的字符串colors，其中colors[i]表示第i个颜色片段的颜色。
#
# Alice 和 Bob 在玩一个游戏，他们 轮流从这个字符串中删除颜色。Alice 先手。
#
# 如果一个颜色片段为 'A'且 相邻两个颜色都是颜色 'A'，那么 Alice 可以删除该颜色片段。Alice不可以删除任何颜色'B'片段。
# 如果一个颜色片段为 'B'且 相邻两个颜色都是颜色 'B'，那么 Bob 可以删除该颜色片段。Bob 不可以删除任何颜色 'A'片段。
# Alice 和 Bob 不能从字符串两端删除颜色片段。
# 如果其中一人无法继续操作，则该玩家 输掉游戏且另一玩家 获胜。
# 假设 Alice 和 Bob 都采用最优策略，如果 Alice 获胜，请返回true，否则 Bob 获胜，返回false。
#
# 
#
# 示例 1：
#
# 输入：colors = "AAABABB"
# 输出：true
# 解释：
# AAABABB -> AABABB
# Alice 先操作。
# 她删除从左数第二个 'A' ，这也是唯一一个相邻颜色片段都是 'A' 的 'A' 。
#
# 现在轮到 Bob 操作。
# Bob 无法执行任何操作，因为没有相邻位置都是 'B' 的颜色片段 'B' 。
# 因此，Alice 获胜，返回 true 。
# 示例 2：
#
# 输入：colors = "AA"
# 输出：false
# 解释：
# Alice 先操作。
# 只有 2 个 'A' 且它们都在字符串的两端，所以她无法执行任何操作。
# 因此，Bob 获胜，返回 false 。
# 示例 3：
#
# 输入：colors = "ABBBBBBBAAA"
# 输出：false
# 解释：
# ABBBBBBBAAA -> ABBBBBBBAA
# Alice 先操作。
# 她唯一的选择是删除从右数起第二个 'A' 。
#
# ABBBBBBBAA -> ABBBBBBAA
# 接下来轮到 Bob 操作。
# 他有许多选择，他可以选择任何一个 'B' 删除。
#
# 然后轮到 Alice 操作，她无法删除任何片段。
# 所以 Bob 获胜，返回 false 。
# 
#
# 提示：
#
# 1 <=colors.length <= 105
# colors只包含字母'A'和'B'





from leetcode.allcode.competition.mypackage import *
# Definition for a binary tree node.
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        countA, countB = 0, 0
        N = len(colors)
        cur, curIdx = colors[0], 0
        for i in range(1, N):
            if colors[i] == cur:
                if i - curIdx > 1:
                    if cur == 'A':
                        countA += 1
                    if cur == 'B':
                        countB += 1
                continue
            curIdx, cur = i, colors[i]
        return countA > countB


so = Solution()
print(so.winnerOfGame("AAABABB"))
print(so.winnerOfGame("AA"))
print(so.winnerOfGame("ABBBBBBBAAA"))


