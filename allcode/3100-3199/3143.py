

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        dist = []
        for x, y in points:
            dist.append(max((abs(x), abs(y))))
        s = list(s)
        z = zip(dist, s)
        z = sorted(list(z))
        cur = z[0][0]
        tag = set()
        ans = 0
        acc = 0
        for d, t in z:
            if cur == d:
                acc += 1
            else:
                ans += acc
                cur = d
                acc = 1
            if t in tag:
                return ans
            tag.add(t)
        return ans + acc



so = Solution()
print(so.maxPointsInsideSquare(points = [[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]], s = "abdca"))
print(so.maxPointsInsideSquare(points = [[1,1],[-2,-2],[-2,2]], s = "abb"))
print(so.maxPointsInsideSquare(points = [[1,1],[-1,-1],[2,-2]], s = "ccd"))




