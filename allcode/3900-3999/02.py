

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def passwordStrength(self, password: str) -> int:
        counter = Counter(password)
        ans = 0
        for k in counter:
            if k.islower():
                ans += 1
            elif k.isupper():
                ans += 2
            elif k.isdigit():
                ans += 3
            elif k in '!@#$':
                ans += 5
        return ans


so = Solution()
print(so.removeDigit())




