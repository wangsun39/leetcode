# 给你两个整数数组 nums1 和 nums2 ，两个数组长度都是 n ，再给你一个整数 k 。你可以对数组 nums1 进行以下操作：
#
# 选择两个下标 i 和 j ，将 nums1[i] 增加 k ，将 nums1[j] 减少 k 。换言之，nums1[i] = nums1[i] + k 且 nums1[j] = nums1[j] - k 。
# 如果对于所有满足 0 <= i < n 都有 num1[i] == nums2[i] ，那么我们称 nums1 等于 nums2 。
#
# 请你返回使 nums1 等于 nums2 的 最少 操作数。如果没办法让它们相等，请你返回 -1 。
#
#
#
# 示例 1：
#
# 输入：nums1 = [4,3,1,4], nums2 = [1,3,7,1], k = 3
# 输出：2
# 解释：我们可以通过 2 个操作将 nums1 变成 nums2 。
# 第 1 个操作：i = 2 ，j = 0 。操作后得到 nums1 = [1,3,4,4] 。
# 第 2 个操作：i = 2 ，j = 3 。操作后得到 nums1 = [1,3,7,1] 。
# 无法用更少操作使两个数组相等。
# 示例 2：
#
# 输入：nums1 = [3,8,5,2], nums2 = [2,4,1,6], k = 1
# 输出：-1
# 解释：无法使两个数组相等。
#
#
# 提示：
#
# n == nums1.length == nums2.length
# 2 <= n <= 105
# 0 <= nums1[i], nums2[j] <= 109
# 0 <= k <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        r1 = [x % k for x in nums1]
        r2 = [x % k for x in nums2]
        if r1 != r2: return -1
        diff = [(nums1[i] - nums2[i]) // k for i in range(n)]
        ans = 0
        counter = Counter()
        for i in range(n):
            counter[r1[i]] += diff[i]
            if diff[i] > 0:
                ans += diff[i]
        if any(x != 0 for x in counter.values()):
            return -1
        return ans




so = Solution()
print(so.minOperations(nums1 = [2,4], nums2 = [4,2], k = 2))  # 1
print(so.minOperations(nums1 = [3,8,5,2], nums2 = [2,4,1,6], k = 1))  # -1
print(so.minOperations(nums1 = [4,3,1,4], nums2 = [1,3,7,1], k = 3))  # 2




