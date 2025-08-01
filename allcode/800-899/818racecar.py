# 你的赛车可以从位置 0 开始，并且速度为 +1 ，在一条无限长的数轴上行驶。赛车也可以向负方向行驶。赛车可以按照由加速指令 'A' 和倒车指令 'R' 组成的指令序列自动行驶。
# 当收到指令 'A' 时，赛车这样行驶：
# position += speed
# speed *= 2
# 当收到指令 'R' 时，赛车这样行驶：
# 如果速度为正数，那么speed = -1
# 否则 speed = 1
# 当前所处位置不变。
# 例如，在执行指令 "AAR" 后，赛车位置变化为 0 --> 1 --> 3 --> 3 ，速度变化为 1 --> 2 --> 4 --> -1 。
#
# 给你一个目标位置 target ，返回能到达目标位置的最短指令序列的长度。
#
#
#
# 示例 1：
#
# 输入：target = 3
# 输出：2
# 解释：
# 最短指令序列是 "AA" 。
# 位置变化 0 --> 1 --> 3 。
# 示例 2：
#
# 输入：target = 6
# 输出：5
# 解释：
# 最短指令序列是 "AAARA" 。
# 位置变化 0 --> 1 --> 3 --> 7 --> 7 --> 6 。
#
#
# 提示：
#
# 1 <= target <= 104


from leetcode.allcode.competition.mypackage import *


class Solution:
    def racecar(self, target: int) -> int:
        dp = [0] * max(target + 1, 4)
        dp[1] = 1
        dp[2] = 4
        dp[3] = 2
        if target < 4: return dp[target]
        k = 3
        for i in range(4, target + 1):
            if i == 2 ** k - 1:
                dp[i] = k
                k += 1
                continue
            dp[i] = dp[2 ** k - 1 - i] + k + 1 # 先走到 2 ** k - 1，再回头走 2 ** k - 1 - i
            # 以下循环表示，先走到 2 ** (k - 1) - 1，再回头走 2 ** j - 1，再回头
            for j in range(k):
                if 2 ** j - 1 >= i: break
                dp[i] = min(dp[i], k - 1 + 1 + j + 1 + dp[i - (2 ** (k - 1) - 1 - (2 ** j - 1))])

        return dp[-1]

so = Solution()
print(so.racecar(4))

