# 给你一棵 n 个节点的树（一个无向、连通、无环图），每个节点表示一个城市，编号从 0 到 n - 1 ，且恰好有 n - 1 条路。0 是首都。给你一个二维整数数组 roads ，其中 roads[i] = [ai, bi] ，表示城市 ai 和 bi 之间有一条 双向路 。
#
# 每个城市里有一个代表，他们都要去首都参加一个会议。
#
# 每座城市里有一辆车。给你一个整数 seats 表示每辆车里面座位的数目。
#
# 城市里的代表可以选择乘坐所在城市的车，或者乘坐其他城市的车。相邻城市之间一辆车的油耗是一升汽油。
#
# 请你返回到达首都最少需要多少升汽油。
#
#
#
# 示例 1：
#
#
#
# 输入：roads = [[0,1],[0,2],[0,3]], seats = 5
# 输出：3
# 解释：
# - 代表 1 直接到达首都，消耗 1 升汽油。
# - 代表 2 直接到达首都，消耗 1 升汽油。
# - 代表 3 直接到达首都，消耗 1 升汽油。
# 最少消耗 3 升汽油。
# 示例 2：
#
#
#
# 输入：roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2
# 输出：7
# 解释：
# - 代表 2 到达城市 3 ，消耗 1 升汽油。
# - 代表 2 和代表 3 一起到达城市 1 ，消耗 1 升汽油。
# - 代表 2 和代表 3 一起到达首都，消耗 1 升汽油。
# - 代表 1 直接到达首都，消耗 1 升汽油。
# - 代表 5 直接到达首都，消耗 1 升汽油。
# - 代表 6 到达城市 4 ，消耗 1 升汽油。
# - 代表 4 和代表 6 一起到达首都，消耗 1 升汽油。
# 最少消耗 7 升汽油。
# 示例 3：
#
#
#
# 输入：roads = [], seats = 1
# 输出：0
# 解释：没有代表需要从别的城市到达首都。
#
#
# 提示：
#
# 1 <= n <= 105
# roads.length == n - 1
# roads[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# roads 表示一棵合法的树。
# 1 <= seats <= 105

from leetcode.allcode.competition.mypackage import *
import math
class Solution:
    def minimumFuelCost1(self, roads: List[List[int]], seats: int) -> int:
        map = defaultdict(list)
        for x, y in roads:
            map[x].append(y)
            map[y].append(x)
        map2 = defaultdict(list)  # x 节点的子节点列表，0 作为根节点
        def dfs(v):
            map2[v] = []
            for x in map[v]:
                if x not in map2:
                    map2[v].append(x)
            for s in map2[v]:
                dfs(s)
        dfs(0)
        print(map2)
        def calc(v):  # 人数，之前的油耗
            nu, cu = 1, 0
            for s in map2[v]:  # 依次计算每个子节点汇聚上来的人数和总共的油耗
                x, y = calc(s)
                cars = math.ceil(x / seats)
                cu += (y + cars)
                nu += x
            return nu, cu
        res = calc(0)
        return res[1]

    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # 2023/12/5 DFS 换个写法
        g = defaultdict(list)
        for x, y in roads:
            g[x].append(y)
            g[y].append(x)

        def dfs(x, fa):
            consume = n_cars = n_seats = 0
            for y in g[x]:
                if y == fa: continue
                a, b, c = dfs(y, x)
                consume += (a + b)
                n_cars += b
                n_seats += c
            if n_seats > 0:
                n_seats -= 1
                if n_seats // seats:
                    n_cars -= (n_seats // seats)
                    n_seats %= seats
            else:
                n_cars += 1
                n_seats = seats - 1
            # print(x, consume, n_cars, n_seats)
            return consume, n_cars, n_seats  # 子树消耗油量，使用汽车数，剩余空位数

        res = dfs(0, -1)
        return res[0]

so = Solution()
print(so.minimumFuelCost(roads = [], seats = 1))
print(so.minimumFuelCost(roads = [[0,1],[0,2],[0,3]], seats = 5))
print(so.minimumFuelCost(roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2))




