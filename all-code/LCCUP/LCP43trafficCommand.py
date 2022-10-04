# 前往「力扣挑战赛」场馆的道路上，有一个拥堵的十字路口，该十字路口由两条双向两车道的路交叉构成。由于信号灯故障，交警需要手动指挥拥堵车辆。假定路口没有新的来车且一辆车从一个车道驶入另一个车道所需的时间恰好为一秒钟，长度为 4 的一维字符串数组 directions 中按照 东、南、西、北 顺序记录了四个方向从最靠近路口到最远离路口的车辆计划开往的方向。其中：
#
# "E" 表示向东行驶；
# "S" 表示向南行驶；
# "W" 表示向西行驶；
# "N" 表示向北行驶。
# 交警每秒钟只能指挥各个车道距离路口最近的一辆车，且每次指挥需要满足如下规则：
#
# 同一秒钟内，一个方向的车道只允许驶出一辆车；
# 同一秒钟内，一个方向的车道只允许驶入一辆车；
# 同一秒钟内，车辆的行驶路线不可相交。
# 请返回最少需要几秒钟，该十字路口等候的车辆才能全部走完。
#
# 各个车道驶出的车辆可能的行驶路线如图所示：
#
#
#
# 注意：
#
# 测试数据保证不会出现掉头行驶指令，即某一方向的行驶车辆计划开往的方向不会是当前车辆所在的车道的方向;
# 表示堵塞车辆行驶方向的字符串仅用大写字母 "E"，"N"，"W"，"S" 表示。
# 示例 1：
#
# 输入：directions = ["W","N","ES","W"]
#
# 输出：2
#
# 解释：
# 第 1 秒：东西方向排在最前的车先行，剩余车辆状态 ["","N","S","W"]；
# 第 2 秒：南、西、北方向的车行驶，路口无等待车辆；
# 因此最少需要 2 秒，返回 2。
#
# 示例 2：
#
# 输入：directions = ["NS","WE","SE","EW"]
#
# 输出：3
#
# 解释：
# 第 1 秒：四个方向排在最前的车均可驶出；
# 第 2 秒：东南方向的车驶出，剩余车辆状态 ["","","E","W"]；
# 第 3 秒：西北方向的车驶出。
#
# 提示：
#
# directions.length = 4
# 0 <= directions[i].length <= 20
#
# https://leetcode.cn/problems/Y1VbOX





from typing import List
from collections import deque
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)
#import random
# random.uniform(a, b)，用于生成一个指定范围内的随机浮点数，闭区间
# randint和randrange的区别：
# randint 产生的随机数区间是包含左右极限的，也就是说左右都是闭区间的[1, n]，能取到1和n。
# 而 randrange 产生的随机数区间只包含左极限，也就是左闭右开的[1, n)，1能取到，而n取不到。

# 浮点数： price = "{:.02f}".format(price)
# newword = float(word[1:]) * (100 - discount) / 100
# newword = "%.2f" % newword

import bisect
# bisect_right：
# 若序列a中存在与x相同的元素，则返回x相等元素右侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x左侧距离最近元素插入点的索引位置
# pos = bisect.bisect_right(left, tail)
# bisect_left：
# 若序列a中存在与x相同的元素，则返回x相等元素左侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x右侧距离最近元素插入点的索引位置

# Map = [['U' for _ in range(n)] for _ in range(m)]

from functools import lru_cache
from typing import List
# @lru_cache(None)

class Solution:
    def trafficCommand(self, directions: List[str]) -> int:
        [e, s, w, n] = list(map(len, directions))
        [ce, cs, cw, cn] = directions
        dp = [[[[100] * (n + 1) for _ in range(w + 1)] for _ in range(s + 1)] for _ in range(e + 1)]
        # dp[a][b][c][d] 表示 东南西北方向分别走了[a,b,c,d]俩车最少需要的时间
        # 初始化为 100， 表示最大值
        def check(a, b, c, d):
            # 同时，东面开出序号为a的车（如果a为None，表示不开出任何车），南面面开出序号为b的车，...，是否可行?
            o1, o2, o3, o4 = ce[a] if a is not None else None, cs[b] if b is not None else None, cw[c] if c is not None else None, cn[d] if d is not None else None
            if o1 and o2:
                if (o1 == o2) or (o1 == 'W' and o2 == 'N') or (o1 == 'S' and o2 == 'W') or (o1 == 'S' and o2 == 'N'):
                    return False
            if o1 and o4:
                if (o1 == o4) or (o1 == 'W' and o4 == 'S') or (o1 == 'S' and o4 == 'E') or (o1 == 'W' and o4 == 'E'):
                    return False
            if o2 and o3:
                if (o2 == o3) or (o2 == 'N' and o3 == 'E') or (o2 == 'W' and o3 == 'N') or (o2 == 'W' and o3 == 'E'):
                    return False
            if o3 and o4:
                if (o3 == o4) or (o3 == 'E' and o4 == 'S') or (o3 == 'N' and o4 == 'E') or (o3 == 'N' and o4 == 'S'):
                    return False
            if o1 and o3:
                if (o1 == o3) or (o1 == 'W' and o3 == 'N') or (o1 == 'S' and o3 == 'E'):
                    return False
            if o2 and o4:
                if (o2 == o4) or (o2 == 'N' and o4 == 'E') or (o2 == 'W' and o4 == 'S'):
                    return False
            return True

        def func(a, b, c, d):
            res = 100
            for da in range(2):
                for db in range(2):
                    for dc in range(2):
                        for dd in range(2):
                            if da == db == dc == dd == 0:
                                continue
                            if a - da < 0 or b - db < 0 or c - dc < 0 or d - dd < 0:
                                continue
                            if not check(a - da if da else None,
                                         b - db if db else None,
                                         c - dc if dc else None,
                                         d - dd if dd else None):
                                continue
                            # if a == 4 and b == 4 and c == 3 and d == 4 and 5 == dp[a - da][b - db][c - dc][d - dd] < res:
                            #     print(dp[a - da][b - db][c - dc][d - dd], a - da,b - db,c - dc,d - dd)
                            res = min(res, dp[a - da][b - db][c - dc][d - dd])
            return res

        dp[0][0][0][0] = 0
        for a in range(e + 1):
            for b in range(s + 1):
                for c in range(w + 1):
                    for d in range(n + 1):
                        if a == b == c == d == 0:
                            continue
                        dp[a][b][c][d] = func(a, b, c, d) + 1
        # print(dp)
        return dp[-1][-1][-1][-1]



so = Solution()

# print(so.trafficCommand(["WNNNS","WWEW","NNENE","EEWE"]))  # 9
print(so.trafficCommand(["WNNNS","WWEW","NNENE","EEWE"]))  # 9
print(so.trafficCommand(["S","W","N","E"]))  # 2
print(so.trafficCommand(["NS","WE","SE","EW"]))  # 3
print(so.trafficCommand(["W","N","ES","W"]))  # 2



