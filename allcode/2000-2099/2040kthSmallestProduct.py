# 给你两个 从小到大排好序 且下标从 0 开始的整数数组 nums1 和 nums2 以及一个整数 k ，请你返回第 k （从 1 开始编号）小的 nums1[i] * nums2[j] 的乘积，其中 0 <= i < nums1.length 且 0 <= j < nums2.length 。
#
#
# 示例 1：
#
# 输入：nums1 = [2,5], nums2 = [3,4], k = 2
# 输出：8
# 解释：第 2 小的乘积计算如下：
# - nums1[0] * nums2[0] = 2 * 3 = 6
# - nums1[0] * nums2[1] = 2 * 4 = 8
# 第 2 小的乘积为 8 。
# 示例 2：
#
# 输入：nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6
# 输出：0
# 解释：第 6 小的乘积计算如下：
# - nums1[0] * nums2[1] = (-4) * 4 = -16
# - nums1[0] * nums2[0] = (-4) * 2 = -8
# - nums1[1] * nums2[1] = (-2) * 4 = -8
# - nums1[1] * nums2[0] = (-2) * 2 = -4
# - nums1[2] * nums2[0] = 0 * 2 = 0
# - nums1[2] * nums2[1] = 0 * 4 = 0
# 第 6 小的乘积为 0 。
# 示例 3：
#
# 输入：nums1 = [-2,-1,0,1,2], nums2 = [-3,-1,2,4,5], k = 3
# 输出：-6
# 解释：第 3 小的乘积计算如下：
# - nums1[0] * nums2[4] = (-2) * 5 = -10
# - nums1[0] * nums2[3] = (-2) * 4 = -8
# - nums1[4] * nums2[0] = 2 * (-3) = -6
# 第 3 小的乘积为 -6 。
#
#
# 提示：
#
# 1 <= nums1.length, nums2.length <= 5 * 104
# -105 <= nums1[i], nums2[j] <= 105
# 1 <= k <= nums1.length * nums2.length
# nums1 和 nums2 都是从小到大排好序的。


from leetcode.allcode.competition.mypackage import *


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n1, n2 = len(nums1), len(nums2)
        chs = sorted([nums1[0] * nums2[0], nums1[-1] * nums2[-1], nums1[0] * nums2[-1], nums1[-1] * nums2[0]])
        lo, hi = chs[0], chs[-1]

        def calc(val):
            # 计算乘积<=val的数对个数
            res = 0
            for i, x in enumerate(nums1):
                if x > 0:
                    p = bisect_right(nums2, val // x)
                elif x < 0:
                    # u = (val + x - 1) // x
                    p = n2 - bisect_left(nums2, math.ceil(val/x))  # 比 val / x 上取整 大的数
                else:
                    p = n2 if val >= 0 else 0
                res += p
            return res
        if k == 1:
            return lo

        while lo + 1 < hi:
            mid = (lo + hi) // 2
            v = calc(mid)
            if v < k:
                lo = mid
            else:
                hi = mid
        return hi


so = Solution()
print(so.kthSmallestProduct(nums1 = [-9,6,10], nums2 = [-7,-1,1,2,3,4,4,6,9,10], k = 15))  # 10
print(so.kthSmallestProduct(nums1 = [-8,-8,3,7], nums2 = [-1], k = 3))  # 8
print(so.kthSmallestProduct(nums1 = [-100000,100000], nums2 = [-100000,100000], k = 1))
print(so.kthSmallestProduct(nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6))
print(so.kthSmallestProduct(nums1 = [2,5], nums2 = [3,4], k = 2))


