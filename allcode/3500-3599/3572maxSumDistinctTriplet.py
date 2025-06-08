# 给你两个整数数组 x 和 y，长度均为 n。你必须选择三个 不同 的下标 i ，j 和 k，满足以下条件：
#
# x[i] != x[j]
# x[j] != x[k]
# x[k] != x[i]
# 你的目标是在满足这些条件下 最大化 y[i] + y[j] + y[k] 的值。返回通过选择这样一组三元组下标所能获得的 最大 可能和。
#
# 如果不存在这样的三元组，返回 -1。
#
#
#
# 示例 1：
#
# 输入：x = [1,2,1,3,2], y = [5,3,4,6,2]
#
# 输出：14
#
# 解释：
#
# 选择 i = 0（x[i] = 1，y[i] = 5），j = 1（x[j] = 2，y[j] = 3），k = 3（x[k] = 3，y[k] = 6）。
# 选出的三个 x 中的值互不相同。5 + 3 + 6 = 14 是我们能获得的最大值。因此输出为 14。
# 示例 2：
#
# 输入：x = [1,2,1,2], y = [4,5,6,7]
#
# 输出：-1
#
# 解释：
#
# x 中只有两个不同的值。因此输出为 -1。
#
#
# 提示：
#
# n == x.length == y.length
# 3 <= n <= 105
# 1 <= x[i], y[i] <= 106

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        n = len(x)
        dd = defaultdict(int)
        for i in range(n):
            dd[x[i]] = max(dd[x[i]], y[i])
        if len(dd) < 3:
            return -1
        res = list(dd.values())
        res.sort(reverse=True)
        return sum(res[:3])



so = Solution()
print(so.maxSumDistinctTriplet())




