# 给你一个 严格升序排列 的正整数数组 arr 和一个整数 k 。
#
# 请你找到这个数组里第 k 个缺失的正整数。
#
#
#
# 示例 1：
#
# 输入：arr = [2,3,4,7,11], k = 5
# 输出：9
# 解释：缺失的正整数包括 [1,5,6,8,9,10,12,13,...] 。第 5 个缺失的正整数为 9 。
# 示例 2：
#
# 输入：arr = [1,2,3,4], k = 2
# 输出：6
# 解释：缺失的正整数包括 [5,6,7,...] 。第 2 个缺失的正整数为 6 。
#
#
# 提示：
#
# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000
# 1 <= k <= 1000
# 对于所有 1 <= i < j <= arr.length 的 i 和 j 满足 arr[i] < arr[j]
#
#
# 进阶：
#
# 你可以设计一个时间复杂度小于 O(n) 的算法解决此问题吗？

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if arr[-1] < n + k:
            return n + k
        if arr[0] > k:
            return k

        lo, hi = 0, n
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if arr[mid] - (mid + 1) >= k:
                hi = mid
            else:
                lo = mid
        # 从 arr[hi - 1] 向后，它之前已经小的数量与目标k的差值 delta，答案就是 arr[hi - 1] + delta
        return arr[hi - 1] + k - (arr[hi - 1] - hi)


so = Solution()
print(so.findKthPositive(arr = [2], k = 1))
print(so.findKthPositive(arr = [2,3,4,7,11], k = 5))



