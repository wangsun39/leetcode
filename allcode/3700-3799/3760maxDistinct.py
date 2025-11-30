

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def maxDistinct(self, s: str) -> int:
        counter = Counter(s)
        return len(counter)


so = Solution()
print(so.maxDistinct())




