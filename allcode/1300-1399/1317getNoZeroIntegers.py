# 「无零整数」是十进制表示中 不含任何 0 的正整数。
#
# 给你一个整数 n，请你返回一个 由两个整数组成的列表 [a, b]，满足：
#
# a 和 b 都是无零整数
# a + b = n
# 题目数据保证至少有一个有效的解决方案。
#
# 如果存在多个有效解决方案，你可以返回其中任意一个。
#
#
#
# 示例 1：
#
# 输入：n = 2
# 输出：[1,1]
# 解释：a = 1, b = 1。a + b = n 并且 a 和 b 的十进制表示形式都不包含任何 0。
# 示例 2：
#
# 输入：n = 11
# 输出：[2,9]
# 示例 3：
#
# 输入：n = 10000
# 输出：[1,9999]
# 示例 4：
#
# 输入：n = 69
# 输出：[1,68]
# 示例 5：
#
# 输入：n = 1010
# 输出：[11,999]
#
#
# 提示：
#
# 2 <= n <= 104

from leetcode.allcode.competition.mypackage import *

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def check(x):
            while x:
                q, r = divmod(x, 10)
                if r == 0: return False
                x = q
            return True
        for i in range(1, n):
            if check(i) and check(n - i):
                return [i, n - i]


so = Solution()
print(so.getNoZeroIntegers(11))


