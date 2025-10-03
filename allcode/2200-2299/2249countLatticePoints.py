# 给你一个二维整数数组 circles ，其中 circles[i] = [xi, yi, ri] 表示网格上圆心为 (xi, yi) 且半径为 ri 的第 i 个圆，返回出现在 至少一个 圆内的 格点数目 。
#
# 注意：
#
# 格点 是指整数坐标对应的点。
# 圆周上的点 也被视为出现在圆内的点。
#
#
# 示例 1：
#
#
#
# 输入：circles = [[2,2,1]]
# 输出：5
# 解释：
# 给定的圆如上图所示。
# 出现在圆内的格点为 (1, 2)、(2, 1)、(2, 2)、(2, 3) 和 (3, 2)，在图中用绿色标识。
# 像 (1, 1) 和 (1, 3) 这样用红色标识的点，并未出现在圆内。
# 因此，出现在至少一个圆内的格点数目是 5 。
# 示例 2：
#
#
#
# 输入：circles = [[2,2,2],[3,4,1]]
# 输出：16
# 解释：
# 给定的圆如上图所示。
# 共有 16 个格点出现在至少一个圆内。
# 其中部分点的坐标是 (0, 2)、(2, 0)、(2, 4)、(3, 2) 和 (4, 4) 。
#
#
# 提示：
#
# 1 <= circles.length <= 200
# circles[i].length == 3
# 1 <= xi, yi <= 100
# 1 <= ri <= min(xi, yi)


from leetcode.allcode.competition.mypackage import *

class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        n = len(circles)
        y_mx = max(y + r for _, y, r in circles)
        y_mn = min(y - r for _, y, r in circles)
        x_mx = max(x + r for x, _, r in circles)
        x_mn = min(x - r for x, _, r in circles)
        ans = 0
        for y in range(y_mn, y_mx + 1):
            diff = [0] * (x_mx - x_mn + 2)  #  差分数组
            for x0, y0, r in circles:
                if r < abs(y0 - y): continue
                sq = (r * r - (y0 - y) * (y0 - y)) ** 0.5
                x1, x2 = ceil(x0 - sq) - x_mn, floor(x0 + sq) - x_mn
                diff[x1] += 1
                diff[x2 + 1] -= 1
            s = 0  # 前缀和
            for x in diff[:-1]:
                s += x
                if s:
                    ans += 1
        return ans


so = Solution()
print(so.countLatticePoints(circles = [[2,2,2],[3,4,1]]))  # 16
print(so.countLatticePoints(circles = [[2,2,1]]))


