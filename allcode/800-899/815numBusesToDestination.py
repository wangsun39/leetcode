# 给你一个数组 routes ，表示一系列公交线路，其中每个 routes[i] 表示一条公交线路，第 i 辆公交车将会在上面循环行驶。
#
# 例如，路线 routes[0] = [1, 5, 7] 表示第 0 辆公交车会一直按序列 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... 这样的车站路线行驶。
# 现在从 source 车站出发（初始时不在公交车上），要前往 target 车站。 期间仅可乘坐公交车。
#
# 求出 最少乘坐的公交车数量 。如果不可能到达终点车站，返回 -1 。
#
#
#
# 示例 1：
#
# 输入：routes = [[1,2,7],[3,6,7]], source = 1, target = 6
# 输出：2
# 解释：最优策略是先乘坐第一辆公交车到达车站 7 , 然后换乘第二辆公交车到车站 6 。
# 示例 2：
#
# 输入：routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
# 输出：-1
#
#
# 提示：
#
# 1 <= routes.length <= 500.
# 1 <= routes[i].length <= 105
# routes[i] 中的所有值 互不相同
# sum(routes[i].length) <= 105
# 0 <= routes[i][j] < 106
# 0 <= source, target < 106

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        stations = defaultdict(list)
        for i, route in enumerate(routes):
            for x in route:
                stations[x].append(i)

        vis = set()
        vis_r = set()
        dq1 = deque()
        for r in stations[source]:
            vis_r.add(r)
            for x in routes[r]:
                if x in vis: continue
                dq1.append(x)
                vis.add(x)
        ans = 1
        while dq1:
            dq2 = deque()
            while dq1:
                x = dq1.popleft()
                if x == target: return ans
                for route in stations[x]:
                    if route in vis_r: continue
                    vis_r.add(route)
                    for y in routes[route]:
                        if y in vis: continue
                        vis.add(y)
                        dq2.append(y)
            dq1 = dq2
            ans += 1
        return -1



so = Solution()
print(so.numBusesToDestination(routes = [[1,2,7],[3,6,7]], source = 1, target = 6))
print(so.numBusesToDestination(routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12))




