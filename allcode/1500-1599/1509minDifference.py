# 给你一个数组 nums 。
#
# 每次操作你可以选择 nums 中的任意一个元素并将它改成 任意值 。
#
# 在 执行最多三次移动后 ，返回 nums 中最大值与最小值的最小差值。
#
#
#
# 示例 1：
#
# 输入：nums = [5,3,2,4]
# 输出：0
# 解释：我们最多可以走 3 步。
# 第一步，将 2 变为 3 。 nums 变成 [5,3,3,4] 。
# 第二步，将 4 改为 3 。 nums 变成 [5,3,3,3] 。
# 第三步，将 5 改为 3 。 nums 变成 [3,3,3,3] 。
# 执行 3 次移动后，最小值和最大值之间的差值为 3 - 3 = 0 。
# 示例 2：
#
# 输入：nums = [1,5,0,10,14]
# 输出：1
# 解释：我们最多可以走 3 步。
# 第一步，将 5 改为 0 。 nums变成 [1,0,0,10,14] 。
# 第二步，将 10 改为 0 。 nums变成 [1,0,0,0,14] 。
# 第三步，将 14 改为 1 。 nums变成 [1,0,0,0,1] 。
# 执行 3 步后，最小值和最大值之间的差值为 1 - 0 = 1 。
# 可以看出，没有办法可以在 3 步内使差值变为0。
# 示例 3：
#
# 输入：nums = [3,100,20]
# 输出：0
# 解释：我们最多可以走 3 步。
# 第一步，将 100 改为 7 。 nums 变成 [3,7,20] 。
# 第二步，将 20 改为 7 。 nums 变成 [3,7,7] 。
# 第三步，将 3 改为 7 。 nums 变成 [7,7,7] 。
# 执行 3 步后，最小值和最大值之间的差值是 7 - 7 = 0。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return 0
        nums.sort()
        return min(nums[-4] - nums[0], nums[-3] - nums[1], nums[-2] - nums[2], nums[-1] - nums[3])


so = Solution()
print(so.minDifference([5,3,2,4]))
print(so.minDifference([1,5,0,10,14]))
print(so.minDifference([3,100,20]))




