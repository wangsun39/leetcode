# 给你一个整数数组 nums ，请你求出乘积为正数的最长子数组的长度。
#
# 一个数组的子数组是由原数组中零个或者更多个连续数字组成的数组。
#
# 请你返回乘积为正数的最长子数组长度。
#
#
#
# 示例  1：
#
# 输入：nums = [1,-2,-3,4]
# 输出：4
# 解释：数组本身乘积就是正数，值为 24 。
# 示例 2：
#
# 输入：nums = [0,1,-2,-3,-4]
# 输出：3
# 解释：最长乘积为正数的子数组为 [1,-2,-3] ，乘积为 6 。
# 注意，我们不能把 0 也包括到子数组中，因为这样乘积为 0 ，不是正数。
# 示例 3：
#
# 输入：nums = [-1,-2,-3,0,1]
# 输出：2
# 解释：乘积为正数的最长子数组是 [-1,-2] 或者 [-2,-3] 。
#
#
# 提示：
#
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9

from leetcode.allcode.competition.mypackage import *

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        zero = []
        # 按 0 分组
        for i, x in enumerate(nums):
            if x == 0:
                zero.append(i)
        def get(sub):
            nonlocal ans
            cnt = 0
            first = -1  # 第一个负数的位置
            for i, x in enumerate(sub):
                if x < 0:
                    cnt += 1
                    if cnt & 1:
                        if first != -1:
                            ans = max(ans, i - first)
                        else:
                            first = i
                    else:
                        ans = max(ans, i + 1)
                else:
                    if cnt & 1:
                        ans = max(ans, i - first)
                    else:
                        ans = max(ans, i + 1)

        if 0 == len(zero):
            get(nums)
        else:
            zero.insert(0, -1)
            zero.append(n)
            for a, b in pairwise(zero):
                get(nums[a + 1: b])
        return ans



so = Solution()
print(so.getMaxLen([1,2,3,5,-6,4,0,10]))
print(so.getMaxLen([0,1,-2,-3,-4]))
print(so.getMaxLen([1,-2,-3,4]))
print(so.getMaxLen([-1,-2,-3,0,1]))




