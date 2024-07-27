# 在一座城市里，你需要建 n 栋新的建筑。这些新的建筑会从 1 到 n 编号排成一列。
#
# 这座城市对这些新建筑有一些规定：
#
# 每栋建筑的高度必须是一个非负整数。
# 第一栋建筑的高度 必须 是 0 。
# 任意两栋相邻建筑的高度差 不能超过  1 。
# 除此以外，某些建筑还有额外的最高高度限制。这些限制会以二维整数数组 restrictions 的形式给出，其中 restrictions[i] = [idi, maxHeighti] ，表示建筑 idi 的高度 不能超过 maxHeighti 。
#
# 题目保证每栋建筑在 restrictions 中 至多出现一次 ，同时建筑 1 不会 出现在 restrictions 中。
#
# 请你返回 最高 建筑能达到的 最高高度 。
#
#
#
# 示例 1：
#
#
# 输入：n = 5, restrictions = [[2,1],[4,1]]
# 输出：2
# 解释：上图中的绿色区域为每栋建筑被允许的最高高度。
# 我们可以使建筑高度分别为 [0,1,2,1,2] ，最高建筑的高度为 2 。
# 示例 2：
#
#
# 输入：n = 6, restrictions = []
# 输出：5
# 解释：上图中的绿色区域为每栋建筑被允许的最高高度。
# 我们可以使建筑高度分别为 [0,1,2,3,4,5] ，最高建筑的高度为 5 。
# 示例 3：
#
#
# 输入：n = 10, restrictions = [[5,3],[2,5],[7,4],[10,3]]
# 输出：5
# 解释：上图中的绿色区域为每栋建筑被允许的最高高度。
# 我们可以使建筑高度分别为 [0,1,2,3,3,4,4,5,4,3] ，最高建筑的高度为 5 。
#
#
# 提示：
#
# 2 <= n <= 109
# 0 <= restrictions.length <= min(n - 1, 105)
# 2 <= idi <= n
# idi 是 唯一的 。
# 0 <= maxHeighti <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.sort()
        restrictions.insert(0, [1, 0])
        mx_hi = [[1, 0]]  # 计算每个限制点实际最高的建筑高度，需要从左到右，再从右到左一共计算两轮
        for i in range(1, len(restrictions)):
            idx1, mx1 = mx_hi[i - 1]
            idx2, mx2 = restrictions[i]
            cur = min(idx2 - idx1 + mx1, mx2)
            mx_hi.append([idx2, cur])

        for i in range(len(restrictions) - 2, -1, -1):
            idx1, mx1 = mx_hi[i]
            idx2, mx2 = mx_hi[i + 1]
            cur = min(mx1, mx2 + (idx2 - idx1))
            mx_hi[i][1] = cur

        if restrictions[-1][0] != n:
            cur = mx_hi[-1][1] + n - mx_hi[-1][0]
            mx_hi.append([n, cur])

        ans = max(x for _, x in mx_hi)

        for i in range(1, len(mx_hi)):  # 计算在两个限制建筑之间能不能有更高的建筑
            idx1, mx1 = mx_hi[i - 1]
            idx2, mx2 = mx_hi[i]
            mn, mx = min(mx1, mx2), max(mx1, mx2)
            if mx - mn < idx2 - idx1:
                ans = max(ans, ((idx2 - idx1) - (mx - mn)) // 2 + mx)
        return ans




so = Solution()
print(so.maxBuilding(n = 10, restrictions = [[8,5],[9,0],[6,2],[4,0],[3,2],[10,0],[5,3],[7,3],[2,4]]))  # 2
print(so.maxBuilding(n = 6, restrictions = []))  # 5
print(so.maxBuilding(n = 5, restrictions = [[2,1],[4,1]]))  # 2
print(so.maxBuilding(n = 10, restrictions = [[5,3],[2,5],[7,4],[10,3]]))  # 5




