

from leetcode.allcode.competition.mypackage import *

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        ans = 0
        for i in range(n):
            x1, y1 = bottomLeft[i]
            x2, y2 = topRight[i]
            for j in range(i + 1, n):
                u1, v1 = bottomLeft[j]
                u2, v2 = topRight[j]
                if x1 >= u2 or u1 >= x2 or y1 >= v2 or v1 >= y2:
                    continue
                a = sorted([x1, x2, u1, u2])
                b = sorted([y1, y2, v1, v2])
                ans = max(ans, min(a[2] - a[1], b[2] - b[1]))
        return ans


so = Solution()
print(so.largestSquareArea(bottomLeft = [[1,1],[2,2],[3,1]], topRight = [[3,3],[4,4],[6,6]]))
print(so.largestSquareArea(bottomLeft = [[1,1],[2,2],[1,2]], topRight = [[3,3],[4,4],[3,4]]))
print(so.largestSquareArea(bottomLeft = [[1,1],[3,3],[3,1]], topRight = [[2,2],[4,4],[4,2]]))




