# 给你一个下标从 0 开始的整数数组 nums 和一个整数 p 。请你从 nums 中找到 p 个下标对，每个下标对对应数值取差值，你需要使得这 p 个差值的 最大值 最小。同时，你需要确保每个下标在这 p 个下标对中最多出现一次。
#
# 对于一个下标对 i 和 j ，这一对的差值为 |nums[i] - nums[j]| ，其中 |x| 表示 x 的 绝对值 。
#
# 请你返回 p 个下标对对应数值 最大差值 的 最小值 。
#
#
#
# 示例 1：
#
# 输入：nums = [10,1,2,7,1,3], p = 2
# 输出：1
# 解释：第一个下标对选择 1 和 4 ，第二个下标对选择 2 和 5 。
# 最大差值为 max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1 。所以我们返回 1 。
# 示例 2：
#
# 输入：nums = [4,2,1,2], p = 1
# 输出：0
# 解释：选择下标 1 和 3 构成下标对。差值为 |2 - 2| = 0 ，这是最大差值的最小值。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109
# 0 <= p <= (nums.length)/2

from leetcode.allcode.competition.mypackage import *


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0: return 0
        nums.sort()
        n = len(nums)

        def check(m):
            num = 0
            i = 0
            while i + 1 < n:
                if nums[i + 1] - nums[i] <= m:
                    num += 1
                    if num >= p:
                        return True
                    i += 2
                else:
                    i += 1
            return False

        lo, hi = 0, nums[-1] - nums[0]
        if check(lo): return lo
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid
        return lo + 1


so = Solution()
print(so.minimizeMax(nums = [0,5,3,4], p = 0))
print(so.minimizeMax(nums = [10,1,2,7,1,3], p = 0))
print(so.minimizeMax(nums = [4,2,1,2], p = 1))




