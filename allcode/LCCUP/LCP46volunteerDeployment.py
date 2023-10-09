# 「力扣挑战赛」有 n 个比赛场馆（场馆编号从 0 开始），场馆之间的通道分布情况记录于二维数组 edges 中，edges[i]= [x, y] 表示第 i 条通道连接场馆 x 和场馆 y(即两个场馆相邻)。初始每个场馆中都有一定人数的志愿者（不同场馆人数可能不同），后续 m 天每天均会根据赛事热度进行志愿者人数调配。调配方案分为如下三种：
#
# 将编号为 idx 的场馆内的志愿者人数减半；
# 将编号为 idx 的场馆相邻的场馆的志愿者人数都加上编号为 idx 的场馆的志愿者人数；
# 将编号为 idx 的场馆相邻的场馆的志愿者人数都减去编号为 idx 的场馆的志愿者人数。
# 所有的调配信息记录于数组 plans 中，plans[i] = [num,idx] 表示第 i 天对编号 idx 的场馆执行了第 num 种调配方案。
# 在比赛结束后对调配方案进行复盘时，不慎将第 0 个场馆的最终志愿者人数丢失，只保留了初始所有场馆的志愿者总人数 totalNum ，以及记录了第 1 ~ n-1 个场馆的最终志愿者人数的一维数组 finalCnt。请你根据现有的信息求出初始每个场馆的志愿者人数，并按场馆编号顺序返回志愿者人数列表。
#
# 注意：
#
# 测试数据保证当某场馆进行第一种调配时，该场馆的志愿者人数一定为偶数；
# 测试数据保证当某场馆进行第三种调配时，该场馆的相邻场馆志愿者人数不为负数；
# 测试数据保证比赛开始时每个场馆的志愿者人数都不超过 10^9；
# 测试数据保证给定的场馆间的道路分布情况中不会出现自环、重边的情况。
# 示例 1：
#
#
# 输入：
# finalCnt = [1,16], totalNum = 21, edges = [[0,1],[1,2]], plans = [[2,1],[1,0],[3,0]]
#
# 输出：[5,7,9]
#
# 解释：
#
#
# 示例 2 ：
#
# 输入：
# finalCnt = [4,13,4,3,8], totalNum = 54, edges = [[0,3],[1,3],[4,3],[2,3],[2,5]], plans = [[1,1],[3,3],[2,5],[1,0]]
#
# 输出：[10,16,9,4,7,8]
#
# 提示：
#
# 2 <= n <= 5*10^4
# 1 <= edges.length <= min((n * (n - 1)) / 2, 5*10^4)
# 0 <= edges[i][0], edges[i][1] < n
# 1 <= plans.length <= 10
# 1 <= plans[i][0] <=3
# 0 <= plans[i][1] < n
# finalCnt.length = n-1
# 0 <= finalCnt[i] < 10^9
# 0 <= totalNum < 5*10^13
#
# https://leetcode.cn/problems/05ZEDJ





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
    def volunteerDeployment(self, finalCnt: List[int], totalNum: int, edges: List[List[int]], plans: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        cur = [[0, x] for x in finalCnt]   # [a, b] 表示 [ax + b]  x 表示最终0场馆人数
        cur.insert(0, [1, 0])
        for num, idx in plans[::-1]:
            pre = [x for x in cur]
            if num == 1:
                pre[idx] = [cur[idx][0] * 2, cur[idx][1] * 2]
            elif num == 2:
                for y in adj[idx]:
                    pre[y][0] -= cur[idx][0]
                    pre[y][1] -= cur[idx][1]
            else:
                for y in adj[idx]:
                    pre[y][0] += cur[idx][0]
                    pre[y][1] += cur[idx][1]
            cur = [x for x in pre]
        xx = (totalNum - sum(e[1] for e in cur)) // sum(e[0] for e in cur)  #
        ans = [e[0] * xx + e[1] for e in cur]
        return ans


so = Solution()
print(so.volunteerDeployment(finalCnt = [1,16], totalNum = 21, edges = [[0,1],[1,2]], plans = [[2,1],[1,0],[3,0]]))  # [5, 7, 9]
print(so.volunteerDeployment(finalCnt = [4,13,4,3,8], totalNum = 54, edges = [[0,3],[1,3],[4,3],[2,3],[2,5]], plans = [[1,1],[3,3],[2,5],[1,0]]))  # [10,16,9,4,7,8]




