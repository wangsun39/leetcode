# 给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。
#
# 输入为三个整数：day、month 和 year，分别表示日、月、年。
#
# 您返回的结果必须是这几个值中的一个 {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}。
#
#
#
# 示例 1：
#
# 输入：day = 31, month = 8, year = 2019
# 输出："Saturday"
# 示例 2：
#
# 输入：day = 18, month = 7, year = 1999
# 输出："Sunday"
# 示例 3：
#
# 输入：day = 15, month = 8, year = 1993
# 输出："Sunday"
#
#
# 提示：
#
# 给出的日期一定是在 1971 到 2100 年之间的有效日期。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        leap = []
        for i in range(1971, 2101):
            if (0 == i % 4 and i % 100 != 0) or (0 == i % 400):
                leap.append(i)
        p = bisect_left(leap, year)
        days = (year - 1971) * 365 + p
        if year in leap:
            if month > 2:
                days += sum(months[:month - 1]) + 1
            else:
                days += sum(months[:month - 1])
            days += day
        else:
            days += sum(months[:month - 1])
            days += day
        days %= 7
        return week[(days + 4) % 7]  # 1970.12.31 is Thursday


so = Solution()
print(so.dayOfTheWeek(day = 1, month = 1, year = 1971))
print(so.dayOfTheWeek(day = 31, month = 8, year = 2019))
print(so.dayOfTheWeek(day = 18, month = 7, year = 1999))
print(so.dayOfTheWeek(day = 15, month = 8, year = 1993))




