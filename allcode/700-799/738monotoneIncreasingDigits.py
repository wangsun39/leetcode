# 当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。
#
# 给定一个整数 n ，返回 小于或等于 n 的最大数字，且数字呈 单调递增 。
#
#
#
# 示例 1:
#
# 输入: n = 10
# 输出: 9
# 示例 2:
#
# 输入: n = 1234
# 输出: 1234
# 示例 3:
#
# 输入: n = 332
# 输出: 299
#
#
# 提示:
#
# 0 <= n <= 109


from leetcode.allcode.competition.mypackage import *


class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = list(str(n))
        s = [ord(x) for x in s]
        m = len(s)
        pre = 0
        i = 0
        while i < m - 1:
            if s[i] > s[i + 1]: break
            if s[i] != s[i + 1]:
                pre = i + 1
            i += 1
        if i < m - 1:
            s[pre] -= 1
            for j in range(pre + 1, m):
                s[j] = ord('9')
        s = [chr(x) for x in s]
        return int(''.join(s))


so = Solution()

