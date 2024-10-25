

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = set()
        n = len(digits)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j != k != i and digits[i] != 0 and digits[k] & 1 == 0:
                        v = digits[i] * 100 + digits[j] * 10 + digits[k]
                        ans.add(v)
        return sorted(list(ans))


so = Solution()
print(so.findEvenNumbers(digits = [2,1,3,0]))
print(so.findEvenNumbers(digits = [2,2,8,8,2]))




