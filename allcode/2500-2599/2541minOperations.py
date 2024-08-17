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
        d1, d2 = defaultdict(list), defaultdict(list)
        if sum(nums1) != sum(nums2): return -1
        for x in nums1:
            d1[x % k].append(x)
        for x in nums2:
            d2[x % k].append(x)
        if len(d1) != len(d2): return -1
        ans = 0
        for x in d1:
            if len(d1[x]) != len(d2[x]): return -1
            c11, c22 = Counter(d1[x]), Counter(d2[x])
            for y in c11:
                if c11[y] > c22[y]:
                    ans += c11[y] - c22[y]
        return ans



so = Solution()
print(so.minOperations(nums1 = [3,8,5,2], nums2 = [2,4,1,6], k = 1))
print(so.minOperations(nums1 = [4,3,1,4], nums2 = [1,3,7,1], k = 3))




