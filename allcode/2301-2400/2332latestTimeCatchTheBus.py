

from leetcode.allcode.competition.mypackage import *

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        n, m = len(buses), len(passengers)
        j = 0  # passengers 的下标
        def find(que, mn, mx):  # 在当前的队伍中找一个最大的空位
            if len(que) == 0: return mx
            if len(que) < capacity and cur_que[-1] != mx:
                return mx
            for i in range(len(que) - 1, 0, -1):
                if i - 1 < 0 or que[i] - que[i - 1] > 1:
                    return que[i] - 1
            return mn
        for i, x in enumerate(buses):
            cur_que = []  # 当前在车上的人
            if j < m and (j == 0 or passengers[j] - passengers[j - 1] > 1):
                ans = passengers[j] - 1
            while j < m and passengers[j] <= x and len(cur_que) < capacity:
                cur_que.append(passengers[j])
                j += 1
            ans = find(cur_que, ans, x)

        return ans

so = Solution()
print(so.latestTimeCatchTheBus(buses = [3,2], passengers = [2], capacity = 2))  # 3
print(so.latestTimeCatchTheBus(buses = [3], passengers = [3,4], capacity = 2))  # 2
print(so.latestTimeCatchTheBus(buses = [10,20], passengers = [2,17,18,19], capacity = 2))  # 16
print(so.latestTimeCatchTheBus(buses = [2,3], passengers = [2,3], capacity = 2))  # 1
print(so.latestTimeCatchTheBus(buses = [3], passengers = [4], capacity = 1))  # 3
print(so.latestTimeCatchTheBus(buses = [2], passengers = [2], capacity = 2))  # 1
print(so.latestTimeCatchTheBus(buses = [2], passengers = [2], capacity = 1))  # 1
print(so.latestTimeCatchTheBus(buses = [3], passengers = [2,3], capacity = 2))  # 1
print(so.latestTimeCatchTheBus(buses = [20,30,10], passengers = [19,13,26,4,25,11,21], capacity = 2))




