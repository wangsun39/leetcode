# 给你一个整数 n，请你每隔三位添加点（即 "." 符号）作为千位分隔符，并将结果以字符串格式返回。
#
#
#
# 示例 1：
#
# 输入：n = 987
# 输出："987"
# 示例 2：
#
# 输入：n = 1234
# 输出："1.234"
# 示例 3：
#
# 输入：n = 123456789
# 输出："123.456.789"
# 示例 4：
#
# 输入：n = 0
# 输出："0"
#
#
# 提示：
#
# 0 <= n < 2^31

from leetcode.allcode.competition.mypackage import *

class Solution:
    def thousandSeparator(self, n: int) -> str:
        l = list(str(n))
        n = len(l)
        ans = []
        for i in range(n):
            j = n - 1 - i
            ans.append(l[j])
            if (i + 1) % 3 == 0 and i < n - 1:
                ans.append('.')
        return ''.join(ans[::-1])


so = Solution()
print(so.thousandSeparator(987))
print(so.thousandSeparator(1234))
print(so.thousandSeparator(123456789))




