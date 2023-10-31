# 给你两个正整数：n 和 target 。
#
# 如果数组 nums 满足下述条件，则称其为 美丽数组 。
#
# nums.length == n.
# nums 由两两互不相同的正整数组成。
# 在范围 [0, n-1] 内，不存在 两个 不同 下标 i 和 j ，使得 nums[i] + nums[j] == target 。
# 返回符合条件的美丽数组所可能具备的 最小 和。
#
#
#
# 示例 1：
#
# 输入：n = 2, target = 3
# 输出：4
# 解释：nums = [1,3] 是美丽数组。
# - nums 的长度为 n = 2 。
# - nums 由两两互不相同的正整数组成。
# - 不存在两个不同下标 i 和 j ，使得 nums[i] + nums[j] == 3 。
# 可以证明 4 是符合条件的美丽数组所可能具备的最小和。
# 示例 2：
#
# 输入：n = 3, target = 3
# 输出：8
# 解释：
# nums = [1,3,4] 是美丽数组。
# - nums 的长度为 n = 3 。
# - nums 由两两互不相同的正整数组成。
# - 不存在两个不同下标 i 和 j ，使得 nums[i] + nums[j] == 3 。
# 可以证明 8 是符合条件的美丽数组所可能具备的最小和。
# 示例 3：
#
# 输入：n = 1, target = 1
# 输出：1
# 解释：nums = [1] 是美丽数组。
#
#
# 提示：
#
# 1 <= n <= 105
# 1 <= target <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        s = set()
        cnt = 0
        ans = 0
        i = 1
        while cnt < n:
            if target - i not in s:
                ans += i
                cnt += 1
                s.add(i)
            i += 1
        return ans



so = Solution()
print(so.minimumPossibleSum(n = 2, target = 3))
print(so.minimumPossibleSum(n = 3, target = 3))
print(so.minimumPossibleSum(n = 1, target = 1))



