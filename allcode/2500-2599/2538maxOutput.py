# 给你一个 n 个节点的无向无根图，节点编号为 0 到 n - 1 。给你一个整数 n 和一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间有一条边。
#
# 每个节点都有一个价值。给你一个整数数组 price ，其中 price[i] 是第 i 个节点的价值。
#
# 一条路径的 价值和 是这条路径上所有节点的价值之和。
#
# 你可以选择树中任意一个节点作为根节点 root 。选择 root 为根的 开销 是以 root 为起点的所有路径中，价值和 最大的一条路径与最小的一条路径的差值。
#
# 请你返回所有节点作为根节点的选择中，最大 的 开销 为多少。
#
#
#
# 示例 1：
#
#
#
# 输入：n = 6, edges = [[0,1],[1,2],[1,3],[3,4],[3,5]], price = [9,8,7,6,10,5]
# 输出：24
# 解释：上图展示了以节点 2 为根的树。左图（红色的节点）是最大价值和路径，右图（蓝色的节点）是最小价值和路径。
# - 第一条路径节点为 [2,1,3,4]：价值为 [7,8,6,10] ，价值和为 31 。
# - 第二条路径节点为 [2] ，价值为 [7] 。
# 最大路径和与最小路径和的差值为 24 。24 是所有方案中的最大开销。
# 示例 2：
#
#
#
# 输入：n = 3, edges = [[0,1],[1,2]], price = [1,1,1]
# 输出：2
# 解释：上图展示了以节点 0 为根的树。左图（红色的节点）是最大价值和路径，右图（蓝色的节点）是最小价值和路径。
# - 第一条路径包含节点 [0,1,2]：价值为 [1,1,1] ，价值和为 3 。
# - 第二条路径节点为 [0] ，价值为 [1] 。
# 最大路径和与最小路径和的差值为 2 。2 是所有方案中的最大开销。
#
#
# 提示：
#
# 1 <= n <= 105
# edges.length == n - 1
# 0 <= ai, bi <= n - 1
# edges 表示一棵符合题面要求的树。
# price.length == n
# 1 <= price[i] <= 105

from typing import List
from typing import Optional
from cmath import inf
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

from bisect import *
# bisect_right：
# 若序列a中存在与x相同的元素，则返回x相等元素右侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x左侧距离最近元素插入点的索引位置
# pos = bisect.bisect_right(left, tail)
# bisect_left：
# 若序列a中存在与x相同的元素，则返回x相等元素左侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x右侧距离最近元素插入点的索引位置
from heapq import *
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

# x / y 上取整 (x + y - 1) // y
# x / y 下取整 x // y
# x / y 四舍五入 int(x / y + 0.5)

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

from sortedcontainers import SortedList
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
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        graph = defaultdict(set)
        for x, y in edges:
            graph[x].add(y)
            graph[y].add(x)
        ans = 0
        def dfs1(x, fa):  # 如果计算的是一条完整的链，可以用这个方法
            nonlocal ans
            h1 = h2 = 0  # 分别表示 x 的价值最大的两个链 (从 x 到叶子)
            for y in graph[x]:
                if y == fa: continue
                sr, sh = dfs(y, x)
                [h1, h2, sh] = sorted([h1, h2, sh], reverse=True)
            r = price[x] + h1 + h2  # 分别表示 x 的子树上最长价值路径
            ans = max(ans, r)
            return r, price[x] + h1
        def dfs(x, fa):
            nonlocal ans
            s1, s2 = price[x], 0  # 分别表示包含端点的最大价值链和不包含端点的最大价值链
            for y in graph[x]:
                if y == fa: continue
                ss1, ss2 = dfs(y, x)
                ans = max(ans, s1 + ss2, s2 + ss1)
                s1 = max(s1, ss1 + price[x])
                s2 = max(s2, ss2 + price[x])
            return s1, s2
        dfs(0, -1)
        return ans


so = Solution()
print(so.maxOutput(n = 6, edges = [[0,1],[1,2],[1,3],[3,4],[3,5]], price = [9,8,7,6,10,5]))
print(so.maxOutput(n = 3, edges = [[0,1],[1,2]], price = [1,1,1]))




