# 给定由一些正数（代表长度）组成的数组 nums ，返回 由其中三个长度组成的、面积不为零的三角形的最大周长 。如果不能形成任何面积不为零的三角形，返回 0。
#
#
#
# 示例 1：
#
# 输入：nums = [2,1,2]
# 输出：5
# 解释：你可以用三个边长组成一个三角形:1 2 2。
# 示例 2：
#
# 输入：nums = [1,2,1,10]
# 输出：0
# 解释：
# 你不能用边长 1,1,2 来组成三角形。
# 不能用边长 1,1,10 来构成三角形。
# 不能用边长 1、2 和 10 来构成三角形。
# 因为我们不能用任何三条边长来构成一个非零面积的三角形，所以我们返回 0。
#
#
# 提示：
#
# 3 <= nums.length <= 104
# 1 <= nums[i] <= 106


from leetcode.allcode.competition.mypackage import *

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        for i in range(n - 2):
            if nums[i + 1] + nums[i + 2] > nums[i]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0

so = Solution()
print(so.largestPerimeter([2,1,2]))
print(so.largestPerimeter([1,2,1,10]))
