# 给你一个整数数组 nums 和一个整数 k ，找出三个长度为 k 、互不重叠、且全部数字和（3 * k 项）最大的子数组，并返回这三个子数组。
#
# 以下标的数组形式返回结果，数组中的每一项分别指示每个子数组的起始位置（下标从 0 开始）。如果有多个结果，返回字典序最小的一个。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,1,2,6,7,5,1], k = 2
# 输出：[0,3,5]
# 解释：子数组 [1, 2], [2, 6], [7, 5] 对应的起始下标为 [0, 3, 5]。
# 也可以取 [2, 1], 但是结果 [1, 3, 5] 在字典序上更大。
# 示例 2：
#
# 输入：nums = [1,2,1,2,1,2,1,2,1], k = 2
# 输出：[0,2,4]
#
#
# 提示：
#
# 1 <= nums.length <= 2 * 104
# 1 <= nums[i] < 216
# 1 <= k <= floor(nums.length / 3)


from leetcode.allcode.competition.mypackage import *


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        s = list(accumulate(nums, initial=0))
        ks = [0] * n  # nums[i: i + k]之和
        for i in range(n):
            if i + k <= n:
                ks[i] = s[i + k] - s[i]
            else:
                ks[i] = s[n] - s[i]
        l, r = [[0] * 2] * n, [[0] * 2] * n
        l[0], r[-1] = [ks[0], 0], [ks[-1], n - 1]
        for i in range(1, n):
            if ks[i] > l[i - 1][0]:
                l[i] = [ks[i], i]
            else:
                l[i] = [l[i - 1][0], l[i - 1][1]]
        for i in range(n - 2, -1, -1):
            if ks[i] >= r[i + 1][0]:
                r[i] = [ks[i], i]
            else:
                r[i] = [r[i + 1][0], r[i + 1][1]]
        mx = 0
        # print
        for i in range(k, n - k):
            cur = l[i - k][0] + ks[i] + r[i + k][0]
            if cur > mx:
                ans = [l[i - k][1], i, r[i + k][1]]
                mx = cur
        return ans



so = Solution()
print(so.maxSumOfThreeSubarrays(nums = [1,2,1,2,6,7,5,1], k = 2))
print(so.maxSumOfThreeSubarrays(nums = [1,2,1,2,1,2,1,2,1], k = 2))

