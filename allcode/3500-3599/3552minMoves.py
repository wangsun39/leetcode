# 给你一个大小为 m x n 的二维字符网格 matrix，用字符串数组表示，其中 matrix[i][j] 表示第 i 行和第 j 列处的单元格。每个单元格可以是以下几种字符之一：
#
# '.' 表示一个空单元格。
# '#' 表示一个障碍物。
# 一个大写字母（'A' 到 'Z'）表示一个传送门。
# 你从左上角单元格 (0, 0) 出发，目标是到达右下角单元格 (m - 1, n - 1)。你可以从当前位置移动到相邻的单元格（上、下、左、右），移动后的单元格必须在网格边界内且不是障碍物。
#
# 如果你踏入一个包含传送门字母的单元格，并且你之前没有使用过该传送门字母，你可以立即传送到网格中另一个具有相同字母的单元格。这次传送不计入移动次数，但每个字母对应的传送门在旅程中 最多 只能使用一次。
#
# 返回到达右下角单元格所需的 最少 移动次数。如果无法到达目的地，则返回 -1。
#
#
#
# 示例 1：
#
# 输入： matrix = ["A..",".A.","..."]
#
# 输出： 2
#
# 解释：
#
#
#
# 在第一次移动之前，从 (0, 0) 传送到 (1, 1)。
# 第一次移动，从 (1, 1) 移动到 (1, 2)。
# 第二次移动，从 (1, 2) 移动到 (2, 2)。
# 示例 2：
#
# 输入： matrix = [".#...",".#.#.",".#.#.","...#."]
#
# 输出： 13
#
# 解释：
#
#
#
#
#
# 提示：
#
# 1 <= m == matrix.length <= 103
# 1 <= n == matrix[i].length <= 103
# matrix[i][j] 是 '#'、'.' 或一个大写英文字母。
# matrix[0][0] 不是障碍物。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        dic = defaultdict(set)
        r, c = len(matrix), len(matrix[0])

        for i in range(r):
            for j in range(c):
                if matrix[i][j] in ('#', '.'): continue
                dic[matrix[i][j]].add(i * c + j)
        fa = list(range(r * c))  # 所有相同字母的代表元
        gate = defaultdict(list)  # 代表元找到组内所有成员
        for i, group in dic.items():
            if 0 in group and r * c - 1 in group: return 0
            if 0 in group:
                for x in group:
                    fa[x] = 0
                    gate[0].append(x)
            elif r * c - 1 in group:
                for x in group:
                    fa[x] = r * c - 1
                    gate[r * c - 1].append(x)
            else:
                v = next(iter(group))
                for x in group:
                    fa[x] = v
                    gate[v].append(x)

        if 0 in gate:
            dq1 = deque(gate[0])
        else:
            dq1 = deque([0])
        vis = set(dq1)
        ans = 0
        while dq1:
            dq2 = deque()
            while dq1:
                e1 = dq1.popleft()
                if e1 == r * c - 1: return ans
                i, j = e1 // c, e1 % c
                for x, y in dir:
                    u, v = i + x, j + y
                    if 0 <= u < r and 0 <= v < c and matrix[u][v] != '#':
                        e2 = u * c + v
                        if e2 not in vis:
                            dq2.append(e2)
                            vis.add(e2)
                            for e3 in gate[fa[e2]]:
                                dq2.append(e3)
                                vis.add(e3)
            ans += 1
            dq1 = dq2

        return -1



so = Solution()
print(so.minMoves(matrix = [".A.","BA.","B.A"]))   # 1
print(so.minMoves(matrix = [".","A"]))
print(so.minMoves(matrix = ["A..",".A.","..."]))




