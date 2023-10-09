# 给你一个大小为 3 * 3 ，下标从 0 开始的二维整数矩阵 grid ，分别表示每一个格子里石头的数目。网格图中总共恰好有 9 个石头，一个格子里可能会有 多个 石头。
#
# 每一次操作中，你可以将一个石头从它当前所在格子移动到一个至少有一条公共边的相邻格子。
#
# 请你返回每个格子恰好有一个石头的 最少移动次数 。
#
#
#
# 示例 1：
#
#
#
# 输入：grid = [[1,1,0],[1,1,1],[1,2,1]]
# 输出：3
# 解释：让每个格子都有一个石头的一个操作序列为：
# 1 - 将一个石头从格子 (2,1) 移动到 (2,2) 。
# 2 - 将一个石头从格子 (2,2) 移动到 (1,2) 。
# 3 - 将一个石头从格子 (1,2) 移动到 (0,2) 。
# 总共需要 3 次操作让每个格子都有一个石头。
# 让每个格子都有一个石头的最少操作次数为 3 。
# 示例 2：
#
#
#
# 输入：grid = [[1,3,0],[1,0,0],[1,0,3]]
# 输出：4
# 解释：让每个格子都有一个石头的一个操作序列为：
# 1 - 将一个石头从格子 (0,1) 移动到 (0,2) 。
# 2 - 将一个石头从格子 (0,1) 移动到 (1,1) 。
# 3 - 将一个石头从格子 (2,2) 移动到 (1,2) 。
# 4 - 将一个石头从格子 (2,2) 移动到 (2,1) 。
# 总共需要 4 次操作让每个格子都有一个石头。
# 让每个格子都有一个石头的最少操作次数为 4 。
#
#
# 提示：
#
# grid.length == grid[i].length == 3
# 0 <= grid[i][j] <= 9
# grid 中元素之和为 9 。

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
# string.ascii_lowercase：包含所有小写字母的字符串
# string.ascii_uppercase：包含所有大写字母的字符串
# string.printable：包含所有可打印字符的字符串
# string.punctuation：包含所有标点的字符串
# string.uppercase：包含所有大写字母的字符串

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
    def minimumMoves(self, grid: List[List[int]]) -> int:
        l1, l2 = [], []
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    l1.append([i, j, 1])
                elif grid[i][j] > 1:
                    l2.append([i, j, grid[i][j]])

        def dfs(l1, l2):
            res = inf
            x = y = -1
            for i, [x, y, n2] in enumerate(l2):
                if n2 == 1:
                    continue
                break
            if x == -1: return 0
            l2[i][2] -= 1
            for j, [u, v, n1] in enumerate(l1):
                if n1 == 0:
                    continue
                d = abs(x - u) + abs(y - v)
                l1[j][2] -= 1
                res = min(res, d + dfs(l1, l2))
                l1[j][2] += 1
            # l2[i][2] += 1
            if res < inf:
                return res
            else:
                return 0
        return dfs(l1, l2)




so = Solution()
print(so.minimumMoves(grid = [[2,2,0],[1,1,0],[0,3,0]]))
print(so.minimumMoves(grid = [[3,2,0],[0,1,0],[0,3,0]]))
print(so.minimumMoves(grid = [[1,1,0],[1,1,1],[1,2,1]]))
print(so.minimumMoves(grid = [[1,3,0],[1,0,0],[1,0,3]]))




