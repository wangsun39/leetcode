# 给定一个未排序的整数数组 nums ， 返回最长递增子序列的个数 。
#
# 注意 这个数列必须是 严格 递增的。
#
#
#
# 示例 1:
#
# 输入: [1,3,5,4,7]
# 输出: 2
# 解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
# 示例 2:
#
# 输入: [2,2,2,2,2]
# 输出: 5
# 解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
#
#
# 提示:
#
# 1 <= nums.length <= 2000
# -106 <= nums[i] <= 106

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        arr = sorted(nums)
        d = {x: i + 1 for i, x in enumerate(arr)}
        nums = [d[x] for x in nums]  # 离散化
        dp1 = [1] * n  # 以 nums 结尾的最长子序列个数
        dp2 = [1] * n  # 以 nums 结尾的最长子序列长度
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp2[i] < dp2[j] + 1:
                        dp2[i] = dp2[j] + 1
                        dp1[i] = dp1[j]
                    elif dp2[i] == dp2[j] + 1:
                        dp1[i] += dp1[j]
        print(dp1)
        print(dp2)
        mx = max(dp2)
        return sum(dp1[i] for i in range(n) if mx == dp2[i])


so = Solution()
print(so.findNumberOfLIS([1,2,3,1,2,3,1,2,3]))  # 10
print(so.findNumberOfLIS([1,1,1,2,2,2,3,3,3]))  # 27
print(so.findNumberOfLIS([1,3,5,4,7]))  # 2
print(so.findNumberOfLIS([2,2,2,2,2]))  # 5




