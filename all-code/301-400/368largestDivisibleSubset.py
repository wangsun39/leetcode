# 给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i], answer[j]) 都应当满足：
# answer[i] % answer[j] == 0 ，或
# answer[j] % answer[i] == 0
# 如果存在多个有效解子集，返回其中任何一个均可。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：[1,2]
# 解释：[1,3] 也会被视为正确答案。
# 示例 2：
#
# 输入：nums = [1,2,4,8]
# 输出：[1,2,4,8]
#  
#
# 提示：
#
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 2 * 109
# nums 中的所有整数 互不相同

from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        N = len(nums)
        dp = [0] * N
        dp[0] = [1, [nums[0]]]  # dp[i] = [x, y] 分别表示 nums[i] 以nums[i]为最大值的Subset 最多有多少个元素，以及能取到最大值时，Subset中的元素列表
        largest = [1, 0]  # 最大值及其下标
        for i in range(1, N):
            num, subset = 0, [nums[i]]
            for j in range(i):
                if nums[i] % nums[j] == 0 and num < dp[j][0]:
                    num, subset = dp[j][0], dp[j][1] + [nums[i]]
            dp[i] = [num + 1, subset]
            if largest[0] < num + 1:
                largest = [num + 1, i]
        print(dp)
        print(largest)
        return dp[largest[1]][1]

so = Solution()
print(so.largestDivisibleSubset([3,4,16,8]))
print(so.largestDivisibleSubset([9,1,2,4,8]))

