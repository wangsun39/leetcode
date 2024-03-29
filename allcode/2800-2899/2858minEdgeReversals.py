# 给你一个 n 个点的 简单有向图 （没有重复边的有向图），节点编号为 0 到 n - 1 。如果这些边是双向边，那么这个图形成一棵 树 。
#
# 给你一个整数 n 和一个 二维 整数数组 edges ，其中 edges[i] = [ui, vi] 表示从节点 ui 到节点 vi 有一条 有向边 。
#
# 边反转 指的是将一条边的方向反转，也就是说一条从节点 ui 到节点 vi 的边会变为一条从节点 vi 到节点 ui 的边。
#
# 对于范围 [0, n - 1] 中的每一个节点 i ，你的任务是分别 独立 计算 最少 需要多少次 边反转 ，从节点 i 出发经过 一系列有向边 ，可以到达所有的节点。
#
# 请你返回一个长度为 n 的整数数组 answer ，其中 answer[i]表示从节点 i 出发，可以到达所有节点的 最少边反转 次数。
#
#
#
# 示例 1：
#
#
#
# 输入：n = 4, edges = [[2,0],[2,1],[1,3]]
# 输出：[1,1,0,2]
# 解释：上图表示了与输入对应的简单有向图。
# 对于节点 0 ：反转 [2,0] ，从节点 0 出发可以到达所有节点。
# 所以 answer[0] = 1 。
# 对于节点 1 ：反转 [2,1] ，从节点 1 出发可以到达所有节点。
# 所以 answer[1] = 1 。
# 对于节点 2 ：不需要反转就可以从节点 2 出发到达所有节点。
# 所以 answer[2] = 0 。
# 对于节点 3 ：反转 [1,3] 和 [2,1] ，从节点 3 出发可以到达所有节点。
# 所以 answer[3] = 2 。
# 示例 2：
#
#
#
# 输入：n = 3, edges = [[1,2],[2,0]]
# 输出：[2,0,1]
# 解释：上图表示了与输入对应的简单有向图。
# 对于节点 0 ：反转 [2,0] 和 [1,2] ，从节点 0 出发可以到达所有节点。
# 所以 answer[0] = 2 。
# 对于节点 1 ：不需要反转就可以从节点 2 出发到达所有节点。
# 所以 answer[1] = 0 。
# 对于节点 2 ：反转 [1,2] ，从节点 2 出发可以到达所有节点。
# 所以 answer[2] = 1 。
#
#
# 提示：
#
# 2 <= n <= 105
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ui == edges[i][0] < n
# 0 <= vi == edges[i][1] < n
# ui != vi
# 输入保证如果边是双向边，可以得到一棵树。

from typing import List
from typing import Optional
from cmath import *
from collections import deque
# de = deque([1, 2, 3])
# de.append(4)
# de.appendleft(6)
# de.pop()
# de.popleft()
from itertools import pairwise, accumulate
# list(accumulate(nums))  数组前缀和
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# print(c.most_common(2)) # n = 2
#  [('c', 3), ('b', 2)]

# d = defaultdict(int)
# from math import *
import random
# random.uniform(a, b)，用于生成一个指定范围内的随机浮点数，闭区间
# randint和randrange的区别：
# randint 产生的随机数区间是包含左右极限的，也就是说左右都是闭区间的[1, n]，能取到1和n。
# 而 randrange 产生的随机数区间只包含左极限，也就是左闭右开的[1, n)，1能取到，而n取不到。

# 浮点数： price = "{:.02f}".format(price)
# newword = float(word[1:]) * (100 - discount) / 100
# newword = "%.2f" % newword
# a.isalpha()  # 判断字符串中是否所有的字符都是字母
# a.isdigit() # 判断字符串中是否所有的字符都是整数
# a.isalnum()  # 判断字符串中是否所有的字符都是字母or数字
# a.isspace()  # 判断字符串中是否所有的字符都是空白符
# a.swapcase()  # 转换大小写

from bisect import *
# bisect_right：
# 若序列a中存在与x相同的元素，则返回x相等元素右侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x左侧距离最近元素插入点的索引位置
# k = bisect_left(a, x) - 1 # k 表示 < x 的最大下标， 不存在: k == -1
# k = bisect_right(a, x) - 1 # k 表示 <= x 的最大下标， 不存在: k == -1
# k = bisect_right(a, x) # k 表示 > x 的最小下标， 不存在: k == n
# k = bisect_left(a, x)  # k 表示 >= x 的最小下标， 不存在: k == n

