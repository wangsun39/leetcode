# 「力扣挑战赛」中 N*M 大小的自行车炫技赛场的场地由一片连绵起伏的上下坡组成，场地的高度值记录于二维数组 terrain 中，场地的减速值记录于二维数组 obstacle 中。
#
# 若选手骑着自行车从高度为 h1 且减速值为 o1 的位置到高度为 h2 且减速值为 o2 的相邻位置（上下左右四个方向），速度变化值为 h1-h2-o2（负值减速，正值增速）。
# 选手初始位于坐标 position 处且初始速度为 1，请问选手可以刚好到其他哪些位置时速度依旧为 1。请以二维数组形式返回这些位置。若有多个位置则按行坐标升序排列，若有多个位置行坐标相同则按列坐标升序排列。
#
# 注意： 骑行过程中速度不能为零或负值
#
# 示例 1：
#
# 输入：position = [0,0], terrain = [[0,0],[0,0]], obstacle = [[0,0],[0,0]]
#
# 输出：[[0,1],[1,0],[1,1]]
#
# 解释：
# 由于当前场地属于平地，根据上面的规则，选手从[0,0]的位置出发都能刚好在其他处的位置速度为 1。
#
# 示例 2：
#
# 输入：position = [1,1], terrain = [[5,0],[0,6]], obstacle = [[0,6],[7,0]]
#
# 输出：[[0,1]]
#
# 解释：
# 选手从 [1,1] 处的位置出发，到 [0,1] 处的位置时恰好速度为 1。
#
# 提示：
#
# n == terrain.length == obstacle.length
# m == terrain[i].length == obstacle[i].length
# 1 <= n <= 100
# 1 <= m <= 100
# 0 <= terrain[i][j], obstacle[i][j] <= 100
# position.length == 2
# 0 <= position[0] < n
# 0 <= position[1] < m
#
# https://leetcode.cn/problems/kplEvH




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
    def bicycleYard(self, position: List[int], terrain: List[List[int]], obstacle: List[List[int]]) -> List[List[int]]:
        row, col = len(terrain), len(terrain[0])
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        already = set()
        ans = []

        def dfs(x, y, v):
            already.add((x, y, v))
            for x1, y1 in dirs:
                if 0 <= x + x1 < row and 0 <= y + y1 < col:
                    v1 = v + terrain[x][y] - terrain[x + x1][y + y1] - obstacle[x + x1][y + y1]
                    if v1 > 0:
                        if (x + x1, y + y1, v1) in already:
                            continue
                        if v1 == 1: ans.append([x + x1, y + y1])
                        dfs(x + x1, y + y1, v1)
        dfs(position[0], position[1], 1)
        return sorted(ans)




so = Solution()
print(so.bicycleYard(position = [0,0], terrain = [[0,0],[0,0]], obstacle = [[0,0],[0,0]]))  # [[0, 1], [1, 0], [1, 1]]
print(so.bicycleYard(position = [1,1], terrain = [[5,0],[0,6]], obstacle = [[0,6],[7,0]]))  # [[0,1]]




