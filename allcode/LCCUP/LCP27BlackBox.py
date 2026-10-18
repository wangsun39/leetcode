# 秋日市集上有个奇怪的黑盒，黑盒的主视图为 n*m 的矩形。从黑盒的主视图来看，黑盒的上面和下面各均匀分布有 m 个小孔，黑盒的左面和右面各均匀分布有 n 个小孔。黑盒左上角小孔序号为 0，按顺时针编号，总共有 2*(m+n) 个小孔。每个小孔均可以打开或者关闭，初始时，所有小孔均处于关闭状态。每个小孔上的盖子均为镜面材质。例如一个 2*3 的黑盒主视图与其小孔分布如图所示:
#
# image.png
#
# 店长告诉小扣，这里是「几何学的快问快答」，店长可能有两种操作：
#
# open(int index, int direction) - 若小孔处于关闭状态，则打开小孔，照入光线；否则直接照入光线；
# close(int index) - 关闭处于打开状态小孔，店长保证不会关闭已处于关闭状态的小孔；
# 其中：
#
# index： 表示小孔序号
# direction：1 表示光线沿 y=x 方向，-1 表示光线沿 y=−x 方向。
# image.png
#
# 当光线照至边界时：若边界上的小孔为开启状态，则光线会射出；否则，光线会在小孔之间进行反射。特别地：
#
# 若光线射向未打开的拐角（黑盒顶点），则光线会原路反射回去；
# 光线自拐角处的小孔照入时，只有一种入射方向（如自序号为 0 的小孔照入方向只能为 -1）
# image.png
#
# 请帮助小扣判断并返回店长每次照入的光线从几号小孔射出。
#
# 示例 1：
#
# 输入： ["BlackBox","open","open","open","close","open"] [[2,3],[6,-1],[4,-1],[0,-1],[6],[0,-1]]
#
# 输出：[null,6,4,6,null,4]
#
# 解释： BlackBox b = BlackBox(2,3); // 新建一个 2x3 的黑盒 b.open(6,-1) // 打开 6 号小孔，并沿 y=-x 方向照入光线，光线至 0 号小孔反射，从 6 号小孔射出 b.open(4,-1) // 打开 4 号小孔，并沿 y=-x 方向照入光线，光线轨迹为 4-2-8-2-4，从 4 号小孔射出 b.open(0,-1) // 打开 0 号小孔，并沿 y=-x 方向照入光线，由于 6 号小孔为开启状态，光线从 6 号小孔射出 b.close(6) // 关闭 6 号小孔 b.shoot(0,-1) // 从 0 号小孔沿 y=-x 方向照入光线，由于 6 号小孔为关闭状态，4 号小孔为开启状态，光线轨迹为 0-6-4，从 4 号小孔射出
#
# 示例 2：
#
# 输入： ["BlackBox","open","open","open","open","close","open","close","open"] [[3,3],[1,-1],[5,1],[11,-1],[11,1],[1],[11,1],[5],[11,-1]]
#
# 输出：[null,1,1,5,1,null,5,null,11]
#
# 解释：
#
# image.png
#
# BlackBox b = BlackBox(3,3); // 新建一个 3x3 的黑盒 b.open(1,-1) // 打开 1 号小孔，并沿 y=-x 方向照入光线，光线轨迹为 1-5-7-11-1，从 1 号小孔射出 b.open(5,1) // 打开 5 号小孔，并沿 y=x 方向照入光线，光线轨迹为 5-7-11-1，从 1 号小孔射出 b.open(11,-1) // 打开 11 号小孔，并沿逆 y=-x 方向照入光线，光线轨迹为 11-7-5，从 5 号小孔射出 b.open(11,1) // 从 11 号小孔沿 y=x 方向照入光线，光线轨迹为 11-1，从 1 号小孔射出 b.close(1) // 关闭 1 号小孔 b.open(11,1) // 从 11 号小孔沿 y=x 方向照入光线，光线轨迹为 11-1-5，从 5 号小孔射出 b.close(5) // 关闭 5 号小孔 b.open(11,-1) // 从 11 号小孔沿 y=-x 方向照入光线，光线轨迹为 11-1-5-7-11，从 11 号小孔射出
#
# 提示：
#
# 1 <= n, m <= 10000
# 1 <= 操作次数 <= 10000
# direction 仅为 1 或 -1
# 0 <= index < 2*(m+n)

from leetcode.allcode.competition.mypackage import *

