

from leetcode.allcode.competition.mypackage import *

class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        s1, s2, s3 = str(num1), str(num2), str(num3)
        s1 = '0' * (4 - len(s1)) + s1
        s2 = '0' * (4 - len(s2)) + s2
        s3 = '0' * (4 - len(s3)) + s3
        res = []
        for i in range(4):
            res.append(min(s1[i], s2[i], s3[i]))
        return int(''.join(res))



so = Solution()
print(so.generateKey( num1 = 987, num2 = 879, num3 = 798))
print(so.generateKey( num1 = 1, num2 = 2, num3 = 3))




