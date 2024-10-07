# 给你一个长度为 n 的整数数组 nums ，表示由范围 [0, n - 1] 内所有整数组成的一个排列。
#
# 全局倒置 的数目等于满足下述条件不同下标对 (i, j) 的数目：
#
# 0 <= i < j < n
# nums[i] > nums[j]
# 局部倒置 的数目等于满足下述条件的下标 i 的数目：
#
# 0 <= i < n - 1
# nums[i] > nums[i + 1]
# 当数组 nums 中 全局倒置 的数量等于 局部倒置 的数量时，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,0,2]
# 输出：true
# 解释：有 1 个全局倒置，和 1 个局部倒置。
# 示例 2：
#
# 输入：nums = [1,2,0]
# 输出：false
# 解释：有 2 个全局倒置，和 1 个局部倒置。
#
# 提示：
#
# n == nums.length
# 1 <= n <= 105
# 0 <= nums[i] < n
# nums 中的所有整数 互不相同
# nums 是范围 [0, n - 1] 内所有数字组成的一个排列

from leetcode.allcode.competition.mypackage import *

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        cnt1 = cnt2 = 0
        n = len(nums)
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                cnt1 += 1
        l = [nums[0]]
        for num in nums[1:]:
            pos = bisect.bisect_left(l, num)
            cnt2 += (len(l) - pos)
            l.insert(pos, num)
        return cnt1 == cnt2




so = Solution()
print(so.isIdealPermutation([1,0,2]))  # true
print(so.isIdealPermutation([1,2,0]))  # false

