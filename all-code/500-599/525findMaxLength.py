# 给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。
#
#
#
# 示例 1:
#
# 输入: nums = [0,1]
# 输出: 2
# 说明: [0, 1] 是具有相同数量 0 和 1 的最长连续子数组。
# 示例 2:
#
# 输入: nums = [0,1,0]
# 输出: 2
# 说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# nums[i] 不是 0 就是 1

from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = cur = 0  # 记录当前的0和1的个数差
        d = {0: -1}  # 记录0和1个数差为x的最小下标
        for i, x in enumerate(nums):
            if x == 0:
                cur += 1
            else:
                cur -= 1
            if cur not in d:
                d[cur] = i
            else:
                ans = max(ans, i - d[cur])
        return ans


so = Solution()
print(so.findMaxLength(nums = [0,1]))
print(so.findMaxLength(nums = [0,1,0]))

