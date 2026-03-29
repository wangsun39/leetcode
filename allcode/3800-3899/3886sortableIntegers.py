# 给你一个长度为 n 的整数数组 nums。
#
# 如果一个整数 k 满足以下条件，则称其为 可排序整数：k 是 n 的 因数，且可以通过依次执行以下操作将 nums 排序为 非递减顺序：
#
# 将 nums 划分为长度为 k 的 连续子数组。
# 独立地对每个子数组进行循环移动（左移或右移任意次数）。
# 返回所有可能的可排序整数 k 的和。
#
# 子数组 是数组中的一个连续、非空元素序列。
#
#
# 示例 1：
#
# 输入： nums = [3,1,2]
#
# 输出： 3
#
# 解释：
#
# 对于 n = 3，可能的因数是 1 和 3。
# 对于 k = 1：每个子数组都只有一个元素。无法通过移动使数组排序。
# 对于 k = 3：单个子数组 [3, 1, 2] 可以通过左移一次得到 [1, 2, 3]，从而将数组排序。
# 只有 k = 3 可排序，因此答案是 3。
# 示例 2：
#
# 输入： nums = [7,6,5]
#
# 输出： 0
#
# 解释：
#
# 对于 n = 3，可能的因数是 1 和 3。
# 对于 k = 1：每个子数组都只有一个元素。无法通过移动使数组排序。
# 对于 k = 3：单个子数组 [7, 6, 5] 无法通过任何移动排序为非递减顺序。
# 没有任何可排序的 k，因此答案是 0。
# 示例 3：
#
# 输入： nums = [5,8]
#
# 输出： 3
#
# 解释：
#
# 对于 n = 2，可能的因数是 1 和 2。
# 由于 [5, 8] 本身已经有序，每个因数都可排序。
# 因此答案是 1 + 2 = 3。
#
#
# 提示：
#
# 1 <= n == nums.length <= 105
# 1 <= nums[i] <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)

        def factors(x):
            res = []
            i = 1
            while i * i <= x:
                if x % i == 0:
                    res.append(i)
                    if i * i != x:
                        res.append(x // i)
                i += 1
            return res

        divisors = factors(n)

        def k_sortable(k: int) -> bool:
            prev_max = None
            for b in range(0, n, k):
                block_first = pre = mn = mx = nums[b]
                desc = 0

                for idx in range(b + 1, b + k):
                    cur = nums[idx]
                    if pre > cur:
                        desc += 1
                        if desc > 1:
                            return False
                    if cur < mn:
                        mn = cur
                    if cur > mx:
                        mx = cur
                    pre = cur

                if pre > block_first:
                    desc += 1
                    if desc > 1:
                        return False

                if prev_max is not None and prev_max > mn:
                    return False
                prev_max = mx
            return True

        ans = 0
        for k in divisors:
            if k_sortable(k):
                ans += k
        return ans


so = Solution()
print(so.sortableIntegers([3,1,2]))




