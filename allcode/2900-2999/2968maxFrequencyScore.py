# 给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。
#
# 你可以对数组执行 至多 k 次操作：
#
# 从数组中选择一个下标 i ，将 nums[i] 增加 或者 减少 1 。
# 最终数组的频率分数定义为数组中众数的 频率 。
#
# 请你返回你可以得到的 最大 频率分数。
#
# 众数指的是数组中出现次数最多的数。一个元素的频率指的是数组中这个元素的出现次数。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,6,4], k = 3
# 输出：3
# 解释：我们可以对数组执行以下操作：
# - 选择 i = 0 ，将 nums[0] 增加 1 。得到数组 [2,2,6,4] 。
# - 选择 i = 3 ，将 nums[3] 减少 1 ，得到数组 [2,2,6,3] 。
# - 选择 i = 3 ，将 nums[3] 减少 1 ，得到数组 [2,2,6,2] 。
# 元素 2 是最终数组中的众数，出现了 3 次，所以频率分数为 3 。
# 3 是所有可行方案里的最大频率分数。
# 示例 2：
#
# 输入：nums = [1,4,4,2,4], k = 0
# 输出：3
# 解释：我们无法执行任何操作，所以得到的频率分数是原数组中众数的频率 3 。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 0 <= k <= 1014

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counter = Counter(nums)




so = Solution()
print(so.maxFrequencyScore())




