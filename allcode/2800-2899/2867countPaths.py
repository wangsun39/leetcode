# 给你一棵 n 个节点的无向树，节点编号为 1 到 n 。给你一个整数 n 和一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ui, vi] 表示节点 ui 和 vi 在树中有一条边。
#
# 请你返回树中的 合法路径数目 。
#
# 如果在节点 a 到节点 b 之间 恰好有一个 节点的编号是质数，那么我们称路径 (a, b) 是 合法的 。
#
# 注意：
#
# 路径 (a, b) 指的是一条从节点 a 开始到节点 b 结束的一个节点序列，序列中的节点 互不相同 ，且相邻节点之间在树上有一条边。
# 路径 (a, b) 和路径 (b, a) 视为 同一条 路径，且只计入答案 一次 。
#
#
# 示例 1：
#
#
#
# 输入：n = 5, edges = [[1,2],[1,3],[2,4],[2,5]]
# 输出：4
# 解释：恰好有一个质数编号的节点路径有：
# - (1, 2) 因为路径 1 到 2 只包含一个质数 2 。
# - (1, 3) 因为路径 1 到 3 只包含一个质数 3 。
# - (1, 4) 因为路径 1 到 4 只包含一个质数 2 。
# - (2, 4) 因为路径 2 到 4 只包含一个质数 2 。
# 只有 4 条合法路径。
# 示例 2：
#
#
#
# 输入：n = 6, edges = [[1,2],[1,3],[2,4],[3,5],[3,6]]
# 输出：6
# 解释：恰好有一个质数编号的节点路径有：
# - (1, 2) 因为路径 1 到 2 只包含一个质数 2 。
# - (1, 3) 因为路径 1 到 3 只包含一个质数 3 。
# - (1, 4) 因为路径 1 到 4 只包含一个质数 2 。
# - (1, 6) 因为路径 1 到 6 只包含一个质数 3 。
# - (2, 4) 因为路径 2 到 4 只包含一个质数 2 。
# - (3, 6) 因为路径 3 到 6 只包含一个质数 3 。
# 只有 6 条合法路径。
#
#
# 提示：
#
# 1 <= n <= 105
# edges.length == n - 1
# edges[i].length == 2
# 1 <= ui, vi <= n
# 输入保证 edges 形成一棵合法的树。

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

def euler_all_primes(n):
    is_prime = [False, False] + [True] * (n - 1)
    primes = []
    flg = False
    for i in range(2, n + 1):
        if is_prime[i]: primes.append(i)
        if flg: continue
        for j in primes:
            if j * i > n: break
            is_prime[j * i] = False
            if i % j == 0: break

    return primes

primes = set(euler_all_primes(100009))

class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        ans = 0
        def dfs(x, fa):  # 返回从x开始的没有质数的路径和有一个质数的路径数
            nonlocal ans
            r1 = r2 = 0
            yl = []
            if x not in primes:
                for y in g[x]:
                    if y != fa:
                        ry1, ry2 = dfs(y, x)
                        if y in primes:
                            r1 += ry1
                            r2 += (ry2 + 1)
                            yl.append([ry1, ry2 + 1])
                        else:
                            r1 += (ry1 + 1)
                            r2 += ry2
                            yl.append([ry1 + 1, ry2])
            else:
                for y in g[x]:
                    if y != fa:
                        ry1, ry2 = dfs(y, x)
                        if y not in primes:
                            r2 += (ry1 + 1)
                            yl.append([ry1 + 1, ry2 + 1])
            s1, s2 = sum(e[0] for e in yl), sum(e[1] for e in yl)
            if x not in primes:
                for a, b in yl:
                    ans += b * (s1 - a)
            else:
                ss = 0
                for a, b in yl:
                    ss += a * (s1 - a)
                ss //= 2
                ans += ss
            ans += r2
            return r1, r2

        dfs(1, -1)
        return ans

so = Solution()
ll = [[1, x] for x in range(2, 100001)]
print(so.countPaths(100000, ll))
print(so.countPaths(8, [[6,7],[4,7],[1,7],[3,4],[2,4],[5,2],[8,3]]))
print(so.countPaths(9, [[7,4],[3,4],[5,4],[1,5],[6,4],[9,5],[8,7],[2,8]]))
print(so.countPaths(n = 5, edges = [[1,2],[1,3],[2,4],[2,5]]))
print(so.countPaths(n = 6, edges = [[1,2],[1,3],[2,4],[3,5],[3,6]]))





