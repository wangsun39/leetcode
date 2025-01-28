# 汽车从起点出发驶向目的地，该目的地位于出发位置东面 target英里处。
#
# 沿途有加油站，每个station[i]代表一个加油站，它位于出发位置东面station[i][0]英里处，并且有station[i][1]升汽油。
#
# 假设汽车油箱的容量是无限的，其中最初有startFuel升燃料。它每行驶 1 英里就会用掉 1 升汽油。
#
# 当汽车到达加油站时，它可能停下来加油，将所有汽油从加油站转移到汽车中。
#
# 为了到达目的地，汽车所必要的最低加油次数是多少？如果无法到达目的地，则返回 -1 。
#
# 注意：如果汽车到达加油站时剩余燃料为 0，它仍然可以在那里加油。如果汽车到达目的地时剩余燃料为 0，仍然认为它已经到达目的地。
#
# 
#
# 示例 1：
#
# 输入：target = 1, startFuel = 1, stations = []
# 输出：0
# 解释：我们可以在不加油的情况下到达目的地。
# 示例 2：
#
# 输入：target = 100, startFuel = 1, stations = [[10,100]]
# 输出：-1
# 解释：我们无法抵达目的地，甚至无法到达第一个加油站。
# 示例 3：
#
# 输入：target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
# 输出：2
# 解释：
# 我们出发时有 10 升燃料。
# 我们开车来到距起点 10 英里处的加油站，消耗 10 升燃料。将汽油从 0 升加到 60 升。
# 然后，我们从 10 英里处的加油站开到 60 英里处的加油站（消耗 50 升燃料），
# 并将汽油从 10 升加到 50 升。然后我们开车抵达目的地。
# 我们沿途在1两个加油站停靠，所以返回 2 。
# 
#
# 提示：
#
# 1 <= target, startFuel, stations[i][1] <= 10^9
# 0 <= stations.length <= 500
# 0 < stations[0][0] < stations[1][0] < ... < stations[stations.length-1][0] < target

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minRefuelStops1(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dq = [startFuel]
        cur = 0
        st = [e[0] for e in stations]
        ans = 0
        start = 0
        while True:
            cur += dq.pop()
            if cur >= target:
                return ans
            ans += 1
            pos = bisect.bisect_right(st, cur, start)
            for i in range(start, pos):
                bisect.insort_left(dq, stations[i][1])
            start = pos
            if len(dq) == 0:
                return -1


    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # 2024/10/7  优先队列的写法
        farthest = startFuel
        ans = 0
        hp = []  # 经过的加油站的油量的大顶堆
        for pos, fu in stations:
            while farthest < pos:
                if len(hp) == 0: return -1
                f = -heappop(hp)
                farthest += f
                ans += 1
            if farthest >= target:
                return ans
            heappush(hp, -fu)
        # 已经经过所有加油站，还未到达target
        while farthest < target:
            if len(hp) == 0: return -1
            f = -heappop(hp)
            farthest += f
            ans += 1
        return ans


so = Solution()
print(so.minRefuelStops(100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]))
print(so.minRefuelStops(1000,299,[[13,21],[26,115],[100,47],[225,99],[299,141],[444,198],[608,190],[636,157],[647,255],[841,123]]))
print(so.minRefuelStops(100, 50, [[60,50]]))
print(so.minRefuelStops(999,1000,[[5,100],[997,100],[998,100]]))
print(so.minRefuelStops(target = 1, startFuel = 1, stations = []))
print(so.minRefuelStops(target = 100, startFuel = 1, stations = [[10,100]]))

