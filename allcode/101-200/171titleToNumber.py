# 给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回 该列名称对应的列序号 。
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
# 示例 1:
#
# 输入: columnTitle = "A"
# 输出: 1
# 示例 2:
#
# 输入: columnTitle = "AB"
# 输出: 28
# 示例 3:
#
# 输入: columnTitle = "ZY"
# 输出: 701
#
#
# 提示：
#
# 1 <= columnTitle.length <= 7
# columnTitle 仅由大写英文组成
# columnTitle 在范围 ["A", "FXSHRXW"] 内

from leetcode.allcode.competition.mypackage import *


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        c2i = {c: i for i, c in enumerate(ascii_uppercase)}
        n = len(columnTitle)
        ans = 0
        for i in range(n - 1, -1, -1):
            ans += (c2i[columnTitle[i]] + 1) * (26 ** (n - 1 - i))
        return ans


so = Solution()
print(so.titleToNumber(columnTitle = "AB"))
print(so.titleToNumber(columnTitle = "A"))
