# 我们得到了一副藏宝图，藏宝图显示，在一个迷宫中存在着未被世人发现的宝藏。
#
# 迷宫是一个二维矩阵，用一个字符串数组表示。它标识了唯一的入口（用 'S' 表示），和唯一的宝藏地点（用 'T' 表示）。但是，宝藏被一些隐蔽的机关保护了起来。在地图上有若干个机关点（用 'M' 表示），只有所有机关均被触发，才可以拿到宝藏。
#
# 要保持机关的触发，需要把一个重石放在上面。迷宫中有若干个石堆（用 'O' 表示），每个石堆都有无限个足够触发机关的重石。但是由于石头太重，我们一次只能搬一个石头到指定地点。
#
# 迷宫中同样有一些墙壁（用 '#' 表示），我们不能走入墙壁。剩余的都是可随意通行的点（用 '.' 表示）。石堆、机关、起点和终点（无论是否能拿到宝藏）也是可以通行的。
#
# 我们每步可以选择向上/向下/向左/向右移动一格，并且不能移出迷宫。搬起石头和放下石头不算步数。那么，从起点开始，我们最少需要多少步才能最后拿到宝藏呢？如果无法拿到宝藏，返回 -1 。
#
# 示例 1：
#
# 输入： ["S#O", "M..", "M.T"]
#
# 输出：16
#
# 解释：最优路线为： S->O, cost = 4, 去搬石头 O->第二行的M, cost = 3, M机关触发 第二行的M->O, cost = 3, 我们需要继续回去 O 搬石头。 O->第三行的M, cost = 4, 此时所有机关均触发 第三行的M->T, cost = 2，去T点拿宝藏。 总步数为16。图片.gif
#
# 示例 2：
#
# 输入： ["S#O", "M.#", "M.T"]
#
# 输出：-1
#
# 解释：我们无法搬到石头触发机关
#
# 示例 3：
#
# 输入： ["S#O", "M.T", "M.."]
#
# 输出：17
#
# 解释：注意终点也是可以通行的。
#
# 限制：
#
# 1 <= maze.length <= 100
# 1 <= maze[i].length <= 100
# maze[i].length == maze[j].length
# S 和 T 有且只有一个
# 0 <= M的数量 <= 16
# 0 <= O的数量 <= 40，题目保证当迷宫中存在 M 时，一定存在至少一个 O 。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimalSteps(self, maze: List[str]) -> int:
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        r, c = len(maze), len(maze[0])
        M = []
        O = []
        g = defaultdict(list)
        for i in range(r):
            for j in range(c):
                if maze[i][j] == '#': continue
                if maze[i][j] == 'S': start = i * c + j
                elif maze[i][j] == 'T': target = i * c + j
                elif maze[i][j] == 'M': M.append(i * c + j)
                elif maze[i][j] == 'O': O.append(i * c + j)
                for dx, dy in dir:
                    x, y = i + dx, j + dy
                    if 0 <= x < r and 0 <= y < c and maze[x][y] != '#':
                        g[i * c + j].append([x * c + y, 1])
        m = len(M)
        o = len(O)

        def dijkstra(g: List[List[Tuple[int]]], start: int, n: int) -> List[int]:
            # dist = [inf] * len(g)   # 注意这个地方可能要替换成 n
            dist = [inf] * n
            dist[start] = 0
            h = [(0, start)]
            while h:
                d, x = heappop(h)
                if d > dist[x]:
                    continue
                for y, wt in g[x]:
                    new_d = dist[x] + wt
                    if new_d < dist[y]:
                        dist[y] = new_d
                        heappush(h, (new_d, y))
            return dist

        ds = {}
        for v in M + O:
            ds[v] = dijkstra(g, v, r * c)
        ds[start] = dijkstra(g, start, r * c)

        @cache
        def calc(x, y):
            # 计算从 x 到 y，且必须经过一个O，的最短距离
            res = inf
            for z in O:
                res = min(res, ds[x][z] + ds[z][y])
            return res

        @cache
        def dfs(p, mask): # 当前在位置 p ，剩余机关用mask表示，完成的最少步数
            if mask == 0:
                return ds[p][target]
            res = inf
            for i in range(m):
                if mask & (1 << i) == 0: continue
                dmi = calc(p, M[i])
                if dmi == inf: return inf
                res = min(res, dmi + dfs(M[i], mask ^ (1 << i)))
            return res

        ans = dfs(start, (1 << m) - 1)
        return -1 if ans == inf else ans


so = Solution()
print(so.minimalSteps(["S#O", "M..", "M.T"]))




