

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                ss = s[i: j + 1]
                if ss.count('0') <= k or ss.count('1') <= k:
                    ans += 1
        return ans


so = Solution()
print(so.countKConstraintSubstrings(s = "10101", k = 1))
print(so.countKConstraintSubstrings(s = "1010101", k = 2))
print(so.countKConstraintSubstrings(s = "11111", k = 1))




