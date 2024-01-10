# 给你一个下标从 0 开始的数组 nums ，该数组由 n 个正整数组成。
#
# 如果满足下述条件，则数组 nums 是一个 交替数组 ：
#
# nums[i - 2] == nums[i] ，其中 2 <= i <= n - 1 。
# nums[i - 1] != nums[i] ，其中 1 <= i <= n - 1 。
# 在一步 操作 中，你可以选择下标 i 并将 nums[i] 更改 为 任一 正整数。
#
# 返回使数组变成交替数组的 最少操作数 。
#
#
#
# 示例 1：
#
# 输入：nums = [3,1,3,2,4,3]
# 输出：3
# 解释：
# 使数组变成交替数组的方法之一是将该数组转换为 [3,1,3,1,3,1] 。
# 在这种情况下，操作数为 3 。
# 可以证明，操作数少于 3 的情况下，无法使数组变成交替数组。
# 示例 2：
#
# 输入：nums = [1,2,2,2,2]
# 输出：2
# 解释：
# 使数组变成交替数组的方法之一是将该数组转换为 [1,2,1,2,1].
# 在这种情况下，操作数为 2 。
# 注意，数组不能转换成 [2,2,2,2,2] 。因为在这种情况下，nums[0] == nums[1]，不满足交替数组的条件。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        odds, even = nums[::2], nums[1::2]
        c_o, c_e = Counter(odds), Counter(even)
        l_o, l_e = list(c_o.items()), list(c_e.items())
        l_o.sort(key=lambda x:x[1], reverse=True)
        l_e.sort(key=lambda x:x[1], reverse=True)
        l_o.append([-1, 0])  # 哨兵
        l_e.append([-1, 0])  # 哨兵
        if l_e[0][0] != l_o[0][0]:
            return n - l_e[0][1] - l_o[0][1]
        return min(n - l_e[0][1] - l_o[1][1], n - l_e[1][1] - l_o[0][1])





so = Solution()
print(so.minimumOperations(nums = [1,2,2,2,2]))
print(so.minimumOperations(nums = [3,1,3,2,4,3]))




