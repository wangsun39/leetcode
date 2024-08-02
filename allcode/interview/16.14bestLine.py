# 给定一个二维平面及平面上的 N 个点列表Points，其中第i个点的坐标为Points[i]=[Xi,Yi]。请找出一条直线，其通过的点的数目最多。
#
# 设穿过最多点的直线所穿过的全部点编号从小到大排序的列表为S，你仅需返回[S[0],S[1]]作为答案，若有多条直线穿过了相同数量的点，则选择S[0]值较小的直线返回，S[0]相同则选择S[1]值较小的直线返回。
#
# 示例：
#
# 输入： [[0,0],[1,1],[1,0],[2,0]]
# 输出： [0,2]
# 解释： 所求直线穿过的3个点的编号为[0,2,3]
# 提示：
#
# 2 <= len(Points) <= 300
# len(Points[i]) = 2

from leetcode.allcode.competition.mypackage import *

class Solution:
    def bestLine(self, points: List[List[int]]) -> List[int]:
        n = len(points)
        mx = 0
        for i in range(n):
            x0, y0 = points[i]
            for j in range(i + 1, n):
                x1, y1 = points[j]
                cnt = 2
                for k in range(j + 1, n):
                    x2, y2 = points[k]
                    if (y1 - y0) * (x2 - x0) == (y2 - y0) * (x1 - x0):
                        cnt += 1
                if cnt > mx:
                    mx = cnt
                    ans = [i, j]
        return ans

so = Solution()
print(so.bestLine([[0,0],[1,1],[1,0],[2,0]]))





