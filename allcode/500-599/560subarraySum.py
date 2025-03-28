# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的连续子数组的个数 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,1,1], k = 2
# 输出：2
# 示例 2：
#
# 输入：nums = [1,2,3], k = 3
# 输出：2
#
#
# 提示：
#
# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107




from leetcode.allcode.competition.mypackage import *


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = 0  # 前缀和
        counter = Counter()  # 前缀和为为x的计数
        counter[0] = 1
        ans = 0
        for x in nums:
            s += x
            ans += counter[s - k]
            counter[s] += 1
        return ans

so = Solution()
print(so.subarraySum(nums = [1,1,1], k = 2))
print(so.subarraySum(nums = [1,2,3], k = 3))