class BlackBox:

    def _next2(self, idx, dir):
        # 光线从idx，以方向dir射出，返回下一个到达的点，及射出的方向
        # dir = 0 对于 题中的 -1，dir = 1 对于 题中的 1
        # 仅考虑光线顺时针旋转
        c0, c1, c2, c3, c4 = 0, self.m, self.m + self.n, self.m * 2 + self.n, self.m * 2 + self.n * 2
        if dir == -1:
            if idx < self.m:  # 上侧出
                d1, d2 = idx - c0, c1 - idx
                if d2 < self.n:  # 到达右侧
                    return (c1 + d2, -dir)
                else:  # 到达下侧
                    return (c2 + (d2 - self.n), -dir)
            elif idx < self.n + self.m:  # 右侧出
                d1, d2 = idx - c1, c2 - idx
                if d1 < self.m:   # 到达上侧
                    return (c1 - d1, -dir)
                else:   # 到达左侧
                    return (c3 + d2 + self.m, -dir)
            elif idx < self.m * 2 + self.n:  # 下侧出
                d1, d2 = idx - c2, c3 - idx
                if d2 > self.n:  # 上侧出
                    return (c1 - d1 - self.n, -dir)
                else:  # 左侧出
                    return ((c3 + d2) % c4, -dir)
            else:  # 左侧出
                d1, d2 = idx - c3, c4 - idx
                if d1 < self.m:  # 下侧出
                    return (c3 - d1, -dir)
                else:  # 右侧出
                    return (c2 - (d1 - self.m), -dir)
        else:
            if idx < self.m:  # 上侧出
                d1, d2 = idx - c0, c1 - idx
                if d1 < self.n:  # 到达左侧
                    return (c4 - d1, -dir)
                else:  # 到达下侧
                    return (c2 + (d2 + self.n), -dir)
            elif idx < self.n + self.m:  # 右侧出
                d1, d2 = idx - c1, c2 - idx
                if d2 < self.m:   # 到达下侧
                    return (c2 + d2, -dir)
                else:   # 到达左侧
                    return (c3 + d2 - self.m, -dir)
            elif idx < self.m * 2 + self.n:  # 下侧出
                d1, d2 = idx - c2, c3 - idx
                if d1 > self.n:  # 上侧出
                    return (c1 - (d1 - self.n), -dir)
                else:  # 右侧出
                    return (c2 - d1, -dir)
            else:  # 左侧出
                d1, d2 = idx - c3, c4 - idx
                if d2 < self.m:  # 上侧出
                    return ((c0 + d2) % c4, -dir)
                else:  # 右侧出
                    return (c2 - (d1 + self.m), -dir)

    def _next(self, idx, dir):
        # 对四个顶点再特殊处理一下
        nx = self._next2(idx, dir)
        if nx[0] in (0, self.m + self.n):
            return (nx[0], -1)
        elif nx[0] in (self.m, self.m * 2 + self.n):
            return (nx[0], 1)
        return nx



    def __init__(self, n: int, m: int):
        # 要为每个点两种入射光线的状态编号，[index, dir] , 顶点只有一个方向
        # 预处理所有状态的循环，对每个状态的循环进行分组
        self.n, self.m = n, m
        # self.ns = (m + n) * 4
        self.g_num = 0
        # self.group = []  # 按循环分组，组内记录 [组内编号, index]
        # self.idx_to_grp = [[[-1] * 2 for _ in range(2)] for _ in range((n + m) * 2)]  # index 到 组的映射 分别对应组的编号和组内序号
        self.idx_to_grp = defaultdict(list)
        # 下面这些点都是顶点，方向是不会出现的
        # self.idx_to_grp[0][1][0] = self.idx_to_grp[m][0][0] = self.idx_to_grp[m + n][1][0] = self.idx_to_grp[m * 2 + n][0][0] = inf
        # self.idx_to_grp[index][dir] = [组号, 组内编号]

        def search(idx, dir):
            if (idx, dir) in self.idx_to_grp:
                return
            # gid = len(self.group)
            # self.group.append([idx])
            self.idx_to_grp[(idx, dir)] = [self.g_num, 0]
            nx = self._next(idx, dir)
            cnt = 1
            # print(self.idx_to_grp[nx[0]][nx[1]][0])
            while nx not in self.idx_to_grp:
                # print(1,nx)
                self.idx_to_grp[nx] = [self.g_num, cnt]
                # self.group[self.g_num].append(nx[1])
                nx = self._next(nx[0], nx[1])
                # print(2, nx)
                cnt += 1
            self.g_num += 1

        for i in range(2 * (n + m)):
            if i == 0 or i == n + m:
                search(i, -1)
            elif i == m or i == m * 2 + n:
                search(i, 1)
            else:
                search(i, -1)
                search(i, 1)

        self.group = [SortedList() for _ in range(self.g_num)]  # 按循环分组，组内记录 [组内编号, index]

        # print(self.group)
        # print(self.idx_to_grp)


    def open(self, index: int, direction: int) -> int:
        if index not in (0, self.m, self.m + self.n, self.m * 2 + self.n):
            gid, ggid = self.idx_to_grp[(index, -direction)]
            if [ggid, index] not in self.group[gid]:
                self.group[gid].add([ggid, index])
        gid, ggid = self.idx_to_grp[(index, direction)]
        if [ggid, index] not in self.group[gid]:
            self.group[gid].add([ggid, index])
        p = self.group[gid].bisect_right([ggid, index])
        if p < len(self.group[gid]):
            return self.group[gid][p][1]
        return self.group[gid][0][1]



    def close(self, index: int) -> None:
        if index not in (0, self.m + self.n):
            gid, ggid = self.idx_to_grp[(index, 1)]
            if [ggid, index] in self.group[gid]:
                self.group[gid].remove([ggid, index])
        if index not in (self.m, self.m * 2 + self.n):
            gid, ggid = self.idx_to_grp[(index, -1)]
            if [ggid, index] in self.group[gid]:
                self.group[gid].remove([ggid, index])


so = BlackBox(1, 6)
so.open(3, -1)
# print(so.open(3, 1))
print(so.open(6, 1))
so = BlackBox(2, 3)


