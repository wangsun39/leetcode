# 给你一个按 非递减顺序 排列的整数数组 nums 。
#
# 请你判断是否能在将 nums 分割成 一个或多个子序列 的同时满足下述 两个 条件：
#
# 每个子序列都是一个 连续递增序列（即，每个整数 恰好 比前一个整数大 1 ）。
# 所有子序列的长度 至少 为 3 。
# 如果可以分割 nums 并满足上述条件，则返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3,3,4,5]
# 输出：true
# 解释：nums 可以分割成以下子序列：
# [1,2,3,3,4,5] --> 1, 2, 3
# [1,2,3,3,4,5] --> 3, 4, 5
# 示例 2：
#
# 输入：nums = [1,2,3,3,4,4,5,5]
# 输出：true
# 解释：nums 可以分割成以下子序列：
# [1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
# [1,2,3,3,4,4,5,5] --> 3, 4, 5
# 示例 3：
#
# 输入：nums = [1,2,3,4,4,5]
# 输出：false
# 解释：无法将 nums 分割成长度至少为 3 的连续递增子序列。
#
#
# 提示：
#
# 1 <= nums.length <= 104
# -1000 <= nums[i] <= 1000
# nums 按非递减顺序排列

from leetcode.allcode.competition.mypackage import *

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        c1 = Counter()   # c1[i]  表示以i结尾，长度为1的子序列个数
        c2 = Counter()   # c2[i]  表示以i结尾，长度为2的子序列个数
        c3 = Counter()   # c3[i]  表示以i结尾，长度>=3的子序列个数
        for x in nums:
            if c1[x - 2] or c2[x - 2]: return False
            if c1[x - 1]:
                c1[x - 1] -= 1
                c2[x] += 1
            elif c2[x - 1]:
                c2[x - 1] -= 1
                c3[x] += 1
            elif c3[x - 1]:
                c3[x - 1] -= 1
                c3[x] += 1
            else:
                c1[x] += 1
        return all(x == 0 for x in c1.values()) and all(x == 0 for x in c2.values())


so = Solution()
print(so.isPossible(nums = [1,2,3,3,4,5]))

