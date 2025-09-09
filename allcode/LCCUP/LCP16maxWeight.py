# 又到了一年一度的春游时间，小吴计划去游乐场游玩 1 天，游乐场总共有 N 个游乐项目，编号从 0 到 N-1。小吴给每个游乐项目定义了一个非负整数值 value[i] 表示自己的喜爱值。两个游乐项目之间会有双向路径相连，整个游乐场总共有 M 条双向路径，保存在二维数组 edges中。 小吴计划选择一个游乐项目 A 作为这一天游玩的重点项目。上午小吴准备游玩重点项目 A 以及与项目 A 相邻的两个项目 B、C （项目A、B与C要求是不同的项目，且项目B与项目C要求相邻），并返回 A ，即存在一条 A-B-C-A 的路径。 下午，小吴决定再游玩重点项目 A以及与A相邻的两个项目 B'、C'，（项目A、B'与C'要求是不同的项目，且项目B'与项目C'要求相邻），并返回 A ，即存在一条 A-B'-C'-A 的路径。下午游玩项目 B'、C' 可与上午游玩项目B、C存在重复项目。 小吴希望提前安排好游玩路径，使得喜爱值之和最大。请你返回满足游玩路径选取条件的最大喜爱值之和，如果没有这样的路径，返回 0。 注意：一天中重复游玩同一个项目并不能重复增加喜爱值了。例如：上下午游玩路径分别是 A-B-C-A与A-C-D-A 那么只能获得 value[A] + value[B] + value[C] + value[D] 的总和。
#
# 示例 1：
#
# 输入：edges = [[0,1],[1,2],[0,2]], value = [1,2,3]
#
# 输出：6
#
# 解释：喜爱值之和最高的方案之一是 0->1->2->0 与 0->2->1->0 。重复游玩同一点不重复计入喜爱值，返回1+2+3=6
#
# 示例 2：
#
# 输入：edges = [[0,2],[2,1]], value = [1,2,5]
#
# 输出：0
#
# 解释：无满足要求的游玩路径，返回 0
#
# 示例 3：
#
# 输入：edges = [[0,1],[0,2],[0,3],[0,4],[0,5],[1,3],[2,4],[2,5],[3,4],[3,5],[4,5]], value = [7,8,6,8,9,7]
#
# 输出：39
#
# 解释：喜爱值之和最高的方案之一是 3->0->1->3 与 3->4->5->3 。喜爱值最高为 7+8+8+9+7=39
#
# 限制：
#
# 3 <= value.length <= 10000
# 1 <= edges.length <= 10000
# 0 <= edges[i][0],edges[i][1] < value.length
# 0 <= value[i] <= 10000
# edges中没有重复的边
# edges[i][0] != edges[i][1]

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxWeight(self, edges: List[List[int]], value: List[int]) -> int:
        g = defaultdict(list)
        gs = defaultdict(set)
        # ge = defaultdict(list)  # 边找对点
        m = len(edges)
        m2 = m ** 0.5
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            gs[x].add(y)
            gs[y].add(x)
        n = len(g)
        deg = [len(g[i]) for i in range(n)]
        triangle = defaultdict(list)
        ans = 0

        def calc(x, max_l):
            # 在之多三个三角形中选至多2个，求最大的value和
            res = 0
            if len(max_l) == 1: return value[x] + value[max_l[0][0]] + value[max_l[0][1]]
            for i in range(len(max_l)):
                for j in range(i + 1, len(max_l)):
                    res = max(res, sum(value[y] for y in set(max_l[i][:2] + max_l[j][:2])))
            return res + value[x]

        for i in range(n):
            # 枚举 A 点，找到所有 B,C 点对
            # 找所有 B，C对的前3大的对
            max_l = []
            if deg[i] <= m2:
                ni = len(g[i])
                for jj in range(ni):
                    j = g[i][jj]
                    for kk in range(j + 1, ni):
                        k = g[i][kk]
                        if j in gs[k]:
                            triangle[i].append([j, k])
                            if len(max_l) == 0 or max_l[-1][-1] <= value[j] + value[k]:
                                max_l.append([j, k, value[j] + value[k]])
                                max_l.sort(key=lambda x:x[2], reverse=True)
                                if len(max_l) > 4: max_l.pop()
            else:
                for j, k in edges:
                    if j == i or k == i: continue
                    if j in gs[i] and k in gs[i]:
                        triangle[i].append([j, k])
                        if len(max_l) == 0 or max_l[-1][-1] <= value[j] + value[k]:
                            max_l.append([j, k, value[j] + value[k]])
                            max_l.sort(key=lambda x: x[2], reverse=True)
                            if len(max_l) > 4: max_l.pop()
            if len(max_l):
                ans = max(ans, calc(i, max_l))

        return ans


so = Solution()
print(so.maxWeight(edges = [[3,8],[4,7],[0,8],[5,7],[6,7],[7,8],[1,3],[4,8],[0,5],[3,5],[5,6],[8,9],[3,9],[0,2],[5,8],[1,2],[4,9],[6,9],[7,9],[1,6],[1,7],[0,7],[1,5],[2,5],[2,6],[0,4],[1,9],[0,9],[2,4],[2,8]], value = [7080,5450,4841,8487,8689,8563,281,3794,3916,4946]))  # 36735
print(so.maxWeight(edges = [[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],[2,3],[2,4],[2,5],[2,6],[2,7],[2,8],[2,9],[3,4],[3,5],[3,6],[3,7],[3,8],[3,9],[4,5],[4,6],[4,7],[4,8],[4,9],[5,6],[5,7],[5,8],[5,9],[6,7],[6,8],[6,9],[7,8],[7,9],[8,9]], value = [6808,5250,74,3659,8931,1273,7545,879,7924,7710]))  # 38918
print(so.maxWeight(edges = [[0,1],[0,2],[0,3],[0,4],[0,5],[1,3],[2,4],[2,5],[3,4],[3,5],[4,5]], value = [7,8,6,8,9,7]))  # 39
print(so.maxWeight(edges = [[0,1],[1,2],[0,2]], value = [1,2,3]))  # 6



