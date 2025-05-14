# 给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
#
#
#
# 示例 1：
#
# 输入：nums = [2,2,3,2]
# 输出：3
# 示例 2：
#
# 输入：nums = [0,1,0,1,0,1,100]
# 输出：100
#
#
# 提示：
#
# 1 <= nums.length <= 3 * 104
# -231 <= nums[i] <= 231 - 1
# nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次
#
#
# 进阶：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
#
#
# 注意：本题与主站 137 题相同： https://leetcode-cn.com/problems/single-number-ii/

from leetcode.allcode.competition.mypackage import *

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter()
        for x in nums:
            for i in range(32):
                if x & (1 << i):
                    counter[i] += 1
        ans = 0
        for i, c in counter.items():
            if c % 3 != 0:
                ans |= (1 << i)

        if ans & (1 << 31):
            ans -= (1 << 32)
        return ans


so = Solution()




