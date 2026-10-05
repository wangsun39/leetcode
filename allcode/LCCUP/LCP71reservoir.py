# 字符串数组 shape 描述了一个二维平面中的矩阵形式的集水器，shape[i][j] 表示集水器的第 i 行 j 列为：
#
# 'l'表示向左倾斜的隔板（即从左上到右下）；
# 'r'表示向右倾斜的隔板（即从左下到右上）；
# '.' 表示此位置没有隔板image.png
# 已知当隔板构成存储容器可以存水，每个方格代表的蓄水量为 2。集水器初始浸泡在水中，除内部密闭空间外，所有位置均被水填满。 现将其从水中竖直向上取出，请返回集水器最终的蓄水量。
#
# 注意：
#
# 隔板具有良好的透气性，因此空气可以穿过隔板，但水无法穿过
# 示例 1：
#
# 输入： shape = ["....rl","l.lr.r",".l..r.","..lr.."]
#
# 输出：18
#
# 解释：如下图所示，由于空气会穿过隔板，因此红框区域没有水image.png
#
# 示例 2：
#
# 输入： shape = [".rlrlrlrl","ll..rl..r",".llrrllrr","..lr..lr."] 输出：18
#
# 解释：如图所示。由于红框右侧未闭合，因此多余的水会从该处流走。image.png
#
# 示例 3：
#
# 输入： shape = ["rlrr","llrl","llr."] 输出：6
#
# 解释：如图所示。image.png
#
# 示例 4：
#
# 输入： shape = ["...rl...","..r..l..",".r.rl.l.","r.r..l.l","l.l..rl.",".l.lr.r.","..l..r..","...lr..."]
#
# 输出：30
#
# 解释：如下图所示。由于中间为内部密闭空间，无法蓄水。image.png
#
# 提示：
#
# 1 <= shape.length <= 50
# 1 <= shape[i].length <= 50
# shape[i][j] 仅为 'l'、'r' 或 '.'

from leetcode.allcode.competition.mypackage import *

class Solution:
    def reservoir(self, shape: List[str]) -> int:
        r, c = len(shape), len(shape[0])

        # 将每个格子分成4个小格子，分别指向4个方向
        up = [[0] * (c + 2) for _ in range(r + 1)]
        down = [[0] * (c + 2) for _ in range(r + 1)]
        left = [[0] * (c + 2) for _ in range(r + 1)]
        right = [[0] * (c + 2) for _ in range(r + 1)]

        m = 1  # 记录并查集中的点数, 0 表示容器外部
        for i in range(r):
            for j in range(1, c + 1):
                up[i][j] = m
                m += 1
                down[i][j] = m
                m += 1
                left[i][j] = m
                m += 1
                right[i][j] = m
                m += 1

        fa = list(range(m))

        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]

        def union(x, y):  # x 是代表元
            fa[find(y)] = find(x)

        cand = []  # 候选有水的位置
        for i in range(r - 1, -1, -1):  # 逆序处理每一行
            for j in range(c):  # 对应 位置 [i][j + 1]
                union(right[i][j], left[i][j + 1])
                union(right[i][j + 1], left[i][j + 2])
                if i > 0:
                    union(down[i - 1][j + 1], up[i][j + 1])
                    union(down[i][j + 1], up[i + 1][j + 1])

                if shape[i][j] in 'l.':
                    union(up[i][j + 1], right[i][j + 1])
                    union(down[i][j + 1], left[i][j + 1])
                if shape[i][j] in 'r.':
                    union(up[i][j + 1], left[i][j + 1])
                    union(down[i][j + 1], right[i][j + 1])

            # 一行处理完，再遍历一遍，决定是否保留进候选
            for j in range(c):  # 对应 位置 [i][j + 1]
                if find(up[i][j + 1]) != find(0):
                    cand.append(up[i][j + 1])
                if find(left[i][j + 1]) != find(0):
                    cand.append(left[i][j + 1])
                if find(down[i][j + 1]) != find(0):
                    cand.append(down[i][j + 1])
                if find(right[i][j + 1]) != find(0):
                    cand.append(right[i][j + 1])

        for j in range(c):
            union(up[0][j + 1], 0)  # 顶层与外部相连
        ans = 0
        for i in cand:  # 如果候选点与外部相连，才能有水，否则是个封闭区域
            if find(i) == find(0):
                # print(i)
                ans += 1
        return ans // 2





so = Solution()
print(so.reservoir(shape = ["rlrr","llrl","llr."]))
print(so.reservoir(shape = ["....rl","l.lr.r",".l..r.","..lr.."]))




