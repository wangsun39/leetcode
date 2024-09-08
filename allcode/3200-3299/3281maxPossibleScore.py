# 给你一个整数数组 start 和一个整数 d，代表 n 个区间 [start[i], start[i] + d]。
#
# 你需要选择 n 个整数，其中第 i 个整数必须属于第 i 个区间。所选整数的 得分 定义为所选整数两两之间的 最小 绝对差。
#
# 返回所选整数的 最大可能得分 。
#
#
#
# 示例 1：
#
# 输入： start = [6,0,3], d = 2
#
# 输出： 4
#
# 解释：
#
# 可以选择整数 8, 0 和 4 获得最大可能得分，得分为 min(|8 - 0|, |8 - 4|, |0 - 4|)，等于 4。
#
# 示例 2：
#
# 输入： start = [2,6,13,13], d = 5
#
# 输出： 5
#
# 解释：
#
# 可以选择整数 2, 7, 13 和 18 获得最大可能得分，得分为 min(|2 - 7|, |2 - 13|, |2 - 18|, |7 - 13|, |7 - 18|, |13 - 18|)，等于 5。
#
#
#
# 提示：
#
# 2 <= start.length <= 105
# 0 <= start[i] <= 109
# 0 <= d <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        diff = [q - p for p, q in pairwise(start)]
        def check(v):
            n = len(start)
            nums = start[:]
            for i, x in enumerate(nums[1:], 1):
                if x - nums[i - 1] > v: continue
                if x - nums[i - 1] + d < v: return False
                nums[i] = nums[i - 1] + v
            return True

        lo, hi = min(diff), start[-1] - start[0] + d + 1
        while lo < hi - 1:
            mid = (lo + hi) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid
        return lo



so = Solution()
print(so.maxPossibleScore(start = [6,0,3], d = 2))
print(so.maxPossibleScore(start = [2,6,13,13], d = 5))




