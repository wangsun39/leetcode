# 元素的 频数 是该元素在一个数组中出现的次数。
#
# 给你一个整数数组 nums 和一个整数 k 。在一步操作中，你可以选择 nums 的一个下标，并将该下标对应元素的值增加 1 。
#
# 执行最多 k 次操作后，返回数组中最高频元素的 最大可能频数 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,4], k = 5
# 输出：3
# 解释：对第一个元素执行 3 次递增操作，对第二个元素执 2 次递增操作，此时 nums = [4,4,4] 。
# 4 是数组中最高频元素，频数是 3 。
# 示例 2：
#
# 输入：nums = [1,4,8,13], k = 5
# 输出：2
# 解释：存在多种最优解决方案：
# - 对第一个元素执行 3 次递增操作，此时 nums = [4,4,8,13] 。4 是数组中最高频元素，频数是 2 。
# - 对第二个元素执行 4 次递增操作，此时 nums = [1,8,8,13] 。8 是数组中最高频元素，频数是 2 。
# - 对第三个元素执行 5 次递增操作，此时 nums = [1,4,13,13] 。13 是数组中最高频元素，频数是 2 。
# 示例 3：
#
# 输入：nums = [3,9,6], k = 2
# 输出：1
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
# 1 <= k <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        s = list(accumulate(nums, initial=0))
        def calc(mx): # 若以最大值为mx， 那么mx的频数最大是几
            p = bisect_right(nums, mx)
            if mx * p - s[p] <= k:
                return p
            lo, hi = 0, p - 1
            while lo < hi - 1:
                mid = (lo + hi) // 2
                if mx * (p - mid) - (s[p] - s[mid]) <= k:
                    hi = mid
                else:
                    lo = mid
            return p - hi


        ans = 0
        for v in nums:
            ans = max(ans, calc(v))
        return ans


so = Solution()
print(so.maxFrequency(nums = [3,9,6], k = 2))
print(so.maxFrequency(nums = [1,2,4], k = 5))
print(so.maxFrequency(nums = [1,4,8,13], k = 5))




