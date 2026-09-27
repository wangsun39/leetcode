# 力扣嘉年华为了确保更舒适的游览环境条件，在会场的各处设置了湿度调节装置，这些调节装置受控于总控室中的一台控制器。 控制器中已经预设了一些调节指令，整数数组operate[i] 表示第 i 条指令增加空气湿度的大小。现在你可以将任意数量的指令修改为降低湿度（变化的数值不变），以确保湿度尽可能的适宜：
#
# 控制器会选择 一段连续的指令 ，从而进行湿度调节的操作；
# 这段指令最终对湿度影响的绝对值，即为当前操作的「不适宜度」
# 在控制器所有可能的操作中，最大 的「不适宜度」即为「整体不适宜度」
# 请返回在所有修改指令的方案中，可以得到的 最小 「整体不适宜度」。
#
# 示例 1：
#
# 输入：operate = [5,3,7]
#
# 输出：8
#
# 解释：对于方案 2 的 [5,3,-7] 操作指令 [5],[3],[-7] 的「不适宜度」分别为 5,3,7 操作指令 [5,3],[3,-7] 的「不适宜度」分别为 8,4 操作指令 [5,3,-7] 的「不适宜度」为 1， 因此对于方案 [5,3,-7]的「整体不适宜度」为 8，其余方案的「整体不适宜度」均不小于 8，如下表所示：image.png
#
# 示例 2：
#
# 输入：operate = [20,10]
#
# 输出：20
#
# 提示：
#
# 1 <= operate.length <= 1000
# 1 <= operate[i] <= 1000

from leetcode.allcode.competition.mypackage import *

class Solution:
    def unSuitability(self, operate: List[int]) -> int:
        n = len(operate)
        mx = max(operate) * 2   #  答案的上界
        dp = [[inf] * (mx + 1) for _ in range(n)]   # 前i项，通过正负号调整，使得 operate[i] 与前i项最小值的差值为 j的最小不舒适度
        dp[0][operate[0]] = operate[0]
        for i, x in enumerate(operate[1:], 1):
            for j in range(mx + 1):   # 枚举前i-1个数经过代数和后，第 i - 1 项的相对之前最低点的位置
                if j + x <= mx:
                    if j + x < dp[i - 1][j]:
                        dp[i][x + j] = min(dp[i][x + j], dp[i - 1][j])
                    else:
                        dp[i][x + j] = min(dp[i][x + j], j + x)
                if j - x >= 0:
                    dp[i][j - x] = min(dp[i][j - x], dp[i - 1][j])
                elif dp[i - 1][j] + (x - j) <= mx:  #  超过 mx 就没有必要更新 dp[i][0]
                    dp[i][0] = min(dp[i][0], dp[i - 1][j] + (x - j))

        return min(dp[-1])



so = Solution()
print(so.unSuitability([5,3,7]))
