
# 你打算利用空闲时间来做兼职工作赚些零花钱。
#
# 这里有 n 份兼职工作，每份工作预计从 startTime[i] 开始到 endTime[i] 结束，报酬为 profit[i]。
#
# 给你一份兼职工作表，包含开始时间 startTime，结束时间 endTime 和预计报酬 profit 三个数组，请你计算并返回可以获得的最大报酬。
# 给你一个正整数数组 nums，你需要从中任选一些子集，然后将子集中每一个数乘以一个 任意整数，并求出他们的和。
#
# 假如该和结果为 1，那么原数组就是一个「好数组」，则返回 True；否则请返回 False。
#
#
#
# 示例 1：
#
# 输入：nums = [12,5,7,23]
# 输出：true
# 解释：挑选数字 5 和 7。
# 5*3 + 7*(-2) = 1
# 示例 2：
#
# 输入：nums = [29,6,10]
# 输出：true
# 解释：挑选数字 29, 6 和 10。
# 29*1 + 6*(-3) + 10*(-1) = 1
# 示例 3：
#
# 输入：nums = [3,6]
# 输出：false
#
#
# 提示：
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9

from typing import List
from math import *

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        g = nums[0]
        for x in nums[1:]:
            g = gcd(g, x)
        return g == 1




obj = Solution()
print(obj.isGoodArray([12,5,7,23]))

