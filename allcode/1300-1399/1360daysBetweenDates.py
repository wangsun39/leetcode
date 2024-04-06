# 请你编写一个程序来计算两个日期之间隔了多少天。
#
# 日期以字符串形式给出，格式为 YYYY-MM-DD，如示例所示。
#
#
#
# 示例 1：
#
# 输入：date1 = "2019-06-29", date2 = "2019-06-30"
# 输出：1
# 示例 2：
#
# 输入：date1 = "2020-01-15", date2 = "2019-12-31"
# 输出：15
#
#
# 提示：
#
# 给定的日期是 1971 年到 2100 年之间的有效日期。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def isLeap(year):
            return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
        leap = []
        for y in range(1971, 2101):
            if isLeap(y):
                leap.append(y)
        month = [31,28,31,30,31,30,31,31,30,31,30,31]
        def days(date):
            y, m, d = date.split('-')
            y, m, d = int(y), int(m), int(d)
            p = bisect_left(leap, y)
            res = p + (y - 1971) * 365
            res += sum(month[i] for i in range(m - 1))
            res += d
            if y in leap and m > 2:
                res += 1
            return res
        return abs(days(date1) - days(date2))





so = Solution()
print(so.daysBetweenDates(date1 = "2019-06-29", date2 = "2019-06-30"))
print(so.daysBetweenDates(date1 = "2020-01-15", date2 = "2019-12-31"))




