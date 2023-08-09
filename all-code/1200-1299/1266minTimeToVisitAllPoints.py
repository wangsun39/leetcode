
class Solution:
    def minTimeToVisitAllPoints(self, points):
        if len(points) <= 1:
            return 0
        res = 0
        for idx, p in enumerate(points[1:]):
            res += max(abs(p[0]-points[idx][0]), abs(p[1]-points[idx][1]))
        return res





obj = Solution()
print(obj.minTimeToVisitAllPoints( [[1,1],[3,4],[-1,0]]))
print(obj.minTimeToVisitAllPoints( [[3,2],[-2,2]]))