# pos = bisect.bisect_right(left, tail)
# bisect_left：
# 若序列a中存在与x相同的元素，则返回x相等元素左侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x右侧距离最近元素插入点的索引位置
from heapq import *
# heap.heapify(nums) # 小顶堆
# heapq.heappop() 函数弹出堆中最小值
# heapq.heappush(nums, 1)
# heapq.heapreplace(heap, item)  删除最小值并添加新值
# 如果需要获取堆中最大或最小的范围值，则可以使用heapq.nlargest() 或heapq.nsmallest() 函数  这2个性能很差

# Map = [['U' for _ in range(n)] for _ in range(m)]
# Map = [['U'] * n for _ in range(m)]

from functools import lru_cache, cache
from typing import List, Tuple
# @lru_cache(None)

# x / y 上取整 (x + y - 1) // y
# x / y 下取整 x // y
# x / y 四舍五入 int(x / y + 0.5)

import string
# string.digits  表示 0123456789
# string.letters：包含所有字母(大写或小写字符串，在python3.0中，使用string.ascii-letters代替)
# string.ascii_lowercase：包含所有小写字母的字符串  ascii_lowercase[x] 当0<=x<26可以得到一个字符
# string.ascii_uppercase：包含所有大写字母的字符串
# string.printable：包含所有可打印字符的字符串
# string.punctuation：包含所有标点的字符串
# string.uppercase：包含所有大写字母的字符串
# c2i = {c: i for i, c in enumerate(ascii_lowercase)}

# f-string用法
# name = 'sun'
# f"Hello, my name is {name}"

from itertools import accumulate
# s = list(accumulate(nums, initial=0))  # 计算前缀和

from sortedcontainers import SortedList, SortedDict, SortedSet
# sl = SortedList()
# sl.add(value) 添加新元素，并排序。时间复杂度O(log(n)).
# sl.update(iterable) 对添加的可迭代的所有元素排序。时间复杂度O(k*log(n)).
# sl.clear() 移除所有元素。时间复杂度O(n).
# sl.discard(value) 移除一个值元素，如果元素不存在，不报错。时间复杂度O(log(n)).
# sl.remove(value) 移除一个值元素，如果元素不存在，报错ValueError。时间复杂度O(log(n)).
# sl.pop(index=-1) 移除一个指定下标元素，如果有序序列为空或者下标超限，报错IndexError.
# sl.bisect_left(value)
# sl.bisect_right(value)
# sl.count(value)
# sl.index(value, start=None, Stop=None) 查找索引范围[start,stop）内第一次出现value的索引，如果value不存在，报错ValueError.

# sd = SortedDict({'a': 1, 'b': 2, 'c': 3})
# skv = sd.keys()  这个是有序的

# ss = SortedSet()
# ss.add(value)
# ss.pop()
# ss.pop(value)
# ss.remove(value)
# ss.remove(value)


# 前缀和
# 左闭右开区间 [left,right) 来表示从 nums[left] 到 nums[right−1] 的子数组，
# 此时子数组的和为 s[right]−s[left]，子数组的长度为 right−left。
# s = list(accumulate(nums, initial=0))

# dir = [[-1, 0], [1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1], [0, -1], [0, 1]]
# dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]
# list(zip(nums))  # [([7, 2, 1],), ([6, 4, 2],), ([6, 5, 3],), ([3, 2, 1],)]   合并
# list(zip(*nums))  # [(7, 6, 6, 3), (2, 4, 5, 2), (1, 2, 3, 1)]    转置

class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for x, y in edges:
            g[x].append((y, 0))  # 第二个参数表示方向
            g[y].append((x, 1))
        def dfs1(x, fa):  # 计算从x出发 最少边反转数
            res = 0
            for y, d in g[x]:
                if y != fa:
                    res += d
                    res += dfs1(y, x)
            return res
        ans = [0] * n
        ans[0] = dfs1(0, -1)
        def dfs2(x, fa):  # 换根 DP
            for y, d in g[x]:
                if y != fa:
                    if d == 0:
                        ans[y] = ans[x] + 1
                    else:
                        ans[y] = ans[x] - 1
                    dfs2(y, x)
        dfs2(0, -1)
        return ans

so = Solution()
print(so.minEdgeReversals(n = 4, edges = [[2,0],[2,1],[1,3]]))
print(so.minEdgeReversals(n = 3, edges = [[1,2],[2,0]]))




