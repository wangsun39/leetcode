# 「力扣挑战赛」场地外，小力组织了一个套玩具的游戏。所有的玩具摆在平地上，toys[i]
# 以[xi, yi, ri]
# 的形式记录了第
# i
# 个玩具的坐标(xi, yi)
# 和半径
# ri。小扣试玩了一下，他扔了若干个半径均为
# r
# 的圈，circles[j]
# 记录了第
# j
# 个圈的坐标(xj, yj)。套圈的规则如下：
#
# 若一个玩具被某个圈完整覆盖了（即玩具的任意部分均在圈内或者圈上），则该玩具被套中。
# 若一个玩具被多个圈同时套中，最终仅计算为套中一个玩具
# 请帮助小扣计算，他成功套中了多少玩具。
#
# 注意：
#
# 输入数据保证任意两个玩具的圆心不会重合，但玩具之间可能存在重叠。
# 示例
# 1：
#
# 输入：toys = [[3, 3, 1], [3, 2, 1]], circles = [[4, 3]], r = 2
#
# 输出：1
#
# 解释： 如图所示，仅套中一个玩具
#
# 示例
# 2：
#
# 输入：toys = [[1, 3, 2], [4, 3, 1], [7, 1, 2]], circles = [[1, 0], [3, 3]], r = 4
#
# 输出：2
#
# 解释： 如图所示，套中两个玩具
#
# 提示：
#
# 1 <= toys.length <= 10 ^ 4
# 0 <= toys[i][0], toys[i][1] <= 10 ^ 9
# 1 <= circles.length <= 10 ^ 4
# 0 <= circles[i][0], circles[i][1] <= 10 ^ 9
# 1 <= toys[i][2], r <= 10
#
# https: // leetcode.cn / problems / vFjcfV




from leetcode.allcode.competition.mypackage import *

class Solution:
    def circleGame(self, toys: List[List[int]], circles: List[List[int]], r: int) -> int:
        toys = [e for e in toys if e[2] <= r]
        dx = defaultdict(list)
        for idx, toy in enumerate(toys):
            dx[toy[0]].append([toy[1], idx])
        for k in dx:
            dx[k].sort()
        def cover(x, y, x2, y2, r2):
            return (x - x2) ** 2 + (y - y2) ** 2 <= (r - r2) ** 2
        cov = set()
        def check(x, cir):
            c1, c2 = cir[0], cir[1]
            y1 = bisect.bisect_left(dx[x], [c2 - r, 0])
            y2 = bisect.bisect_right(dx[x], [c2 + r, 1e10])
            for y in range(y1, y2):
                if len(dx[x]) == 0 or dx[x][y][1] in cov:
                    continue
                if cover(c1, c2, x, dx[x][y][0], toys[dx[x][y][1]][2]):
                    cov.add(dx[x][y][1])

        for cir in circles:
            for x in range(cir[0] - r + 1, cir[0] + r):
                check(x, cir)
        for e in cov: print(toys[e])
        return len(cov)


so = Solution()

print(so.circleGame(toys= [[67, 18, 1]], circles = [[65, 18]], r = 3))  # 1
print(so.circleGame([[89,29,4],[68,8,3],[49,76,5],[87,83,5],[91,78,4],[27,66,4],[81,20,10],[43,82,7],[46,57,5],[29,39,5],[47,12,9],[62,14,3],[37,18,9],[63,87,5],[53,56,3],[72,73,7],[26,44,4],[64,88,2],[24,7,3],[34,45,8],[50,35,2],[72,28,10],[15,88,10],[78,94,8],[15,4,7],[61,49,6],[20,69,2],[36,63,5],[97,1,3],[24,36,5],[78,28,6],[49,66,2],[80,79,8],[15,66,9],[96,92,2],[61,71,10],[61,98,1],[85,42,3],[68,86,2],[4,86,5],[40,66,2],[69,14,9],[67,18,1],[23,15,8],[46,1,7],[10,25,3],[52,5,2],[51,62,5],[62,37,1],[11,40,4],[55,80,8],[0,13,4],[5,91,10],[8,76,1],[4,7,9],[47,6,1],[38,13,2],[54,76,4],[56,33,10],[18,84,3],[62,100,3],[34,37,6],[67,40,2],[82,100,9],[52,37,5],[59,82,5],[99,98,4],[7,1,8],[15,92,9],[97,88,9],[29,40,4],[0,40,7],[84,42,5],[11,99,1],[11,47,2],[56,38,9],[29,81,5],[16,92,10],[75,10,10],[68,1,6],[61,47,7],[22,53,3],[67,6,1],[96,100,9],[5,13,7],[90,94,8],[35,87,2],[12,70,9],[21,1,5],[40,33,5],[89,15,2],[28,52,10],[22,67,1],[86,8,2],[38,40,4],[13,82,3],[16,91,7],[36,60,1],[78,52,7],[48,91,4]],
[[66,24],[51,85],[99,92],[59,53],[92,98],[79,84],[98,97],[80,63],[2,98],[19,100],[14,7],[86,94],[32,25],[58,88],[87,22],[37,9],[12,76],[35,3],[92,64],[51,78],[94,69],[70,39],[99,41],[32,40],[63,63],[0,45],[11,43],[6,91],[40,47],[87,30],[37,9],[55,71],[56,42],[5,66],[65,18],[91,48],[36,21],[94,18],[17,61],[75,63],[78,46],[22,7],[77,3],[24,67],[29,84],[66,97],[41,77],[42,78],[1,63],[100,67],[15,45],[45,33],[41,44],[96,73],[33,71],[92,35],[26,0],[81,47],[49,95],[15,49],[80,62],[11,76],[38,76],[45,34],[16,31],[67,66],[60,98],[95,46],[52,60],[53,66],[3,76],[68,82],[40,75],[0,24],[41,21],[62,84],[51,25],[21,45],[58,36],[59,38],[7,6],[8,53],[4,71],[53,88],[86,49],[41,22],[32,82],[43,14],[80,1],[24,81],[93,37],[51,47],[34,5],[1,61],[89,7],[62,0],[46,3],[56,37],[19,93],[44,45]],
3))  # 3
print(so.circleGame([[3,3,8],[3,6,3],[1,7,9],[3,1,5],[9,10,4],[6,9,7],[1,9,9],[9,6,1],[7,1,4],[1,8,7]],
[[4,3],[3,1],[6,2],[9,10],[9,9],[2,4],[6,9],[4,4],[4,5],[6,8]],
10))  # 7
print(so.circleGame(toys= [[3, 3, 1], [3, 2, 1]], circles = [[4, 3]], r = 2))  # 1
print(so.circleGame(toys= [[1, 3, 2], [4, 3, 1], [7, 1, 2]], circles = [[1, 0], [3, 3]], r = 4))  # 2




