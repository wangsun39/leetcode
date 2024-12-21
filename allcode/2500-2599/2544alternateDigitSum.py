
from leetcode.allcode.competition.mypackage import *

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = str(n)
        sign = 1
        ans = 0
        for ss in s:
            ans += (int(ss) * sign)
            sign = -sign
        return ans


so = Solution()
print(so.alternateDigitSum(521))
print(so.alternateDigitSum(111))
print(so.alternateDigitSum(886996))




