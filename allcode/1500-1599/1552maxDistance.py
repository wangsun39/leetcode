
from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def check(val):
            start = position[0]
            acc = 1
            for i, x in enumerate(position):
                if x - start >= val:
                    start = x
                    acc += 1
                    if acc == m:
                        return True
            return False
        lo, hi = 0, max(position)
        while lo < hi - 1:
            mid = (lo + hi) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid
        return lo




so = Solution()
print(so.maxDistance(position = [5,4,3,2,1,1000000000], m = 2))
print(so.maxDistance(position = [1,2,3,4,7], m = 3))




