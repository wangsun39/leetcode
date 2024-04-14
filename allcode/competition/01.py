

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findLatestTime(self, s: str) -> str:
        if '?' not in s:
            return s
        if s[0] == '?':
            if s[1] == '?':
                h = '11'
            elif s[1] > '1':
                h = '0' + s[1]
            else:
                h = '1' + s[1]
        else:
            if s[0] == '1':
                h = '1' + (s[1] if s[1] != '?' else '1')
            else:
                h = '0' + (s[1] if s[1] != '?' else '9')
        if s[3] == '?':
            m = '5' + (s[4] if s[4] != '?' else '9')
        else:
            m = s[3] + (s[4] if s[4] != '?' else '9')
        return h + ':' + m





so = Solution()
print(so.findLatestTime("1?:?4"))
print(so.findLatestTime("0?:5?"))




