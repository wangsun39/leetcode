# 给两个整数数组 nums1 和 nums2 ，返回 两个数组中 公共的 、长度最长的子数组的长度 。
#
#
#
# 示例 1：
#
# 输入：nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# 输出：3
# 解释：长度最长的公共子数组是 [3,2,1] 。
# 示例 2：
#
# 输入：nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# 输出：5
#
#
# 提示：
#
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 100

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[0] * m for _ in range(n)]  # dp[i][j] 表示以nums1[i]结尾，nums2[j]结尾的公共子串长度
        for i in range(n):
            dp[i][0] = 1 if nums1[i] == nums2[0] else 0
        for j in range(m):
            dp[0][j] = 1 if nums1[0] == nums2[j] else 0

        for i in range(1, n):
            for j in range(1, m):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
        return max(max(x) for x in dp)



so = Solution()
print(so.findLength(nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]))
print(so.findLength(nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]))




