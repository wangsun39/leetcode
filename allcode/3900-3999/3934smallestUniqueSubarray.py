# 给你一个整数数组 nums 。
#
# 找出 nums 中与其他任何 子数组 均 不 相同 的 子数组 的 最小 长度。
#
# 返回一个整数，表示此类 子数组 的 最小可能长度 。
#
# 子数组 是数组中的一个连续的非空元素序列。
#
# 如果两个 子数组 具有相同的长度，并且对应位置的元素也相同，则认为这两个 子数组 是相同的。
#
#
#
# 示例 1：
#
# 输入： nums = [3,3,3]
#
# 输出： 3
#
# 解释：
#
# 长度为 1 的子数组：[3] → 出现 3 次
# 长度为 2 的子数组：[3, 3] → 出现 2 次
# 长度为 3 的子数组：[3, 3, 3] → 出现 1 次
# 子数组 [3, 3, 3] 是唯一的，因此最小唯一子数组的长度为 3。
#
# 示例 2：
#
# 输入： nums = [2,1,2,3,3]
#
# 输出： 1
#
# 解释：
#
# 长度为 1 的子数组：
#
# [2] → 出现 2 次
# [1] → 出现 1 次
# [3] → 出现 2 次
# 子数组 [1] 是唯一的，因此最小唯一子数组的长度为 1。
# 示例 3：
#
# 输入： nums = [1,1,2,2,1]
#
# 输出： 2
#
# 解释：
#
# 长度为 1 的子数组：
#
# [1] → 出现 3 次
# [2] → 出现 2 次
# 长度为 2 的子数组：
#
# [1, 1] → 出现 1 次
# [1, 2] → 出现 1 次
# [2, 2] → 出现 1 次
# [2, 1] → 出现 1 次
# 至少有一个长度为 2 的子数组是唯一的，因此最小唯一子数组的长度为 2。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        MOD1 = 10**9 + 7
        MOD2 = 10**9 + 9
        BASE = 10**5 + 3

        def check(val: int) -> bool:
            if val == 0:
                return False

            hash1 = hash2 = 0
            for i in range(val):
                hash1 = (hash1 * BASE + nums[i]) % MOD1
                hash2 = (hash2 * BASE + nums[i]) % MOD2

            base_k1 = base_k2 = 1
            for i in range(val):
                base_k1 = (base_k1 * BASE) % MOD1
                base_k2 = (base_k2 * BASE) % MOD2

            count = defaultdict(int)
            count[(hash1, hash2)] += 1

            for i in range(val, n):
                hash1 = (hash1 * BASE - nums[i - val] * base_k1 + nums[i]) % MOD1
                hash2 = (hash2 * BASE - nums[i - val] * base_k2 + nums[i]) % MOD2
                count[(hash1, hash2)] += 1

            return 1 in count.values()

        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left


so = Solution()
print(so.smallestUniqueSubarray([3,3,3]))




