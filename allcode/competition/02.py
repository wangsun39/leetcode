

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        s = sum(-1 if x == 0 else 1 for x in possible)
        ss = 0
        for i, x in enumerate(possible[:-1]):
            ss += (-1 if x == 0 else 1)
            if ss > s - ss:
                return i + 1
        return -1


so = Solution()
print(so.minimumLevels([0,0]))
print(so.minimumLevels([1,1,1,1,1]))
print(so.minimumLevels([1,0,1,0]))




