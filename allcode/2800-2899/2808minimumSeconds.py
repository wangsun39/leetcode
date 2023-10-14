# 给你一个下标从 0 开始长度为 n 的数组 nums 。
#
# 每一秒，你可以对数组执行以下操作：
#
# 对于范围在 [0, n - 1] 内的每一个下标 i ，将 nums[i] 替换成 nums[i] ，nums[(i - 1 + n) % n] 或者 nums[(i + 1) % n] 三者之一。
# 注意，所有元素会被同时替换。
#
# 请你返回将数组 nums 中所有元素变成相等元素所需要的 最少 秒数。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,1,2]
# 输出：1
# 解释：我们可以在 1 秒内将数组变成相等元素：
# - 第 1 秒，将每个位置的元素分别变为 [nums[3],nums[1],nums[3],nums[3]] 。变化后，nums = [2,2,2,2] 。
# 1 秒是将数组变成相等元素所需要的最少秒数。
# 示例 2：
#
# 输入：nums = [2,1,3,3,2]
# 输出：2
# 解释：我们可以在 2 秒内将数组变成相等元素：
# - 第 1 秒，将每个位置的元素分别变为 [nums[0],nums[2],nums[2],nums[2],nums[3]] 。变化后，nums = [2,3,3,3,3] 。
# - 第 2 秒，将每个位置的元素分别变为 [nums[1],nums[1],nums[2],nums[3],nums[4]] 。变化后，nums = [3,3,3,3,3] 。
# 2 秒是将数组变成相等元素所需要的最少秒数。
# 示例 3：
#
# 输入：nums = [5,5,5,5]
# 输出：0
# 解释：不需要执行任何操作，因为一开始数组中的元素已经全部相等。
#
#
# 提示：
#
# 1 <= n == nums.length <= 105
# 1 <= nums[i] <= 109

from leetcode.allcode.competition.mypackage import *


class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        pre = {}  # pre[i] 表示前一次出现i的位置
        # 先找到每个数最后一次出现的位置
        n = len(nums)
        for i in range(n - 1, -1, -1):
            if nums[i] not in pre:
                pre[nums[i]] = i
        dis = defaultdict(int)  # dis[i] 记录两个 i 之间的最长距离，nums 看作循环数组
        for i, x in enumerate(nums):
            d = (i - pre[x] + n) % n
            if d == 0:
                d = n - 1
            else:
                d = d - 1
            pre[x] = i
            dis[x] = max(dis[x], d)
        ans = min(dis.values())
        return (ans + 1) // 2


so = Solution()
print(so.minimumSeconds([8,13,3,3]))
print(so.minimumSeconds([1,2,1,2]))
print(so.minimumSeconds([2,1,3,3,2]))
print(so.minimumSeconds([5,5,5,5]))




