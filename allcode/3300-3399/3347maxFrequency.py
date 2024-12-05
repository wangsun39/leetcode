# 给你一个整数数组 nums 和两个整数 k 和 numOperations 。
#
# 你必须对 nums 执行 操作  numOperations 次。每次操作中，你可以：
#
# 选择一个下标 i ，它在之前的操作中 没有 被选择过。
# 将 nums[i] 增加范围 [-k, k] 中的一个整数。
# 在执行完所有操作以后，请你返回 nums 中出现 频率最高 元素的出现次数。
#
# 一个元素 x 的 频率 指的是它在数组中出现的次数。
#
#
#
# 示例 1：
#
# 输入：nums = [1,4,5], k = 1, numOperations = 2
#
# 输出：2
#
# 解释：
#
# 通过以下操作得到最高频率 2 ：
#
# 将 nums[1] 增加 0 ，nums 变为 [1, 4, 5] 。
# 将 nums[2] 增加 -1 ，nums 变为 [1, 4, 4] 。
# 示例 2：
#
# 输入：nums = [5,11,20,20], k = 5, numOperations = 1
#
# 输出：2
#
# 解释：
#
# 通过以下操作得到最高频率 2 ：
#
# 将 nums[1] 增加 0 。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 0 <= k <= 109
# 0 <= numOperations <= nums.length

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        diff = defaultdict(int)
        counter = Counter(nums)
        for x in nums:
            diff[x - k] += 1
            diff[x] += 0
            diff[x + k + 1] -= 1
        diff = [[key, v] for key, v in diff.items()]
        diff.sort()
        ans = 0
        s = 0
        for key, v in diff:
            s += v
            if s - counter[key] <= numOperations:
                ans = max(ans, s)
            else:
                ans = max(ans, counter[key] + numOperations)
        return ans

so = Solution()
print(so.maxFrequency(nums = [20,51,73,4,19,54,52,8,53,89,77,25,89,48,81,45,49,59,77,13], k = 21, numOperations = 7))
print(so.maxFrequency(nums = [5,11,20,20], k = 5, numOperations = 1))
print(so.maxFrequency(nums = [1,4,5], k = 1, numOperations = 2))




