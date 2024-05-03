# 给定两个 以0为索引 的二进制数组 nums1 和 nums2 。找出 最宽 的索引对 (i, j) ，使的 i <= j 并且 nums1[i] + nums1[i+1] + ... + nums1[j] == nums2[i] + nums2[i+1] + ... + nums2[j]。
#
# 最宽 的指标对是指在 i 和 j 之间的 距离最大 的指标对。一对指标之间的 距离 定义为 j - i + 1 。
#
# 返回 最宽 索引对的 距离 。如果没有满足条件的索引对，则返回 0 。
#
#
#
# 示例 1:
#
# 输入: nums1 = [1,1,0,1], nums2 = [0,1,1,0]
# 输出: 3
# 解释:
# 如果i = 1, j = 3:
# Nums1 [1] + Nums1 [2] + Nums1[3] = 1 + 0 + 1 = 2。
# Nums2 [1] + Nums2 [2] + Nums2[3] = 1 + 1 + 0 = 2。
# i和j之间的距离是j - i + 1 = 3 - 1 + 1 = 3。
# 示例 2:
#
# 输入: nums1 = [0,1], nums2 = [1,1]
# 输出: 1
# 解释:
# If i = 1 and j = 1:
# nums1[1] = 1。
# nums2[1] = 1。
# i和j之间的距离是j - i + 1 = 1 - 1 + 1 = 1。
# 示例 3:
#
# 输入: nums1 = [0], nums2 = [1]
# 输出: 0
# 解释:
# 没有满足要求的索引对。
#
#
# 提示:
#
# n == nums1.length == nums2.length
# 1 <= n <= 105
# nums1[i] 仅为 0 或 1.
# nums2[i] 仅为 0 或 1.

from leetcode.allcode.competition.mypackage import *

class Solution:
    def widestPairOfIndices(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        nums3 = [nums2[i] - nums1[i] for i in range(n)]
        s = list(accumulate(nums3, initial=0))
        # 找出使得s[i] == s[j]的最大值j - i
        left = {}  # 值为x的最小下标
        ans = 0
        for i, x in enumerate(s):
            if x in left:
                ans = max(ans, i - left[x])
            else:
                left[x] = i
        return ans


so = Solution()
print(so.widestPairOfIndices(nums1 = [1,1,0,1], nums2 = [0,1,1,0]))
print(so.widestPairOfIndices(nums1 = [0,1], nums2 = [1,1]))
print(so.widestPairOfIndices(nums1 = [0], nums2 = [1]))




