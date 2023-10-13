

from leetcode.allcode.competition.mypackage import *

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        n1 = sum(x for x in range(1, n + 1) if x % m != 0)
        n2 = sum(x for x in range(1, n + 1) if x % m == 0)
        return n1 - n2


so = Solution()
print(so.differenceOfSums(n = 10, m = 3))
print(so.differenceOfSums(n = 5, m = 6))




