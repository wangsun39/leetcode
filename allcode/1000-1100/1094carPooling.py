# 车上最初有 capacity 个空座位。车 只能 向一个方向行驶（也就是说，不允许掉头或改变方向）
#
# 给定整数 capacity 和一个数组 trips ,  trip[i] = [numPassengersi, fromi, toi] 表示第 i 次旅行有 numPassengersi 乘客，接他们和放他们的位置分别是 fromi 和 toi 。这些位置是从汽车的初始位置向东的公里数。
#
# 当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false。
#
#
#
# 示例 1：
#
# 输入：trips = [[2,1,5],[3,3,7]], capacity = 4
# 输出：false
# 示例 2：
#
# 输入：trips = [[2,1,5],[3,3,7]], capacity = 5
# 输出：true
#
#
# 提示：
#
# 1 <= trips.length <= 1000
# trips[i].length == 3
# 1 <= numPassengersi <= 100
# 0 <= fromi < toi <= 1000
# 1 <= capacity <= 105

from math import inf
from typing import List
from bisect import *

class Solution:
    def carPooling1(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        cc = 0  # 当前乘客数
        ci = 0  # 当前的位置
        diff = [0] * (max(x[2] for x in trips) + 1)
        for cnt, start, end in trips:
            while ci <= start:
                cc += diff[ci]
                ci += 1
            if cc + cnt > capacity:
                return False
            diff[end] -= cnt
            cc += cnt
        return True

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # 2023/12/2 换个写法
        x1, x2 = [[y, x] for x, y, _ in trips], [[y, -x] for x, _, y in trips]
        x = x1 + x2
        x.sort()
        s = 0  # 当前乘客数
        for a, b in x:
            s += b
            if s > capacity:
                return False
        return True




obj = Solution()
print(obj.carPooling(trips = [[2,1,5],[3,5,7]], capacity = 3))
print(obj.carPooling(trips = [[2,1,5],[3,3,7]], capacity = 4))
print(obj.carPooling(trips = [[2,1,5],[3,3,7]], capacity = 5))

