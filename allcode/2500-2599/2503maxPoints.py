# 给你一个大小为 m x n 的整数矩阵 grid 和一个大小为 k 的数组 queries 。
#
# 找出一个大小为 k 的数组 answer ，且满足对于每个整数 queres[i] ，你从矩阵 左上角 单元格开始，重复以下过程：
#
# 如果 queries[i] 严格 大于你当前所处位置单元格，如果该单元格是第一次访问，则获得 1 分，并且你可以移动到所有 4 个方向（上、下、左、右）上任一 相邻 单元格。
# 否则，你不能获得任何分，并且结束这一过程。
# 在过程结束后，answer[i] 是你可以获得的最大分数。注意，对于每个查询，你可以访问同一个单元格 多次 。
#
# 返回结果数组 answer 。
#
#
#
# 示例 1：
#
#
# 输入：grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
# 输出：[5,8,1]
# 解释：上图展示了每个查询中访问并获得分数的单元格。
# 示例 2：
#
#
# 输入：grid = [[5,2,1],[1,1,2]], queries = [3]
# 输出：[0]
# 解释：无法获得分数，因为左上角单元格的值大于等于 3 。
#
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 1000
# 4 <= m * n <= 105
# k == queries.length
# 1 <= k <= 104
# 1 <= grid[i][j], queries[i] <= 106
from typing import List
from typing import Optional
from cmath import inf
from collections import deque
# de = deque([1, 2, 3])
# de.append(4)
# de.appendleft(6)
# de.pop()
# de.popleft()
from itertools import pairwise
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
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        # 比赛中的方法，通过不了最后一个用例，可能这个用例是后加的
        row, col = len(grid), len(grid[0])
        n = len(queries)
        ans = []
        qu = [[i, e] for i, e in enumerate(queries)]
        qu.sort(key=lambda x: x[1])
        queue = deque([[0, 0]])
        flag = set()  # 放入过队列中的点（包括已经被覆盖的点，和在队列中的点）
        flag.add((0,0))
        pre = 0
        def bfs(val):
            nonlocal queue
            q = deque([])
            res = 0
            dir = [[-1,0],[1,0],[0,-1],[0,1]]
            while len(queue):
                x, y = queue.popleft()
                if grid[x][y] >= val:
                    q.append([x, y])
                    continue
                res += 1
                for u, v in dir:
                    xx, yy = x + u, y + v
                    if 0 <= xx < row and 0 <= yy < col and (xx, yy) not in flag:
                        queue.append([xx, yy])
                        flag.add((xx, yy))
            queue = q
            return res

        for i in range(n):
            cur = bfs(qu[i][1])
            ans.append(pre + cur)
            pre += cur
        anss = [0] * n
        for i in range(n):
            j = qu[i][0]
            anss[j] = ans[i]
        return anss

    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        # 2023/2/18  优先队列
        ans = [0] * len(queries)
        r, c = len(grid), len(grid[0])
        dir = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        nextq = [[grid[0][0], 0, 0]]
        heapify(nextq)
        vis = {(0, 0)}
        s = 0
        def helper(val):
            nonlocal s
            while len(nextq) and nextq[0][0] < val:
                v, x, y = heappop(nextq)
                # vis.add((x, y))
                s += 1
                for u, v in dir:
                    xx, yy = x + u, y + v
                    if 0 <= xx < r and 0 <= yy < c and (xx, yy) not in vis:
                        heappush(nextq, [grid[xx][yy], xx, yy])
                        vis.add((xx, yy))

            return s

        for x, i in sorted([[x, i] for i, x in enumerate(queries)]):
            ans[i] = helper(x)
        return ans


so = Solution()
print(so.maxPoints(grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]))
print(so.maxPoints([[5,2,1],[1,1,2]], queries = [3]))




