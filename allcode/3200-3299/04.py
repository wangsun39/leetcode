

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        ss = [0]
        for x in s:
            if x == '1':
                ss.append(ss[-1] + 1)
            else:
                ss.append(ss[-1])
        ans = []
        for l, r in queries:
            ones = ss[r + 1] - ss[l]
            zeros = r - l + 1 - ones
            if ones <= k or zeros <= k:
                ans.append()


so = Solution()
print(so.countKConstraintSubstrings())




