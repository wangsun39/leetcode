# 两个整数的 汉明距离 指的是这两个数字的二进制数对应位不同的数量。
#
# 给你一个整数数组 nums，请你计算并返回 nums 中任意两个数之间 汉明距离的总和 。
#
#
#
# 示例 1：
#
# 输入：nums = [4,14,2]
# 输出：6
# 解释：在二进制表示中，4 表示为 0100 ，14 表示为 1110 ，2表示为 0010 。（这样表示是为了体现后四位之间关系）
# 所以答案为：
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6
# 示例 2：
#
# 输入：nums = [4,14,4]
# 输出：4
#
#
# 提示：
#
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 109
# 给定输入的对应答案符合 32-bit 整数范围

from leetcode.allcode.competition.mypackage import *

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        counter = Counter()
        n = len(nums)
        for x in nums:
            i = 0
            while x:
                if x & 1: counter[i] += 1
                x >>= 1
                i += 1
        ans = 0
        for _, v in counter.items():
            ans += v * (n - v)
        return ans

so = Solution()
print(so.totalHammingDistance(nums = [4,14,2]))



