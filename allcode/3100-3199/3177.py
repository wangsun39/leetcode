# 给你一个整数数组 nums 和一个 非负 整数 k 。如果一个整数序列 seq 满足在范围下标范围 [0, seq.length - 2] 中存在 不超过 k 个下标 i 满足 seq[i] != seq[i + 1] ，那么我们称这个整数序列为 好 序列。
#
# 请你返回 nums 中 好
# 子序列
#  的最长长度
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,1,1,3], k = 2
#
# 输出：4
#
# 解释：
#
# 最长好子序列为 [1,2,1,1,3] 。
#
# 示例 2：
#
# 输入：nums = [1,2,3,4,5,1], k = 0
#
# 输出：2
#
# 解释：
#
# 最长好子序列为 [1,2,3,4,5,1] 。
#
#
#
# 提示：
#
# 1 <= nums.length <= 5 * 103
# 1 <= nums[i] <= 109
# 0 <= k <= min(50, nums.length)

from leetcode.allcode.competition.mypackage import *

class Solution:
    def removeDigit(self) -> str:
        pass


so = Solution()
print(so.removeDigit())




