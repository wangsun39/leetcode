# 欢迎各位勇者来到力扣城，本次试炼主题为「打地鼠」。middle_img_v2_d5d09656-0616-4a80-845e-ece461c5ba9g.png{:height="200px"} 勇者面前有一个大小为 3*3 的打地鼠游戏机，地鼠将随机出现在各个位置，moles[i] = [t,x,y] 表示在第 t 秒会有地鼠出现在 (x,y) 位置上，并于第 t+1 秒该地鼠消失。
#
# 勇者有一把可敲打地鼠的锤子，初始时刻（即第 0 秒）锤子位于正中间的格子 (1,1)，锤子的使用规则如下：
#
# 锤子每经过 1 秒可以往上、下、左、右中的一个方向移动一格，也可以不移动
# 锤子只可敲击所在格子的地鼠，敲击不耗时
# 请返回勇者最多能够敲击多少只地鼠。
#
# 注意：
#
# 输入用例保证在相同时间相同位置最多仅有一只地鼠
# 示例 1：
#
# 输入： moles = [[1,1,0],[2,0,1],[4,2,2]]
#
# 输出： 2
#
# 解释： 第 0 秒，锤子位于 (1,1) 第 1 秒，锤子移动至 (1,0) 并敲击地鼠 第 2 秒，锤子移动至 (2,0) 第 3 秒，锤子移动至 (2,1) 第 4 秒，锤子移动至 (2,2) 并敲击地鼠 因此勇者最多可敲击 2 只地鼠
#
# 示例 2：
#
# 输入：moles = [[2,0,2],[5,2,0],[4,1,0],[1,2,1],[3,0,2]]
#
# 输出：3
#
# 解释： 第 0 秒，锤子位于 (1,1) 第 1 秒，锤子移动至 (2,1) 并敲击地鼠 第 2 秒，锤子移动至 (1,1) 第 3 秒，锤子移动至 (1,0) 第 4 秒，锤子在 (1,0) 不移动并敲击地鼠 第 5 秒，锤子移动至 (2,0) 并敲击地鼠 因此勇者最多可敲击 3 只地鼠
#
# 示例 3：
#
# 输入：moles = [[0,1,0],[0,0,1]]
#
# 输出：0
#
# 解释： 第 0 秒，锤子初始位于 (1,1)，此时并不能敲击 (1,0)、(0,1) 位置处的地鼠
#
# 提示：
#
# 1 <= moles.length <= 10^5
# moles[i].length == 3
# 0 <= moles[i][0] <= 10^9
# 0 <= moles[i][1], moles[i][2] < 3

from leetcode.allcode.competition.mypackage import *

# 预处理
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
arrived = defaultdict(lambda: defaultdict(lambda: []))   # arrived[(i, j)][k]  表示从位置(i, j)走k步，所能到达的所有点
for i in range(3):
    for j in range(3):
        # BFS
        vis = {(i, j)}
        dq1 = deque([(i, j)])
        dis = 0
        while dq1:
            dq2 = deque()
            while dq1:
                x, y = dq1.popleft()
                for k in range(dis, 5):
                    arrived[(i, j)][k].append((x, y))
                for dx, dy in dir:
                    u, v = x + dx, y + dy
                    if 0 <= u < 3 and 0 <= v < 3 and (u, v) not in vis:
                        dq2.append((u, v))
                        vis.add((u, v))
            dq1 = dq2
            dis += 1


class Solution:
    def getMaximumNumber(self, moles: List[List[int]]) -> int:
        moles.sort()
        moles2 = []
        days = []
        for i in range(len(moles)):
            t, x, y = moles[i]
            if moles2 and moles[i - 1][0] == t:
                moles2[-1][x][y] = 1
            else:
                days.append(t)
                moles2.append([[0] * 3 for _ in range(3)])
                moles2[-1][x][y] = 1
        dp1 = [[-inf] * 3 for _ in range(3)]
        dp1[1][1] = 0
        if days[0] == 0:  # 处理开始就打到的情况
            if moles2[0][1][1]:
                dp1[1][1] = 1
            days.pop(0)
            moles2.pop(0)
        n = len(moles2)
        for i in range(n):
            dp2 = [[0] * 3 for _ in range(3)]
            if i == 0:
                t = days[i]
            else:
                t = days[i] - days[i - 1]
            t = min(t, 4)
            for x in range(3):
                for y in range(3):
                    for j, k in arrived[(x, y)][t]:
                        dp2[x][y] = max(dp2[x][y], moles2[i][x][y] + dp1[j][k])
            dp1 = dp2
        return max(max(row) for row in dp1)


so = Solution()
print(so.getMaximumNumber([[1,0,0]]))  # 0
print(so.getMaximumNumber([[0,0,0],[1,1,0],[0,2,0],[1,0,1],[1,2,1]]))  # 1
print(so.getMaximumNumber([[1,1,0],[2,0,1],[4,2,2]]))  # 2
print(so.getMaximumNumber([[2,0,2],[5,2,0],[4,1,0],[1,2,1],[3,0,2]]))  # 3

