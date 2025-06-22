# 给你一个下标从 0 开始且长度为 n 的整数数组 nums 。分割 数组 nums 的方案数定义为符合以下两个条件的 pivot 数目：
#
# 1 <= pivot < n
# nums[0] + nums[1] + ... + nums[pivot - 1] == nums[pivot] + nums[pivot + 1] + ... + nums[n - 1]
# 同时给你一个整数 k 。你可以将 nums 中 一个 元素变为 k 或 不改变 数组。
#
# 请你返回在 至多 改变一个元素的前提下，最多 有多少种方法 分割 nums 使得上述两个条件都满足。
#
#
#
# 示例 1：
#
# 输入：nums = [2,-1,2], k = 3
# 输出：1
# 解释：一个最优的方案是将 nums[0] 改为 k 。数组变为 [3,-1,2] 。
# 有一种方法分割数组：
# - pivot = 2 ，我们有分割 [3,-1 | 2]：3 + -1 == 2 。
# 示例 2：
#
# 输入：nums = [0,0,0], k = 1
# 输出：2
# 解释：一个最优的方案是不改动数组。
# 有两种方法分割数组：
# - pivot = 1 ，我们有分割 [0 | 0,0]：0 == 0 + 0 。
# - pivot = 2 ，我们有分割 [0,0 | 0]: 0 + 0 == 0 。
# 示例 3：
#
# 输入：nums = [22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14], k = -33
# 输出：4
# 解释：一个最优的方案是将 nums[2] 改为 k 。数组变为 [22,4,-33,-20,-15,15,-16,7,19,-10,0,-13,-14] 。
# 有四种方法分割数组。
#
#
# 提示：
#
# n == nums.length
# 2 <= n <= 105
# -105 <= k, nums[i] <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))
        counter = Counter(s[1:-1])  # 前缀和计数时，去掉最后一个
        if s[n] & 1 == 1:
            ans = 0
        else:
            ans = counter[s[n] // 2]

        pc = Counter()
        for i, x in enumerate(nums):
            # 将x改为k，从x开始向后的每个前缀和都增加 delta
            delta = k - x
            s_new = s[n] + delta
            if s_new & 1 == 0:
                h_new = s_new // 2
                res = pc[h_new] + (counter[h_new - delta] - pc[h_new - delta])  # counter中不含最后一个元素，这里就不需要考虑了
                ans = max(ans, res)
            pc[s[i + 1]] += 1
        return ans


so = Solution()
print(so.waysToPartition(nums = [0,0,1,0], k = 0))
print(so.waysToPartition(nums = [0,-4732,0,0], k = -4732))
print(so.waysToPartition(nums = [22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14], k = -33))
print(so.waysToPartition(nums = [0,0,0], k = 1))
print(so.waysToPartition(nums = [2,-1,2], k = 3))
