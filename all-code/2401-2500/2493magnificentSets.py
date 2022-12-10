# 给你一个正整数 n ，表示一个 无向 图中的节点数目，节点编号从 1 到 n 。
#
# 同时给你一个二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示节点 ai 和 bi 之间有一条 双向 边。注意给定的图可能是不连通的。
#
# 请你将图划分为 m 个组（编号从 1 开始），满足以下要求：
#
# 图中每个节点都只属于一个组。
# 图中每条边连接的两个点 [ai, bi] ，如果 ai 属于编号为 x 的组，bi 属于编号为 y 的组，那么 |y - x| = 1 。
# 请你返回最多可以将节点分为多少个组（也就是最大的 m ）。如果没办法在给定条件下分组，请你返回 -1 。
#
#
#
# 示例 1：
#
#
#
# 输入：n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
# 输出：4
# 解释：如上图所示，
# - 节点 5 在第一个组。
# - 节点 1 在第二个组。
# - 节点 2 和节点 4 在第三个组。
# - 节点 3 和节点 6 在第四个组。
# 所有边都满足题目要求。
# 如果我们创建第五个组，将第三个组或者第四个组中任何一个节点放到第五个组，至少有一条边连接的两个节点所属的组编号不符合题目要求。
# 示例 2：
#
# 输入：n = 3, edges = [[1,2],[2,3],[3,1]]
# 输出：-1
# 解释：如果我们将节点 1 放入第一个组，节点 2 放入第二个组，节点 3 放入第三个组，前两条边满足题目要求，但第三条边不满足题目要求。
# 没有任何符合题目要求的分组方式。
#
#
# 提示：
#
# 1 <= n <= 500
# 1 <= edges.length <= 104
# edges[i].length == 2
# 1 <= ai, bi <= n
# ai != bi
# 两个点之间至多只有一条边。
from typing import List
from typing import Optional
from cmath import inf
from collections import deque
# de = deque([1, 2, 3])
# de.append(4)
# de.appendleft(6)
# de.pop()
# de.popleft()
#from itertools import pairwise
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
# a.isalpha()  # 判断字符串中是否所有的字符都是字母
# a.isdigit() # 判断字符串中是否所有的字符都是整数
# a.isalnum()  # 判断字符串中是否所有的字符都是字母or数字
# a.isspace()  # 判断字符串中是否所有的字符都是空白符
# a.swapcase()  # 转换大小写

import bisect
# bisect_right：
# 若序列a中存在与x相同的元素，则返回x相等元素右侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x左侧距离最近元素插入点的索引位置
# pos = bisect.bisect_right(left, tail)
# bisect_left：
# 若序列a中存在与x相同的元素，则返回x相等元素左侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x右侧距离最近元素插入点的索引位置
import heapq
# heap.heapify(nums) # 小顶堆
# heapq.heappop() 函数弹出堆中最小值
# heapq.heappush(nums, 1)
# heapq.heapreplace(heap, item)  删除最小值并添加新值
# 如果需要获取堆中最大或最小的范围值，则可以使用heapq.nlargest() 或heapq.nsmallest() 函数

# Map = [['U' for _ in range(n)] for _ in range(m)]

from functools import lru_cache, cache
from typing import List
# @lru_cache(None)

# bit位 函数：
# n.bit_length()  数值的二进制的长度数
# value = int(s, 2)
# lowbit(i) 即i&-i	表示这个数的二进制表示中最低位的1所对应的值
# n>>k & 1	求n的第k位数字
# x | (1 << k)	将x第k位 置为1
# x ^ (1 << k)	将x第k位取反
# x & (x - 1)	将x最右边的1置为0(去掉最右边的1)
# x | (x + 1)	将x最右边的0置为1
# x & 1	判断奇偶性 真为奇，假为偶


import string
# string.digits  表示 0123456789
# string.letters：包含所有字母(大写或小写字符串，在python3.0中，使用string.ascii-letters代替)
# string.ascii_lowercase：包含所有小写字母的字符串
# string.printable：包含所有可打印字符的字符串
# string.punctuation：包含所有标点的字符串
# string.uppercase：包含所有大写字母的字符串

# f-string用法
# name = 'sun'
# f"Hello, my name is {name}"

from itertools import accumulate
# s = list(accumulate(nums, initial=0))  # 计算前缀和

# from sortedcontainers import SortedList
    # SortedList.add(value) 添加新元素，并排序。时间复杂度O(log(n)).
    # SortedList.update(iterable) 对添加的可迭代的所有元素排序。时间复杂度O(k*log(n)).
    # SortedList.clear() 移除所有元素。时间复杂度O(n).
    # SortedList.discard(value) 移除一个值元素，如果元素不存在，不报错。时间复杂度O(log(n)).
    # SortedList.remove(value) 移除一个值元素，如果元素不存在，报错ValueError。时间复杂度O(log(n)).
    # SortedList.pop(index=-1) 移除一个指定下标元素，如果有序序列为空或者下标超限，报错IndexError.
    # SortedList.bisect_left(value)
    # SortedList.bisect_right(value)
    # SortedList.count(value)
    # SortedList.index(value, start=None, Stop=None) 查找索引范围[start,stop）内第一次出现value的索引，如果value不存在，报错ValueError.

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for x, y in edges:
            adj[x - 1].append(y - 1)
            adj[y - 1].append(x - 1)
        color = [0] * n  # 2分图着色，两种颜色，-1 和 1
        def col(i, c):
            color[i] = c
            for x in adj[i]:
                if color[x] == c:
                    return False
                if color[x] == 0:
                    nodes.append(x)
                    if not col(x, -c):
                        return False
            return True

        def bfs(start):   # 从 start 点开始 bfs，start的分组从 grp 开始
            flg = [0] * n
            q1, q2 = deque([start]), deque()
            flg[start] = 1
            ans = 0
            while len(q1):
                ans += 1
                while len(q1):
                    x = q1.popleft()
                    for y in adj[x]:
                        if flg[y] == 1:
                            continue
                        q2.append(y)
                        flg[y] = 1
                q1, q2 = q2, deque()
            return ans

        ans = 0
        for i, node in enumerate(color):
            if node: continue
            nodes = [i]
            if not col(i, 1):  # 对一个连通分量进行着色
                return -1
            mx = 0
            for j in nodes:
                mx = max(mx, bfs(j))
            ans += mx
        return ans






so = Solution()
print(so.magnificentSets(n = 2, edges = [[1,2]]))
print(so.magnificentSets(n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))
print(so.magnificentSets(n = 3, edges = [[1,2],[2,3],[3,1]]))




