# 给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。
#
# 如果子数组中所有元素都相等，则认为子数组是一个 等值子数组 。注意，空数组是 等值子数组 。
#
# 从 nums 中删除最多 k 个元素后，返回可能的最长等值子数组的长度。
#
# 子数组 是数组中一个连续且可能为空的元素序列。
#
#
#
# 示例 1：
#
# 输入：nums = [1,3,2,3,1,3], k = 3
# 输出：3
# 解释：最优的方案是删除下标 2 和下标 4 的元素。
# 删除后，nums 等于 [1, 3, 3, 3] 。
# 最长等值子数组从 i = 1 开始到 j = 3 结束，长度等于 3 。
# 可以证明无法创建更长的等值子数组。
# 示例 2：
#
# 输入：nums = [1,1,2,2,1,1], k = 2
# 输出：4
# 解释：最优的方案是删除下标 2 和下标 3 的元素。
# 删除后，nums 等于 [1, 1, 1, 1] 。
# 数组自身就是等值子数组，长度等于 4 。
# 可以证明无法创建更长的等值子数组。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= nums.length
# 0 <= k <= nums.length

from leetcode.allcode.competition.mypackage import *

class Solution:
    def longestEqualSubarray1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def check(val):
            size = val + k
            counter = Counter(nums[: size])
            for v in counter.values():
                if v >= val:
                    return True
            for i in range(size, n):
                counter[nums[i - size]] -= 1
                counter[nums[i]] += 1
                if counter[nums[i]] >= val:
                    return True
            return False
        lo, hi = 0, n + 1
        while lo < hi - 1:
            mid = (lo + hi) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid
        return lo

    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        d = defaultdict(list)
        for i, x in enumerate(nums):
            d[x].append(i)
        ans = 0
        for l in d.values():
            n = len(l)
            left = right = 0
            while right < n:
                while (right - left + 1) + k >= l[right] - l[left] + 1:
                    ans = max(ans, right - left + 1)
                    right += 1
                    if right >= n: break
                left += 1
                right = max(right, left)
        return ans



so = Solution()
print(so.longestEqualSubarray(nums = [1,3,2,3,1,3], k = 3))
print(so.longestEqualSubarray(nums = [1,1,2,2,1,1], k = 2))




