# 给你一个整数数组 nums 和一个整数数字 x。
#
# 如果一个 子数组 nums[l..r] 的元素和同时满足以下两个条件，则认为该子数组是 有效子数组：
#
# 该和的首位数字等于 x。
# 该和的末位数字等于 x。
# 返回有效子数组的数量。
#
# 子数组 是数组中一个连续、非空 的元素序列。
#
#
#
# 示例 1：
#
# 输入： nums = [1,100,1], x = 1
#
# 输出： 4
#
# 解释：
#
# 有效子数组为：
#
# nums[0..0]：sum = 1
# nums[0..1]：sum = 1 + 100 = 101
# nums[1..2]：sum = 100 + 1 = 101
# nums[2..2]：sum = 1
# 因此，答案为 4。
#
# 示例 2：
#
# 输入： nums = [1], x = 2
#
# 输出： 0
#
# 解释：
#
# 唯一的子数组是 nums[0..0]，其和为 1，不满足条件。
#
# 因此，答案为 0。
#
#
#
# 提示：
#
# 1 <= nums.length <= 1500
# 1 <= nums[i] <= 109
# 1 <= x <= 9

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        s = list(accumulate(nums, initial=0))
        n = len(nums)
        ans = 0
        x = str(x)
        for i in range(n):
            for j in range(i, n):
                ss = s[j + 1] - s[i]
                c = str(ss)
                if c[0] == c[-1] == x:
                    ans += 1
        return ans


so = Solution()




