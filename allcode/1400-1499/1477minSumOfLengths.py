# 给你一个整数数组 arr 和一个整数值 target 。
#
# 请你在 arr 中找 两个互不重叠的子数组 且它们的和都等于 target 。可能会有多种方案，请你返回满足要求的两个子数组长度和的 最小值 。
#
# 请返回满足要求的最小长度和，如果无法找到这样的两个子数组，请返回 -1 。
#
#
#
# 示例 1：
#
# 输入：arr = [3,2,2,4,3], target = 3
# 输出：2
# 解释：只有两个子数组和为 3 （[3] 和 [3]）。它们的长度和为 2 。
# 示例 2：
#
# 输入：arr = [7,3,4,7], target = 7
# 输出：2
# 解释：尽管我们有 3 个互不重叠的子数组和为 7 （[7], [3,4] 和 [7]），但我们会选择第一个和第三个子数组，因为它们的长度和 2 是最小值。
# 示例 3：
#
# 输入：arr = [4,3,2,6,2,3,4], target = 6
# 输出：-1
# 解释：我们只有一个和为 6 的子数组。
# 示例 4：
#
# 输入：arr = [5,5,4,4,5], target = 3
# 输出：-1
# 解释：我们无法找到和为 3 的子数组。
# 示例 5：
#
# 输入：arr = [3,1,1,1,5,1,2,1], target = 3
# 输出：3
# 解释：注意子数组 [1,2] 和 [2,1] 不能成为一个方案因为它们重叠了。
#
#
# 提示：
#
# 1 <= arr.length <= 10^5
# 1 <= arr[i] <= 1000
# 1 <= target <= 10^8

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        s = list(accumulate(arr, initial=0))
        n = len(arr)
        pair = []
        for i in range(n):
            l = s[i]
            r = l + target
            p = bisect_left(s, r)
            if p >= len(s):
                break
            if s[p] == r:
                pair.append([i, p - 1])  # [i, p - 1] 区间和为 target
        if len(pair) <= 1:
            return -1
        minv = [inf] * n  # minv[i] 保持 arr[i+1]开始区间和为target的最小区间长度
        curi = n - 1
        curv = inf
        for l, r in pair[::-1]:
            while curi >= l:
                minv[curi] = curv
                curi -= 1
            curv = min(curv, r - l + 1)
        for i in range(l):
            minv[i] = curv
        ans = inf
        for l, r in pair:
            ans = min(ans, r - l + 1 + minv[r])
        return ans if ans < inf else -1


so = Solution()
print(so.minSumOfLengths(arr = [3,1,1,1,5,1,2,1], target = 3))
print(so.minSumOfLengths(arr = [5,5,4,4,5], target = 3))
print(so.minSumOfLengths(arr = [3,2,2,4,3], target = 3))
print(so.minSumOfLengths(arr = [7,3,4,7], target = 7))
print(so.minSumOfLengths(arr = [4,3,2,6,2,3,4], target = 6))




