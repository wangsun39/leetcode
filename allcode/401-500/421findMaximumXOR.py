# 给你一个整数数组 nums ，返回 nums[i] XOR nums[j] 的最大运算结果，其中 0 ≤ i ≤ j < n 。
#
#
#
# 示例 1：
#
# 输入：nums = [3,10,5,25,2,8]
# 输出：28
# 解释：最大运算结果是 5 XOR 25 = 28.
# 示例 2：
#
# 输入：nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# 输出：127
#
#
# 提示：
#
# 1 <= nums.length <= 2 * 105
# 0 <= nums[i] <= 231 - 1

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        mx = max(nums)
        prefix = 0
        ans = 0
        for i in range(mx.bit_length() - 1, -1, -1):
            prefix |= (1 << i)
            s = set()  # hash 表
            for x in nums:
                s.add(x & prefix)
            t = ans | (1 << i)
            found = False
            for x in nums:
                if t ^ (x & prefix) in s:
                    found = True
                    break
            if found:
                ans |= (1 << i)
        return ans



so = Solution()
print(so.findMaximumXOR([3,10,5,25,2,8]))
print(so.findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70]))




