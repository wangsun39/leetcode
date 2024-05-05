# 给你一个字符串 date ，按 YYYY-MM-DD 格式表示一个 现行公元纪年法 日期。返回该日期是当年的第几天。
#
#
#
# 示例 1：
#
# 输入：date = "2019-01-09"
# 输出：9
# 解释：给定日期是2019年的第九天。
# 示例 2：
#
# 输入：date = "2019-02-10"
# 输出：41
#
#
# 提示：
#
# date.length == 10
# date[4] == date[7] == '-'，其他的 date[i] 都是数字
# date 表示的范围从 1900 年 1 月 1 日至 2019 年 12 月 31 日

from leetcode.allcode.competition.mypackage import *

class Solution:
    def dayOfYear(self, date: str) -> int:
        [year, month, day] = date.split('-')
        year, month, day = int(year), int(month), int(day)
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = 0
        if (0 == year % 4 and year % 100 != 0) or (0 == year % 400):
            if month > 2:
                days += sum(months[:month - 1]) + 1
            else:
                days += sum(months[:month - 1])
            days += day
        else:
            days += sum(months[:month - 1])
            days += day
        return days


so = Solution()




