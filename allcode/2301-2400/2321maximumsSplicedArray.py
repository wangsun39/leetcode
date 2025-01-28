# 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，长度都是 n 。
#
# 你可以选择两个整数 left 和 right ，其中 0 <= left <= right < n ，接着 交换 两个子数组 nums1[left...right] 和 nums2[left...right] 。
#
# 例如，设 nums1 = [1,2,3,4,5] 和 nums2 = [11,12,13,14,15] ，整数选择 left = 1 和 right = 2，那么 nums1 会变为 [1,12,13,4,5] 而 nums2 会变为 [11,2,3,14,15] 。
# 你可以选择执行上述操作 一次 或不执行任何操作。
#
# 数组的 分数 取 sum(nums1) 和 sum(nums2) 中的最大值，其中 sum(arr) 是数组 arr 中所有元素之和。
#
# 返回 可能的最大分数 。
#
# 子数组 是数组中连续的一个元素序列。arr[left...right] 表示子数组包含 nums 中下标 left 和 right 之间的元素（含 下标 left 和 right 对应元素）。
#
#
#
# 示例 1：
#
# 输入：nums1 = [60,60,60], nums2 = [10,90,10]
# 输出：210
# 解释：选择 left = 1 和 right = 1 ，得到 nums1 = [60,90,60] 和 nums2 = [10,60,10] 。
# 分数为 max(sum(nums1), sum(nums2)) = max(210, 80) = 210 。
# 示例 2：
#
# 输入：nums1 = [20,40,20,70,30], nums2 = [50,20,50,40,20]
# 输出：220
# 解释：选择 left = 3 和 right = 4 ，得到 nums1 = [20,40,20,40,20] 和 nums2 = [50,20,50,70,30] 。
# 分数为 max(sum(nums1), sum(nums2)) = max(140, 220) = 220 。
# 示例 3：
#
# 输入：nums1 = [7,11,13], nums2 = [1,1,1]
# 输出：31
# 解释：选择不交换任何子数组。
# 分数为 max(sum(nums1), sum(nums2)) = max(31, 3) = 31 。
#
#
# 提示：
#
# n == nums1.length == nums2.length
# 1 <= n <= 105
# 1 <= nums1[i], nums2[i] <= 104

from leetcode.allcode.competition.mypackage import *

# bit位 函数：
# n.bit_length()
# value = int(s, 2)

class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        sub1 = [nums1[i] - nums2[i] for i in range(n)]
        sub2 = [nums2[i] - nums1[i] for i in range(n)]
        def maxArray(arr):
            dp = [0] * n
            dp[0] = arr[0]
            ans = dp[0]
            for i in range(1, n):
                dp[i] = max(arr[i], dp[i - 1] + arr[i])
                ans = max(ans, dp[i])
            return ans
        r1, r2 = maxArray(sub1), maxArray(sub2)
        # print(r1,r2)
        return max(sum(nums1) + r2, sum(nums2) + r1)

so = Solution()
print(so.maximumsSplicedArray(nums1 = [60,160,60], nums2 = [10,90,10]))
print(so.maximumsSplicedArray(nums1 = [60,60,60], nums2 = [10,90,10]))
print(so.maximumsSplicedArray([20,40,20,70,30], nums2 = [50,20,50,40,20]))
print(so.maximumsSplicedArray(nums1 = [7,11,13], nums2 = [1,1,1]))




