# 我们有两个长度相等且不为空的整型数组 nums1 和 nums2 。在一次操作中，我们可以交换 nums1[i] 和 nums2[i]的元素。
#
# 例如，如果 nums1 = [1,2,3,8] ， nums2 =[5,6,7,4] ，你可以交换 i = 3 处的元素，得到 nums1 =[1,2,3,4] 和 nums2 =[5,6,7,8] 。
# 返回 使 nums1 和 nums2 严格递增 所需操作的最小次数 。
#
# 数组 arr 严格递增 且  arr[0] < arr[1] < arr[2] < ... < arr[arr.length - 1] 。
#
# 注意：
#
# 用例保证可以实现操作。
#  
#
# 示例 1:
#
# 输入: nums1 = [1,3,5,4], nums2 = [1,2,3,7]
# 输出: 1
# 解释:
# 交换 A[3] 和 B[3] 后，两个数组如下:
# A = [1, 3, 5, 7] ， B = [1, 2, 3, 4]
# 两个数组均为严格递增的。
# 示例 2:
#
# 输入: nums1 = [0,3,5,8,9], nums2 = [2,1,4,6,9]
# 输出: 1
#  
#
# 提示:
#
# 2 <= nums1.length <= 105
# nums2.length == nums1.length
# 0 <= nums1[i], nums2[i] <= 2 * 105
#
# https://leetcode.cn/problems/minimum-swaps-to-make-sequences-increasing

from typing import List
class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        p1, p2 = [nums1[0], nums2[0]], [nums2[0], nums1[0]]
        dp1, dp2 = 0, 1
        if nums1[0] == nums2[0]:
            dp1, dp2 = 0, 0  # 分别表示不交换第i个，和交换第i个的最少交换次数
        n = len(nums1)
        for i in range(1, n):
            dp11, dp22 = n, n
            if nums1[i] > p1[0] and nums2[i] > p1[1]:
                dp11, dp22 = dp1, dp2 + 1
            if nums1[i] > p2[0] and nums2[i] > p2[1]:
                dp11, dp22 = min(dp11, dp2), min(dp22, dp1 + 1)
            p1, p2 = [nums1[i], nums2[i]], [nums2[i], nums1[i]]
            dp1, dp2 = dp11, dp22
        return min(dp1, dp2)

so = Solution()

print(so.minSwap(nums1 = [0,3,4,9,10], nums2 = [2,3,7,5,6]))
print(so.minSwap(nums1 = [0,3,5,8,9], nums2 = [2,1,4,6,9]))
print(so.minSwap(nums1 = [1,3,5,4], nums2 = [1,2,3,7]))

