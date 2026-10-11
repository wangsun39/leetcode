# 小扣在探索丛林的过程中，无意间发现了传说中“落寞的黄金之都”。而在这片建筑废墟的地带中，小扣使用探测仪监测到了存在某种带有「祝福」效果的力场。 经过不断的勘测记录，小扣将所有力场的分布都记录了下来。forceField[i] = [x,y,side] 表示第 i 片力场将覆盖以坐标 (x,y) 为中心，边长为 side 的正方形区域。
#
# 若任意一点的 力场强度 等于覆盖该点的力场数量，请求出在这片地带中 力场强度 最强处的 力场强度。
#
# 注意：
#
# 力场范围的边缘同样被力场覆盖。
# 示例 1：
#
# 输入： forceField = [[0,0,1],[1,0,1]]
#
# 输出：2
#
# 解释：如图所示，（0.5, 0) 处力场强度最强为 2， （0.5，-0.5）处力场强度同样是 2。image.png
#
# 示例 2：
#
# 输入： forceField = [[4,4,6],[7,5,3],[1,6,2],[5,6,3]]
#
# 输出：3
#
# 解释：如下图所示， forceField[0]、forceField[1]、forceField[3] 重叠的区域力场强度最大，返回 3image.png
#
# 提示：
#
# 1 <= forceField.length <= 100
# forceField[i].length == 3
# 0 <= forceField[i][0], forceField[i][1] <= 10^9
# 1 <= forceField[i][2] <= 10^9


from leetcode.allcode.competition.mypackage import *


class Solution:

    def fieldOfGreatestBlessing(self, forceField: List[List[int]]) -> int:
        ff = [(x - side / 2, x + side / 2, y - side / 2, y + side / 2) for x, y, side in forceField]

        p_x = set()
        for rec in ff:
            p_x.add(rec[0])
            p_x.add(rec[1])
        p_x = list(p_x)
        # p_x.sort()

        def f(l):
            d = SortedDict()
            for start, end in l:
                d[start] = d.setdefault(start, 0) + 1
                d[end + 0.001] = d.setdefault(end, 0) - 1

            ans = mx = 0
            for freq in d.values():
                mx += freq
                ans = max(ans, mx)
            return ans

        m = len(p_x)
        ans = 0
        for i in range(m):
            p_y = []
            for rec in ff:
                if p_x[i] < rec[0] or p_x[i] > rec[1]: continue
                p_y.append([rec[2], rec[3]])
            # p_y.sort()
            res = f(p_y)
            if res > ans:
                ans = res
        return ans



so = Solution()
print(so.fieldOfGreatestBlessing([[932,566,342],[546,489,250],[723,454,748],[830,887,334],[617,534,721],[924,267,892],[151,64,65],[318,825,196],[102,941,940],[748,562,582],[76,938,228],[921,15,245],[871,96,823],[701,737,991],[339,861,146],[484,409,823],[574,728,557],[104,845,459],[363,804,94],[445,685,83],[324,641,328],[626,2,897],[656,627,521],[935,506,956],[210,848,502],[990,889,112]]))
print(so.fieldOfGreatestBlessing([[0,0,1],[1,0,1]]))
print(so.fieldOfGreatestBlessing([[4,4,6],[7,5,3],[1,6,2],[5,6,3]]))




