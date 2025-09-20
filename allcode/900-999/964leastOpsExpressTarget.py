# 给定一个正整数 x，我们将会写出一个形如 x (op1) x (op2) x (op3) x ... 的表达式，其中每个运算符 op1，op2，… 可以是加、减、乘、除（+，-，*，或是 /）之一。例如，对于 x = 3，我们可以写出表达式 3 * 3 / 3 + 3 - 3，该式的值为 3 。
#
# 在写这样的表达式时，我们需要遵守下面的惯例：
#
# 除运算符（/）返回有理数。
# 任何地方都没有括号。
# 我们使用通常的操作顺序：乘法和除法发生在加法和减法之前。
# 不允许使用一元否定运算符（-）。例如，“x - x” 是一个有效的表达式，因为它只使用减法，但是 “-x + x” 不是，因为它使用了否定运算符。
# 我们希望编写一个能使表达式等于给定的目标值 target 且运算符最少的表达式。返回所用运算符的最少数量。
#
#
#
# 示例 1：
#
# 输入：x = 3, target = 19
# 输出：5
# 解释：3 * 3 + 3 * 3 + 3 / 3 。表达式包含 5 个运算符。
# 示例 2：
#
# 输入：x = 5, target = 501
# 输出：8
# 解释：5 * 5 * 5 * 5 - 5 * 5 * 5 + 5 / 5 。表达式包含 8 个运算符。
# 示例 3：
#
# 输入：x = 100, target = 100000000
# 输出：3
# 解释：100 * 100 * 100 * 100 。表达式包含 3 个运算符。
#
#
# 提示：
#
# 2 <= x <= 100
# 1 <= target <= 2 * 108

from leetcode.allcode.competition.mypackage import *

class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        # target = an * x ^ n + an-1 * x ^ (n-1) + ... + a1 * x + a0
        # -x < ai < x
        # 求某一组ai，使得上式成立，且用到的x最少，总共用到x的数量为 an * n + an-1 * (n-1) + a1 * 1 + a0 * 2   因为a0 = a0 * (x/x)
        # 用 DP 求解
        @cache
        def dfs(t, i):
            # 上式从右向左依次计算，模 x 之后的数，余数按向下取整和向上取整两种方式，依次递归dfs(q,i+1)和dfs(q+1,i+1)
            # dfs返回的是 t * (x ^ i) 对应的数，最少需要由多少个x组合而成
            if t == 0: return 0
            if t % x == 0:
                return dfs(t // x, i + 1)
            q, r = divmod(t, x)
            if t < x:
                return min(r * i, (i + 1) + (x - r) * i)
            res = min(dfs(q, i + 1) + r * i, dfs(q + 1, i + 1) + (x - r) * i)
            return res

        q, r = divmod(target, x)
        ans = min(dfs(q, 1) + r * 2, dfs(q + 1, 1) + (x - r) * 2)
        return ans - 1

so = Solution()
print(so.leastOpsExpressTarget(x = 3, target = 19))   # 5
print(so.leastOpsExpressTarget(x = 5, target = 125))   # 2
print(so.leastOpsExpressTarget(x = 5, target = 501))   # 8
print(so.leastOpsExpressTarget(x = 5, target = 4))  # 2




