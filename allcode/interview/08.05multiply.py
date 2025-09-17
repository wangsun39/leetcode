# 递归乘法。 写一个递归函数，不使用 * 运算符， 实现两个正整数的相乘。可以使用加号、减号、位移，但要吝啬一些。
#
# 示例 1：
#
#  输入：A = 1, B = 10
#  输出：10
# 示例 2：
#
#  输入：A = 3, B = 4
#  输出：12
# 提示：
#
# 保证乘法范围不会溢出

from leetcode.allcode.competition.mypackage import *

class Solution:
    def multiply(self, A: int, B: int) -> int:

        def dfs(A, B, shift):
            if B == 0: return 0
            if B & 1:
                return (A << shift) + dfs(A, B >> 1, shift + 1)
            return dfs(A, B >> 1, shift + 1)

        return dfs(A, B, 0)



so = Solution()
print(so.multiply(A = 1, B = 10))




