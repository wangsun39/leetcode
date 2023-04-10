
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
from math import *
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
# Map = [['U'] * n for _ in range(m)]

from functools import lru_cache, cache
from typing import List, Tuple
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
# string.ascii_uppercase：包含所有大写字母的字符串
# string.printable：包含所有可打印字符的字符串
# string.punctuation：包含所有标点的字符串
# string.uppercase：包含所有大写字母的字符串

# f-string用法
# name = 'sun'
# f"Hello, my name is {name}"

from itertools import accumulate
# s = list(accumulate(nums, initial=0))  # 计算前缀和

from sortedcontainers import SortedList
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

# 前缀和
# 左闭右开区间 [left,right) 来表示从 nums[left] 到 nums[right−1] 的子数组，
# 此时子数组的和为 s[right]−s[left]，子数组的长度为 right−left。
# s = list(accumulate(nums, initial=0))

# dir = [[-1, 0], [1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1], [0, -1], [0, 1]]
# dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]


class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        if r == 1 and c == 1: return 1
        q1 = deque()
        q1.append((0, 0))
        vis_r = [0] * c  # 每行最右端访问到哪个节点
        vis_c = [0] * r  # 每列最下端访问到哪个节点
        vis = {(0, 0)}
        ans = 1
        while len(q1):
            q2 = deque()
            while len(q1):
                x, y = q1.popleft()
                if x == r - 1 and y == c - 1:
                    return ans
                if grid[0][0] == 0: continue

                if vis_c[x] < c - 1:
                    right = min((max(vis_c[x], grid[x][y] + y), c - 1))
                    if x == r - 1 and right == c - 1:
                        return ans + 1
                    for i in range(max(y + 1, vis_c[x] + 1), right + 1):
                        # 这个地方 max(y + 1, vis_c[x] + 1) 很关键，
                        # 比赛就是直接从 vis_c[x] + 1 开始，实际是错误的，
                        # y 有可能 比 vis_c[x] 大，此时 vis_c[x] 前面的节点不一定都访问到
                        # 但这并不影响结构，假如后面访问到 vis_c[x] 前面节点的可以继续处理，
                        if (x, i) in vis: continue  # 用 vis，避免重复放入队列，不用也是可以的
                        q2.append((x, i))
                        vis.add((x, i))
                    vis_c[x] = right
                if vis_r[y] < r - 1:
                    down = min(max(vis_r[y], grid[x][y] + x), r - 1)
                    if y == c - 1 and down == r - 1:
                        return ans + 1
                    for i in range(max(x + 1, vis_r[y] + 1), down + 1):
                        if (i, y) in vis: continue
                        q2.append((i, y))
                        vis.add((i, y))
                    vis_r[y] = down
            q1 = q2
            ans += 1

        return -1



so = Solution()

print(so.minimumVisitedCells([[13,16,10,4,7,17,17,0,8,15,13,15,8,13,3,7,13,12,11,3,0,3,3,5,5,1,5,1,9,3,5,5,3,11,3,5,11,6,7,8,4,0,0,5,5,6,0,3,5,1,3,2,7,2,7,5,0,4,5,3,1,2,1,3,4,3,1,1,4,0,0,4,2,3,2,0,3,0,1,2,0,0,2,2,1],[17,5,14,2,16,5,0,16,9,14,5,1,10,5,3,3,5,6,13,10,12,13,3,12,8,3,2,6,8,1,10,2,6,4,4,5,4,7,3,4,3,4,6,9,3,7,1,3,1,8,4,0,6,3,2,2,6,6,1,4,1,3,5,1,2,0,0,3,4,1,1,0,1,0,3,1,0,1,0,0,2,2,2,1,1],[2,3,7,16,7,4,1,15,2,4,4,4,14,12,15,10,4,1,1,2,4,5,1,5,9,9,8,0,10,10,1,1,2,6,0,6,4,8,10,9,8,5,8,4,8,5,3,5,8,6,3,2,0,6,5,3,3,0,6,1,2,1,4,0,5,4,3,1,2,3,0,2,1,2,2,1,1,1,2,0,1,1,1,0,0]]))
print(so.minimumVisitedCells([[1,1,0],[0,1,0]]))
print(so.minimumVisitedCells([[0,1,0]]))
print(so.minimumVisitedCells([[1,0]]))
print(so.minimumVisitedCells([[0]]))
print(so.minimumVisitedCells([[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]))
print(so.minimumVisitedCells([[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]]))
print(so.minimumVisitedCells([[2,1,0],[1,0,0]]))




