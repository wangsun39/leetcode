# 给你两个正整数 n 和 k 。
#
# 如果正整数 i 满足 n % i == 0 ，那么我们就说正整数 i 是整数 n 的因子。
#
# 考虑整数 n 的所有因子，将它们 升序排列 。请你返回第 k 个因子。如果 n 的因子数少于 k ，请你返回 -1 。
#
#
#
# 示例 1：
#
# 输入：n = 12, k = 3
# 输出：3
# 解释：因子列表包括 [1, 2, 3, 4, 6, 12]，第 3 个因子是 3 。
# 示例 2：
#
# 输入：n = 7, k = 2
# 输出：7
# 解释：因子列表包括 [1, 7] ，第 2 个因子是 7 。
# 示例 3：
#
# 输入：n = 4, k = 4
# 输出：-1
# 解释：因子列表包括 [1, 2, 4] ，只有 3 个因子，所以我们应该返回 -1 。
#
#
# 提示：
#
# 1 <= k <= n <= 1000
#
#
# 进阶：
#
# 你可以设计时间复杂度小于 O(n) 的算法来解决此问题吗？

from leetcode.allcode.competition.mypackage import *

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        j = 0
        large = []
        for i in range(1, n + 1):
            if n % i == 0:
                if i * i > n: break
                j += 1
                if j == k:
                    return i
                if i * i < n:
                    large.insert(0, n // i)

        if len(large) + j >= k:
            return large[k - j - 1]
        return -1


so = Solution()
print(so.kthFactor(n = 12, k = 3))
print(so.kthFactor(n = 7, k = 2))
print(so.kthFactor(n = 4, k = 4))




