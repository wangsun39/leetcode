# 我们称一个分割整数数组的方案是 好的 ，当它满足：
#
# 数组被分成三个 非空 连续子数组，从左至右分别命名为 left ， mid ， right 。
# left 中元素和小于等于 mid 中元素和，mid 中元素和小于等于 right 中元素和。
# 给你一个 非负 整数数组 nums ，请你返回 好的 分割 nums 方案数目。由于答案可能会很大，请你将结果对 109 + 7 取余后返回。
#
#
#
# 示例 1：
#
# 输入：nums = [1,1,1]
# 输出：1
# 解释：唯一一种好的分割方案是将 nums 分成 [1] [1] [1] 。
# 示例 2：
#
# 输入：nums = [1,2,2,2,5,0]
# 输出：3
# 解释：nums 总共有 3 种好的分割方案：
# [1] [2] [2,2,5,0]
# [1] [2,2] [2,5,0]
# [1,2] [2,2] [5,0]
# 示例 3：
#
# 输入：nums = [3,2,1]
# 输出：0
# 解释：没有好的分割方案。
#
#
# 提示：
#
# 3 <= nums.length <= 105
# 0 <= nums[i] <= 104

from leetcode.allcode.competition.mypackage import *

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        s = list(accumulate(nums, initial=0))
        n = len(nums)
        ans = 0
        for i3 in range(2, n):  # 遍历第3段的开头
            s3 = s[n] - s[i3]
            if s3 * 3 < s[-1]:
                break
            s12 = s[-1] - s3
            # s1 的范围 [max(0, s12-s3), s12 // 2]
            p1 = max(bisect_left(s, max(0, s12 - s3)), 1)  # p1不能取0，否则第一段的长度为0
            p2 = bisect_right(s, s12 // 2)
            p2 = min(p2, i3)
            ans += (p2 - p1)
            ans %= MOD
            # print(i3, p1, p2)
        return ans



so = Solution()
print(so.waysToSplit(nums = [0,0,0]))
print(so.waysToSplit(nums = [1,2,2,2,5,0]))
print(so.waysToSplit(nums = [1,1,1]))
print(so.waysToSplit(nums = [3,2,1]))




