# 给你一个长度为 3 的整数数组 nums。
#
# 现以某种顺序 连接 数组 nums 中所有元素的 二进制表示 ，请你返回可以由这种方法形成的 最大 数值。
#
# 注意 任何数字的二进制表示 不含 前导零。
#
#
#
# 示例 1:
#
# 输入: nums = [1,2,3]
#
# 输出: 30
#
# 解释:
#
# 按照顺序 [3, 1, 2] 连接数字的二进制表示，得到结果 "11110"，这是 30 的二进制表示。
#
# 示例 2:
#
# 输入: nums = [2,8,16]
#
# 输出: 1296
#
# 解释:
#
# 按照顺序 [2, 8, 16] 连接数字的二进制表述，得到结果 "10100010000"，这是 1296 的二进制表示。
#
#
#
# 提示:
#
# nums.length == 3
# 1 <= nums[i] <= 127

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        def calc(a, b, c):
            v = bin(a)[2:] + bin(b)[2:] + bin(c)[2:]
            return int(v, 2)

        return max(calc(nums[0], nums[1], nums[2]),calc(nums[2], nums[0], nums[1]),calc(nums[0], nums[2], nums[1]),
                   calc(nums[1], nums[0], nums[2]),calc(nums[1], nums[2], nums[0]),calc(nums[2], nums[1], nums[0]))


so = Solution()
print(so.maxGoodNumber(nums = [1,2,3]))
print(so.maxGoodNumber(nums = [2,8,16]))




