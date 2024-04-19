

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        x = [a for a, _ in points]
        x.sort()
        ans = 0
        i, n = 0, len(x)
        while i < n:
            l = i
            r = l
            while r < n and x[r] - x[l] <= w:
                r += 1
            ans += 1
            i = r
        return ans


so = Solution()
print(so.minRectanglesToCoverPoints(points = [[2,1],[1,0],[1,4],[1,8],[3,5],[4,6]], w = 1))
print(so.minRectanglesToCoverPoints(points = [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]], w = 2))
print(so.minRectanglesToCoverPoints(points = [[2,3],[1,2]], w = 0))




