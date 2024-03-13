# 给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。
#
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 给定 n 和 k，返回第 k 个排列。
#
#
#
# 示例 1：
#
# 输入：n = 3, k = 3
# 输出："213"
# 示例 2：
#
# 输入：n = 4, k = 9
# 输出："2314"
# 示例 3：
#
# 输入：n = 3, k = 1
# 输出："123"
#
#
# 提示：
#
# 1 <= n <= 9
# 1 <= k <= n!

from leetcode.allcode.competition.mypackage import *

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        order = [1]  # 阶乘
        for i in range(2, 10):
            order.append(order[-1] * i)

        def dfs(cand, kk):   # cand是可选的数字的有序list，在此中选出，第kk大的结果，kk从0开始
            m = len(cand)
            if m == 1:
                return str(cand[kk])
            q, r = divmod(kk, order[m - 2])
            return str(cand[q]) + dfs(cand[:q] + cand[q + 1:], r)
        return dfs(list(range(1, n + 1)), k - 1)


so = Solution()
print(so.getPermutation(n = 3, k = 3))
print(so.getPermutation(n = 4, k = 9))
print(so.getPermutation(n = 3, k = 1))




