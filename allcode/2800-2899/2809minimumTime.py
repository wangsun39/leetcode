# 给你两个长度相等下标从 0 开始的整数数组 nums1 和 nums2 。每一秒，对于所有下标 0 <= i < nums1.length ，nums1[i] 的值都增加 nums2[i] 。操作 完成后 ，你可以进行如下操作：
#
# 选择任一满足 0 <= i < nums1.length 的下标 i ，并使 nums1[i] = 0 。
# 同时给你一个整数 x 。
#
# 请你返回使 nums1 中所有元素之和 小于等于 x 所需要的 最少 时间，如果无法实现，那么返回 -1 。
#
#
#
# 示例 1：
#
# 输入：nums1 = [1,2,3], nums2 = [1,2,3], x = 4
# 输出：3
# 解释：
# 第 1 秒，我们对 i = 0 进行操作，得到 nums1 = [0,2+2,3+3] = [0,4,6] 。
# 第 2 秒，我们对 i = 1 进行操作，得到 nums1 = [0+1,0,6+3] = [1,0,9] 。
# 第 3 秒，我们对 i = 2 进行操作，得到 nums1 = [1+1,0+2,0] = [2,2,0] 。
# 现在 nums1 的和为 4 。不存在更少次数的操作，所以我们返回 3 。
# 示例 2：
#
# 输入：nums1 = [1,2,3], nums2 = [3,3,3], x = 4
# 输出：-1
# 解释：不管如何操作，nums1 的和总是会超过 x 。
#
#
# 提示：
#
# 1 <= nums1.length <= 103
# 1 <= nums1[i] <= 103
# 0 <= nums2[i] <= 103
# nums1.length == nums2.length
# 0 <= x <= 106

from leetcode.allcode.competition.mypackage import *


class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        n = len(nums1)
        nums3 = []  # 按nums2从小到大排序后，将nums1调整为nums3
        for i, _ in sorted(enumerate(nums2), key=lambda x: x[1]):
            nums3.append(nums1[i])
        nums2.sort()
        s1, s2 = sum(nums1), sum(nums2)
        if s1 <= x: return 0
        dp = [[0] * n for _ in range(n)]  # 前i+1个数，选j+1个子序列最大能组合成删除的总和
        dp[0][0] = nums3[0] + nums2[0]
        for i in range(1, n):
            for j in range(i + 1):
                dp[i][j] = dp[i - 1][j]
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + nums3[i] + (j + 1) * nums2[i])
                else:
                    dp[i][j] = max(dp[i][j], nums3[i] + (j + 1) * nums2[i])

        # print(dp)
        for t in range(1, n + 1):
            # 枚举经过了的时间
            # print(s1, t * s2, s1 + t * s2, s1 + t * s2 - dp[-1][t - 1])
            if s1 + t * s2 - dp[-1][t - 1] <= x:
                return t
        return -1


so = Solution()
print(so.minimumTime(nums1 = [1,2,3], nums2 = [1,2,3], x = 4))




