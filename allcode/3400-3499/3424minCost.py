# 给你两个长度都为 n 的整数数组 arr 和 brr 以及一个整数 k 。你可以对 arr 执行以下操作任意次：
#
# 将 arr 分割成若干个 连续的 子数组，并将这些子数组按任意顺序重新排列。这个操作的代价为 k 。
# 选择 arr 中的任意一个元素，将它增加或者减少一个正整数 x 。这个操作的代价为 x 。
#
# 请你返回将 arr 变为 brr 的 最小 总代价。
#
# 子数组 是一个数组中一段连续 非空 的元素序列。
#
#
#
# 示例 1：
#
# 输入：arr = [-7,9,5], brr = [7,-2,-5], k = 2
#
# 输出：13
#
# 解释：
#
# 将 arr 分割成两个连续子数组：[-7] 和 [9, 5] 然后将它们重新排列成 [9, 5, -7] ，代价为 2 。
# 将 arr[0] 减小 2 ，数组变为 [7, 5, -7] ，操作代价为 2 。
# 将 arr[1] 减小 7 ，数组变为 [7, -2, -7] ，操作代价为 7 。
# 将 arr[2] 增加 2 ，数组变为 [7, -2, -5] ，操作代价为 2 。
# 将两个数组变相等的总代价为 2 + 2 + 7 + 2 = 13 。
#
# 示例 2：
#
# 输入：arr = [2,1], brr = [2,1], k = 0
#
# 输出：0
#
# 解释：
#
# 由于数组已经相等，不需要进行任何操作，所以总代价为 0 。
#
#
#
# 提示：
#
# 1 <= arr.length == brr.length <= 105
# 0 <= k <= 2 * 1010
# -105 <= arr[i] <= 105
# -105 <= brr[i] <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        n = len(arr)
        s1 = sum(abs(arr[i] - brr[i]) for i in range(n))
        arr.sort()
        brr.sort()
        s2 = sum(abs(arr[i] - brr[i]) for i in range(n))
        return min(s1, s2 + k)




so = Solution()
print(so.minCost(arr = [-7,9,5], brr = [7,-2,-5], k = 2))




