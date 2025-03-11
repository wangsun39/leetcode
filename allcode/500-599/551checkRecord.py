# 给定一个字符串来代表一个学生的出勤记录，这个记录仅包含以下三个字符：
#
# 'A' : Absent，缺勤
# 'L' : Late，迟到
# 'P' : Present，到场
# 如果一个学生的出勤记录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。
#
# 你需要根据这个学生的出勤记录判断他是否会被奖赏。
#
# 示例 1:
#
# 输入: "PPALLP"
# 输出: True
# 示例 2:
#
# 输入: "PPALLL"
# 输出: False

from leetcode.allcode.competition.mypackage import *


class Solution:
    def checkRecord(self, s: str) -> bool:
        countA = 0
        i, N = 0, len(s)
        while i < N:
            if 'A' == s[i]:
                countA += 1
            if countA > 1:
                return False
            if 'L' == s[i]:
                if s[i:].startswith('LLL'):
                    return False
            i += 1
        return True

so = Solution()
print(so.checkRecord("PPALLP"))
print(so.checkRecord("PPALLL"))

