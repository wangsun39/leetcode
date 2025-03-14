# 给你两个整数数组，nums1 和 nums2，长度均为 n，以及一个正整数 k 。
#
# 对从 0 到 n - 1 每个下标 i ，执行下述操作：
#
# 找出所有满足 nums1[j] 小于 nums1[i] 的下标 j 。
# 从这些下标对应的 nums2[j] 中选出 至多 k 个，并 最大化 这些值的总和作为结果。
# 返回一个长度为 n 的数组 answer ，其中 answer[i] 表示对应下标 i 的结果。
#
#
#
# 示例 1：
#
# 输入：nums1 = [4,2,1,5,3], nums2 = [10,20,30,40,50], k = 2
#
# 输出：[80,30,0,80,50]
#
# 解释：
#
# 对于 i = 0 ：满足 nums1[j] < nums1[0] 的下标为 [1, 2, 4] ，选出其中值最大的两个，结果为 50 + 30 = 80 。
# 对于 i = 1 ：满足 nums1[j] < nums1[1] 的下标为 [2] ，只能选择这个值，结果为 30 。
# 对于 i = 2 ：不存在满足 nums1[j] < nums1[2] 的下标，结果为 0 。
# 对于 i = 3 ：满足 nums1[j] < nums1[3] 的下标为 [0, 1, 2, 4] ，选出其中值最大的两个，结果为 50 + 30 = 80 。
# 对于 i = 4 ：满足 nums1[j] < nums1[4] 的下标为 [1, 2] ，选出其中值最大的两个，结果为 30 + 20 = 50 。
# 示例 2：
#
# 输入：nums1 = [2,2,2,2], nums2 = [3,1,2,3], k = 1
#
# 输出：[0,0,0,0]
#
# 解释：由于 nums1 中的所有元素相等，不存在满足条件 nums1[j] < nums1[i]，所有位置的结果都是 0 。
#
#
#
# 提示：
#
# n == nums1.length == nums2.length
# 1 <= n <= 105
# 1 <= nums1[i], nums2[i] <= 106
# 1 <= k <= n

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        mxl = []
        n = len(nums1)
        ans = [0] * n
        s = 0
        pre_v = -1
        pre_a = 0
        for i, x in sorted(enumerate(nums1), key=lambda y:y[1]):
            if pre_v == x or pre_v == -1:
                ans[i] = pre_a
            else:
                ans[i] = s
            pre_v, pre_a = x, ans[i]
            if len(mxl) < k:
                heappush(mxl, nums2[i])
                s += nums2[i]
            else:
                if mxl[0] < nums2[i]:
                    y = heappop(mxl)
                    s += nums2[i] - y
                    heappush(mxl, nums2[i])
        return ans

so = Solution()
print(so.findMaxSum(nums1 = [4,2,1,5,3], nums2 = [10,20,30,40,50], k = 2))
print(so.findMaxSum(nums1 = [2,2,2,2], nums2 = [3,1,2,3], k = 1))




