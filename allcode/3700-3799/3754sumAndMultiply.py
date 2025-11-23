

from leetcode.allcode.competition.mypackage import *

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = list(str(n))
        s = [x for x in s if x != '0']
        if len(s) == 0: return 0
        n1 = int(''.join(s))
        n2 = sum(int(x) for x in s)
        return n1 * n2



so = Solution()




