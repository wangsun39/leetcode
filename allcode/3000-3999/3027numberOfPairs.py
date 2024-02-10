# 给你一个  n x 2 的二维数组 points ，它表示二维平面上的一些点坐标，其中 points[i] = [xi, yi] 。
#
# 我们定义 x 轴的正方向为 右 （x 轴递增的方向），x 轴的负方向为 左 （x 轴递减的方向）。类似的，我们定义 y 轴的正方向为 上 （y 轴递增的方向），y 轴的负方向为 下 （y 轴递减的方向）。
#
# 你需要安排这 n 个人的站位，这 n 个人中包括 liupengsay 和小羊肖恩 。你需要确保每个点处 恰好 有 一个 人。同时，liupengsay 想跟小羊肖恩单独玩耍，所以 liupengsay 会以 liupengsay 的坐标为 左上角 ，小羊肖恩的坐标为 右下角 建立一个矩形的围栏（注意，围栏可能 不 包含任何区域，也就是说围栏可能是一条线段）。如果围栏的 内部 或者 边缘 上有任何其他人，liupengsay 都会难过。
#
# 请你在确保 liupengsay 不会 难过的前提下，返回 liupengsay 和小羊肖恩可以选择的 点对 数目。
#
# 注意，liupengsay 建立的围栏必须确保 liupengsay 的位置是矩形的左上角，小羊肖恩的位置是矩形的右下角。比方说，以 (1, 1) ，(1, 3) ，(3, 1) 和 (3, 3) 为矩形的四个角，给定下图的两个输入，liupengsay 都不能建立围栏，原因如下：
#
# 图一中，liupengsay 在 (3, 3) 且小羊肖恩在 (1, 1) ，liupengsay 的位置不是左上角且小羊肖恩的位置不是右下角。
# 图二中，liupengsay 在 (1, 3) 且小羊肖恩在 (1, 1) ，小羊肖恩的位置不是在围栏的右下角。
#
#
#
# 示例 1：
#
#
#
# 输入：points = [[1,1],[2,2],[3,3]]
# 输出：0
# 解释：没有办法可以让 liupengsay 的围栏以 liupengsay 的位置为左上角且小羊肖恩的位置为右下角。所以我们返回 0 。
# 示例 2：
#
#
#
# 输入：points = [[6,2],[4,4],[2,6]]
# 输出：2
# 解释：总共有 2 种方案安排 liupengsay 和小羊肖恩的位置，使得 liupengsay 不会难过：
# - liupengsay 站在 (4, 4) ，小羊肖恩站在 (6, 2) 。
# - liupengsay 站在 (2, 6) ，小羊肖恩站在 (4, 4) 。
# 不能安排 liupengsay 站在 (2, 6) 且小羊肖恩站在 (6, 2) ，因为站在 (4, 4) 的人处于围栏内。
# 示例 3：
#
#
#
# 输入：points = [[3,1],[1,3],[1,1]]
# 输出：2
# 解释：总共有 2 种方案安排 liupengsay 和小羊肖恩的位置，使得 liupengsay 不会难过：
# - liupengsay 站在 (1, 1) ，小羊肖恩站在 (3, 1) 。
# - liupengsay 站在 (1, 3) ，小羊肖恩站在 (1, 1) 。
# 不能安排 liupengsay 站在 (1, 3) 且小羊肖恩站在 (3, 1) ，因为站在 (1, 1) 的人处于围栏内。
# 注意围栏是可以不包含任何面积的，上图中第一和第二个围栏都是合法的。
#
#
# 提示：
#
# 2 <= n <= 1000
# points[i].length == 2
# -109 <= points[i][0], points[i][1] <= 109
# points[i] 点对两两不同。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: [x[0], -x[1]])
        ans = 0
        for i, [_, y] in enumerate(points):
            q = []
            for j, [u, v] in enumerate(points[i + 1:], i + 1):
                if v > y: continue
                if q and (q[-1][0] == u or q[-1][1] >= v): continue
                q.append([u, v])
            ans += len(q)
        return ans




so = Solution()
print(so.numberOfPairs([[6,2],[4,4],[2,6]]))
print(so.numberOfPairs([[1,1],[2,2],[3,3]]))
print(so.numberOfPairs([[3,1],[1,3],[1,1]]))




