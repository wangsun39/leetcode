# 某机械零部件上有一些不同规格的齿轮依次相连，ratio[i] 表示第 i 个齿轮的齿数。 某工程师为比较齿轮的实际转动值与理论值，将转动第 cnt 个齿轮 degree 度。 请返回所有齿轮的理论转动角度（反向转动为负角度）。
#
# 注意：
#
# 齿轮转动时，任意相邻的两个齿轮转动齿数相同，且方向相反。
# 示例 1：
#
# 输入：ratio = [10,15], cnt = 0, degree = 90
#
# 输出：[90,-60]
#
# 解释：
#
# 0 号齿轮齿数为 10，转动角度为 90 度；
#
# 位于其右侧的 1 号齿轮齿数为 15，随 0 号齿轮的转动，角度为 60，方向与 1 号齿轮相反；
#
# 示例 2：
#
# 输入：ratio = [3,6,10], cnt = 1, degree = 180
#
# 输出：[-360,180,-108]
#
# 解释： 1 号齿轮齿数为 6，转动角度为 180 度；
#
# 位于其左侧的 0 号齿轮齿数为 3，随 1 号齿轮的转动，角度为 360，方向与 1 号齿轮相反；
#
# 位于其右侧的 2 号齿轮齿数为 10，随 1 号齿轮的转动，角度为 108，方向与 1 号齿轮相反。
#
# 提示：
#
# 1 <= ratio.length <= 10^5
# 1 <= ratio[i] <= 10^6
# 0 <= cnt < ratio.length
# 1 <= degree <= 10^9
# 用例保证返回的每个齿轮的转动值均为整数，且其绝对值不超过 10^9
#
# 注意：竞赛中，请勿复制题面内容，以免影响您的竞赛成绩真实性。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def spinGears(self, ratio: List[int], cnt: int, degree: int) -> List[int]:
        n = len(ratio)
        ans = [0] * n
        ans[cnt] = degree
        for i in range(1, n):
            if cnt - i >= 0:
                ans[cnt - i] = -ans[cnt - i + 1] * ratio[cnt - i + 1] // ratio[cnt - i]
            if cnt + i < n:
                ans[cnt + i] = -ans[cnt + i - 1] * ratio[cnt + i - 1] // ratio[cnt + i]
        return ans


so = Solution()
print(so.spinGears(ratio = [10,15], cnt = 0, degree = 90))




