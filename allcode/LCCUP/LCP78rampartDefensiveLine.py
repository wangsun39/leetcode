
from leetcode.allcode.competition.mypackage import *


class Solution:
    def rampartDefensiveLine(self, rampart: List[List[int]]) -> int:
        n = len(rampart)
        space = []
        for i in range(1, n):
            v = rampart[i][0] - rampart[i - 1][1]
            space.append(v)
        # print(space)
        lo, hi = min(space), space[0] + space[1]
        def check(x):
            sp = [y for y in space]
            l, r = 0, n - 2
            while l < r:
                if sp[l] >= x:
                    sp[l] -= x
                elif sp[l + 1] >= x - sp[l]:
                    sp[l + 1] -= (x - sp[l])
                else:
                    return False
                if l + 1 == r: break
                if sp[r] >= x:
                    sp[r] -= x
                elif sp[r - 1] >= x - sp[r]:
                    sp[r - 1] -= (x - sp[r])
                else:
                    return False
                l += 1
                r -= 1
            return True
        if check(hi): return hi
        while lo < hi - 1:
            mid = (lo + hi) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid
        return lo



so = Solution()
print(so.rampartDefensiveLine([[0,3],[4,5],[7,9]]))
print(so.rampartDefensiveLine([[3,5],[12,29],[31,38],[39,42],[43,44],[46,47]]))
print(so.rampartDefensiveLine([[1,2],[5,8],[11,15],[18,25]]))




