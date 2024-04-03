

from leetcode.allcode.competition.mypackage import *

class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = 0
        y = x
        while x:
            s += (x % 10)
            x //= 10
        return s if y % s == 0 else -1


so = Solution()
print(so.sumOfTheDigitsOfHarshadNumber(18))
print(so.sumOfTheDigitsOfHarshadNumber(23))




