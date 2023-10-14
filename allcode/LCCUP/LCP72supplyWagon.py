
from leetcode.allcode.competition.mypackage import *


class Solution:
    def supplyWagon(self, supplies: List[int]) -> List[int]:
        def f(ll):
            m = len(ll)
            mn = inf
            idx = -1
            for i in range(m - 1):
                if ll[i] + ll[i + 1] < mn:
                    mn = ll[i] + ll[i + 1]
                    idx = i
            return ll[:idx] + [mn] + ll[idx + 2:]

        ans = supplies
        n = len(supplies)
        while len(ans) > n // 2:
            ans = f(ans)
        return ans



so = Solution()
print(so.supplyWagon([7,3,6,1,8]))
print(so.supplyWagon( [1,3,1,5]))




