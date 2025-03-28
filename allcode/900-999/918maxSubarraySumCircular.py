# 给定一个长度为 n 的环形整数数组 nums ，返回 nums 的非空 子数组 的最大可能和 。
#
# 环形数组 意味着数组的末端将会与开头相连呈环状。形式上， nums[i] 的下一个元素是 nums[(i + 1) % n] ， nums[i] 的前一个元素是 nums[(i - 1 + n) % n] 。
#
# 子数组 最多只能包含固定缓冲区 nums 中的每个元素一次。形式上，对于子数组 nums[i], nums[i + 1], ..., nums[j] ，不存在 i <= k1, k2 <= j 其中 k1 % n == k2 % n 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,-2,3,-2]
# 输出：3
# 解释：从子数组 [3] 得到最大和 3
# 示例 2：
#
# 输入：nums = [5,-3,5]
# 输出：10
# 解释：从子数组 [5,5] 得到最大和 5 + 5 = 10
# 示例 3：
#
# 输入：nums = [3,-2,2,-3]
# 输出：3
# 解释：从子数组 [3] 和 [3,-2,2] 都可以得到最大和 3
#
#
# 提示：
#
# n == nums.length
# 1 <= n <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104

from leetcode.allcode.competition.mypackage import *


class Solution:
    def maxSubarraySumCircular1(self, nums: List[int]) -> int:
        # 优先队列做法
        n = len(nums)
        nums = nums + nums
        s = list(accumulate(nums, initial=0))
        hq = [[0, 0]]
        heapify(hq)
        ans = -inf
        for i, x in enumerate(s[1:], 1):
            l = hq[0]
            mn, idx = l
            while i - idx > n:
                heappop(hq)
                l = hq[0]
                mn, idx = l
            ans = max(ans, x - mn)
            heappush(hq, [x, i])
        return ans

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_s = v = nums[0]  # 最大子段和
        for i, x in enumerate(nums[1:], 1):
            # v 表示以 x 结尾的最大子数组和
            if v <= 0:  # 当前面的和 <= 0，那么:如果最大和子数组包含x,就不会包含x前的任何值
                v = x
            else:
                v += x
            max_s = max(max_s, v)

        s = sum(nums)
        min_s = v = nums[0]  # 最小子段和，取一段最小和数组，剩下部分为答案
        for i, x in enumerate(nums[1:], 1):
            if v >= 0:
                v = x
            else:
                v += x
            min_s = min(min_s, v)
        if min_s == s: return max_s  # 这种情况说明nums全是负数，此时取max(nums)，为了避免计算可以直接用max_s
        ans = max(s - min_s, max_s)
        return ans


so = Solution()
print(so.maxSubarraySumCircular([-2]))
print(so.maxSubarraySumCircular([1,-2,3,-2]))
print(so.maxSubarraySumCircular([5,-3,5]))
print(so.maxSubarraySumCircular([3,-2,2,-3]))