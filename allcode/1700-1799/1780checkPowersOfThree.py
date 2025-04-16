# 给你一个整数 n ，如果你可以将 n 表示成若干个不同的三的幂之和，请你返回 true ，否则请返回 false 。
#
# 对于一个整数 y ，如果存在整数 x 满足 y == 3x ，我们称这个整数 y 是三的幂。
#
#
#
# 示例 1：
#
# 输入：n = 12
# 输出：true
# 解释：12 = 31 + 32
# 示例 2：
#
# 输入：n = 91
# 输出：true
# 解释：91 = 30 + 32 + 34
# 示例 3：
#
# 输入：n = 21
# 输出：false
#
#
# 提示：
#
# 1 <= n <= 107




from leetcode.allcode.competition.mypackage import *

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        l = [3 ** i for i in range(16)]
        for i in range(1, 2 ** 16):
            s = 0
            for j in range(16):
                if (i >> j) & 1:
                    s += l[j]
                    if s == n:
                        return True
                    if s > n:
                        break
        return False



so = Solution()
print(so.checkPowersOfThree(12))  # T
print(so.checkPowersOfThree(91))  # T
print(so.checkPowersOfThree(21))  # F




