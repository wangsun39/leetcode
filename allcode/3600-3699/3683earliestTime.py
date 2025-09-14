

from leetcode.allcode.competition.mypackage import *

min = lambda a, b: b if b < a else a
max = lambda a, b: b if b > a else a

class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        return min(x + y for x, y in tasks)


so = Solution()
print(so.removeDigit())




