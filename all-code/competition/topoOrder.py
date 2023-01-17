
from typing import List
from typing import Optional
from collections import deque
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)
import math
import random
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
import heapq
# heap.heapify(nums)
# heapq.heappop() 函数弹出堆中最小值
# heapq.heappush(nums, 1)
# 如果需要获取堆中最大或最小的范围值，则可以使用heapq.nlargest() 或heapq.nsmallest() 函数

# Map = [['U' for _ in range(n)] for _ in range(m)]

from functools import lru_cache
from typing import List
# @lru_cache(None)

# bit位 函数：
# n.bit_length()
# value = int(s, 2)


# conditions 中的节点 id 从 0 到 n - 1
# conditions 中每对 [x,y] 表示先x后y，顺序不能颠倒
def buildTopo(conditions, n):
    tree = defaultdict(set)
    pre_num = [0] * n
    for x, y in conditions:
        if y not in tree[x]:
            tree[x].add(y)
            pre_num[y] += 1
    queue = [i for i in range(n) if pre_num[i] == 0]
    ans = []
    while len(queue):
        q = queue.pop(0)
        ans.append(q)
        for x in tree[q]:
            pre_num[x] -= 1
            if pre_num[x] == 0:
                queue.append(x)
    if len(ans) != n:
        return []  # 存在圈
    return ans

# 另一种拓扑序
# 统计每个节点拓扑序小的点的某种属性的极值  (851)
def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
    n = len(quiet)
    tree = defaultdict(set)
    ans = [i for i in range(n)]  # 比自己richer的最安静值对应的id
    preNum = [0] * n
    for x, y in richer:
        if y not in tree[x]:
            tree[x].add(y)
            preNum[y] += 1
    queue = [i for i in range(n) if preNum[i] == 0]
    while len(queue):
        q = queue.pop(0)
        for x in tree[q]:
            preNum[x] -= 1
            if quiet[ans[q]] < quiet[ans[x]]:
                ans[x] = ans[q]
            if preNum[x] == 0:
                queue.append(x)
    return ans





