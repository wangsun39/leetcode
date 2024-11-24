# 给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。
#
# 例如：
#
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...
#
#
# 示例 1：
#
# 输入：columnNumber = 1
# 输出："A"
# 示例 2：
#
# 输入：columnNumber = 28
# 输出："AB"
# 示例 3：
#
# 输入：columnNumber = 701
# 输出："ZY"
# 示例 4：
#
# 输入：columnNumber = 2147483647
# 输出："FXSHRXW"
#
#
# 提示：
#
# 1 <= columnNumber <= 231 - 1

from leetcode.allcode.competition.mypackage import *


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        i2c = {i: c for i, c in enumerate(ascii_uppercase)}
        ans = []

        while True:
            columnNumber -= 1
            q, r = divmod(columnNumber, 26)
            print(q, r)
            ans.append(i2c[r])
            columnNumber = q
            if columnNumber == 0:
                break
        return ''.join(ans[::-1])


so = Solution()
