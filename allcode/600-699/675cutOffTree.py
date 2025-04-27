# 你被请来给一个要举办高尔夫比赛的树林砍树。树林由一个m x n 的矩阵表示， 在这个矩阵中：
#
# 0 表示障碍，无法触碰
# 1表示地面，可以行走
# 比 1 大的数表示有树的单元格，可以行走，数值表示树的高度
# 每一步，你都可以向上、下、左、右四个方向之一移动一个单位，如果你站的地方有一棵树，那么你可以决定是否要砍倒它。
#
# 你需要按照树的高度从低向高砍掉所有的树，每砍过一颗树，该单元格的值变为 1（即变为地面）。
#
# 你将从 (0, 0) 点开始工作，返回你砍完所有树需要走的最小步数。 如果你无法砍完所有的树，返回 -1 。
#
# 可以保证的是，没有两棵树的高度是相同的，并且你至少需要砍倒一棵树。
#
#
#
# 示例 1：
#
#
# 输入：forest = [[1,2,3],[0,0,4],[7,6,5]]
# 输出：6
# 解释：沿着上面的路径，你可以用 6 步，按从最矮到最高的顺序砍掉这些树。
# 示例 2：
#
#
# 输入：forest = [[1,2,3],[0,0,0],[7,6,5]]
# 输出：-1
# 解释：由于中间一行被障碍阻塞，无法访问最下面一行中的树。
# 示例 3：
#
# 输入：forest = [[2,3,4],[0,0,5],[8,7,6]]
# 输出：6
# 解释：可以按与示例 1 相同的路径来砍掉所有的树。
# (0,0) 位置的树，可以直接砍去，不用算步数。
#
#
# 提示：
#
# m == forest.length
# n == forest[i].length
# 1 <= m, n <= 50
# 0 <= forest[i][j] <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def cutOffTree1(self, forest: List[List[int]]) -> int:
        # Floyd 这个写法性能不够
        def floyd1(n: int, edges: List[List[int]]) -> List[List[int]]:  # 无向图
            w = [[inf] * n for _ in range(n)]
            for x, y, wt in edges:
                w[x][y] = w[y][x] = wt

            @cache
            def dfs(k: int, i: int, j: int) -> int:
                if k < 0:  # 递归边界
                    return w[i][j]
                return min(dfs(k - 1, i, j), dfs(k - 1, i, k) + dfs(k - 1, k, j))

            f = [[inf] * n for _ in range(n)]  # f[i][j] 表示 i 到 j 的最小距离
            for i in range(n):
                f[i][i] = 0
                for j in range(i + 1, n):
                    f[i][j] = f[j][i] = dfs(n - 1, i, j)

            return f

        r, c = len(forest), len(forest[0])
        n = r * c
        edges = []
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        dic = {}  # 高度对应到点
        for i in range(r):
            for j in range(c):
                if forest[i][j] == 0: continue
                dic[forest[i][j]] = i * c + j
                for u, v in dir:
                    x, y = i + u, j + v
                    if 0 <= x < r and 0 <= y < c and forest[x][y]:
                        edges.append([i * c + j, x * c + y, 1])

        f = floyd1(n, edges)
        ans = 0
        pos = [dic[h] for h in sorted(list(dic.keys()))]
        if pos[0] != 0: pos.insert(0, 0)
        for i in range(1, len(pos)):
            if (v := f[pos[i - 1]][pos[i]]) == inf: return -1
            ans += v

        return ans


    def cutOffTree(self, forest: List[List[int]]) -> int:
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

        # 建图
        r, c = len(forest), len(forest[0])
        n = r * c
        g = defaultdict(list)
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        dic = {}  # 高度对应到点
        for i in range(r):
            for j in range(c):
                if forest[i][j] == 0: continue
                dic[forest[i][j]] = i * c + j
                for u, v in dir:
                    x, y = i + u, j + v
                    if 0 <= x < r and 0 <= y < c and forest[x][y]:
                        g[i * c + j].append([x * c + y, 1])

        ans = 0
        pos = [dic[h] for h in sorted(list(dic.keys())) if h != 1]
        if pos[0] != 0: pos.insert(0, 0)
        for i in range(1, len(pos)):
            d = dijkstra(g, pos[i-1], n)
            if d[pos[i]] == inf: return -1
            ans += d[pos[i]]
        return ans

obj = Solution()
print(obj.cutOffTree(forest = [[4,2,3],[0,0,1],[7,6,5]]))
print(obj.cutOffTree(forest = [[1,2,3],[0,0,4],[7,6,5]]))



