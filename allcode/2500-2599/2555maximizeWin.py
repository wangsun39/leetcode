# 在 X轴 上有一些奖品。给你一个整数数组 prizePositions ，它按照 非递减 顺序排列，其中 prizePositions[i] 是第 i 件奖品的位置。数轴上一个位置可能会有多件奖品。再给你一个整数 k 。
#
# 你可以选择两个端点为整数的线段。每个线段的长度都必须是 k 。你可以获得位置在任一线段上的所有奖品（包括线段的两个端点）。注意，两个线段可能会有相交。
#
# 比方说 k = 2 ，你可以选择线段 [1, 3] 和 [2, 4] ，你可以获得满足 1 <= prizePositions[i] <= 3 或者 2 <= prizePositions[i] <= 4 的所有奖品 i 。
# 请你返回在选择两个最优线段的前提下，可以获得的 最多 奖品数目。
#
#
#
# 示例 1：
#
# 输入：prizePositions = [1,1,2,2,3,3,5], k = 2
# 输出：7
# 解释：这个例子中，你可以选择线段 [1, 3] 和 [3, 5] ，获得 7 个奖品。
# 示例 2：
#
# 输入：prizePositions = [1,2,3,4], k = 0
# 输出：2
# 解释：这个例子中，一个选择是选择线段 [3, 3] 和 [4, 4] ，获得 2 个奖品。
#
#
# 提示：
#
# 1 <= prizePositions.length <= 105
# 1 <= prizePositions[i] <= 109
# 0 <= k <= 109
# prizePositions 有序非递减。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        counter = Counter(prizePositions)
        prize = sorted(counter.items())
        n = len(prize)
        right = [0] * n  # 从prize[i][0]开始向右长度为k的线段上的奖品数量
        r = 0
        cur = 0
        left = [0] * n # 记录 <= prize[r][0] 线段长度为k的奖品最大数量
        ans = 0
        for l in range(n):
            if l > 0:
                cur -= prize[l - 1][1]
            while r < n and prize[r][0] - prize[l][0] <= k:
                cur += prize[r][1]
                if r > 0:
                    left[r] = max(left[r - 1], cur)
                else:
                    left[r] = cur
                r += 1
            right[l] = cur
            if l > 0:
                ans = max(ans, right[l] + left[l - 1])
            else:
                ans = right[l]
        # print(prize)
        # print(left)
        # print(right)
        return ans








so = Solution()
print(so.maximizeWin(prizePositions = [1,1,2,2,3,3,5], k = 2))
print(so.maximizeWin(prizePositions = [1,2,3,4], k = 0))




