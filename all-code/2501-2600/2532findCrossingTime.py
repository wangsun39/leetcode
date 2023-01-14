# 共有 k 位工人计划将 n 个箱子从旧仓库移动到新仓库。给你两个整数 n 和 k，以及一个二维整数数组 time ，数组的大小为 k x 4 ，其中 time[i] = [leftToRighti, pickOldi, rightToLefti, putNewi] 。
#
# 一条河将两座仓库分隔，只能通过一座桥通行。旧仓库位于河的右岸，新仓库在河的左岸。开始时，所有 k 位工人都在桥的左侧等待。为了移动这些箱子，第 i 位工人（下标从 0 开始）可以：
#
# 从左岸（新仓库）跨过桥到右岸（旧仓库），用时 leftToRighti 分钟。
# 从旧仓库选择一个箱子，并返回到桥边，用时 pickOldi 分钟。不同工人可以同时搬起所选的箱子。
# 从右岸（旧仓库）跨过桥到左岸（新仓库），用时 rightToLefti 分钟。
# 将箱子放入新仓库，并返回到桥边，用时 putNewi 分钟。不同工人可以同时放下所选的箱子。
# 如果满足下面任一条件，则认为工人 i 的 效率低于 工人 j ：
#
# leftToRighti + rightToLefti > leftToRightj + rightToLeftj
# leftToRighti + rightToLefti == leftToRightj + rightToLeftj 且 i > j
# 工人通过桥时需要遵循以下规则：
#
# 如果工人 x 到达桥边时，工人 y 正在过桥，那么工人 x 需要在桥边等待。
# 如果没有正在过桥的工人，那么在桥右边等待的工人可以先过桥。如果同时有多个工人在右边等待，那么 效率最低 的工人会先过桥。
# 如果没有正在过桥的工人，且桥右边也没有在等待的工人，同时旧仓库还剩下至少一个箱子需要搬运，此时在桥左边的工人可以过桥。如果同时有多个工人在左边等待，那么 效率最低 的工人会先过桥。
# 所有 n 个盒子都需要放入新仓库，请你返回最后一个搬运箱子的工人 到达河左岸 的时间。
#
#
#
# 示例 1：
#
# 输入：n = 1, k = 3, time = [[1,1,2,1],[1,1,3,1],[1,1,4,1]]
# 输出：6
# 解释：
# 从 0 到 1 ：工人 2 从左岸过桥到达右岸。
# 从 1 到 2 ：工人 2 从旧仓库搬起一个箱子。
# 从 2 到 6 ：工人 2 从右岸过桥到达左岸。
# 从 6 到 7 ：工人 2 将箱子放入新仓库。
# 整个过程在 7 分钟后结束。因为问题关注的是最后一个工人到达左岸的时间，所以返回 6 。
# 示例 2：
#
# 输入：n = 3, k = 2, time = [[1,9,1,8],[10,10,10,10]]
# 输出：50
# 解释：
# 从 0 到 10 ：工人 1 从左岸过桥到达右岸。
# 从 10 到 20 ：工人 1 从旧仓库搬起一个箱子。
# 从 10 到 11 ：工人 0 从左岸过桥到达右岸。
# 从 11 到 20 ：工人 0 从旧仓库搬起一个箱子。
# 从 20 到 30 ：工人 1 从右岸过桥到达左岸。
# 从 30 到 40 ：工人 1 将箱子放入新仓库。
# 从 30 到 31 ：工人 0 从右岸过桥到达左岸。
# 从 31 到 39 ：工人 0 将箱子放入新仓库。
# 从 39 到 40 ：工人 0 从左岸过桥到达右岸。
# 从 40 到 49 ：工人 0 从旧仓库搬起一个箱子。
# 从 49 到 50 ：工人 0 从右岸过桥到达左岸。
# 从 50 到 58 ：工人 0 将箱子放入新仓库。
# 整个过程在 58 分钟后结束。因为问题关注的是最后一个工人到达左岸的时间，所以返回 50 。
#
#
# 提示：
#
# 1 <= n, k <= 104
# time.length == k
# time[i].length == 4
# 1 <= leftToRighti, pickOldi, rightToLefti, putNewi <= 1000

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

class Worker:
    def __init__(self, i, time):
        self.id = i
        self.l2r, self.pick, self.r2l, self.put = time
    def __lt__(self, other):
        if self.l2r + self.r2l == other.l2r + other.r2l:
            return self.id > other.id
        return self.l2r + self.r2l > other.l2r + other.r2l

class Task:
    def __init__(self, i, time, finish_t):
        self.id = i
        self.time = time
        self.finish_t = finish_t
    def __lt__(self, other):
        return self.finish_t < other.finish_t


class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        wait_l, wait_r = [], []
        picks, puts = [], []
        for i, t in enumerate(time):
            heappush(wait_l, Worker(i, t))
        cur = 0
        n1 = n2 = 0  # 分别表示出发的人次数目，和送到的箱子数目
        while True:
            if len(wait_r):  # 桥左右的等待队列每次pop出一个工人，并改变当前的时间
                wk = heappop(wait_r)
                n2 += 1
                if n2 == n:
                    return cur + wk.r2l
                tsk = Task(wk.id, [wk.l2r, wk.pick, wk.r2l, wk.put], cur + wk.r2l + wk.put)
                heappush(puts, tsk)
                cur += wk.r2l
            elif len(wait_l) and n1 < n:
                n1 += 1
                wk = heappop(wait_l)
                tsk = Task(wk.id, [wk.l2r, wk.pick, wk.r2l, wk.put], cur + wk.l2r + wk.pick)
                heappush(picks, tsk)
                cur += wk.l2r
            else:
                cur += 1  # 如果本轮时间没有pop出任何工人，也需要把时间++

            # 把当前时间之前的，所有puts和picks中的工人全都pop出来，入队
            while len(puts) and puts[0].finish_t <= cur:
                tsk = heappop(puts)
                wk = Worker(tsk.id, tsk.time)
                heappush(wait_l, wk)
            while len(picks) and picks[0].finish_t <= cur:
                tsk = heappop(picks)
                wk = Worker(tsk.id, tsk.time)
                heappush(wait_r, wk)



so = Solution()
print(so.findCrossingTime(n = 1, k = 3, time = [[1,1,2,1],[1,1,3,1],[1,1,4,1]]))  # 6
print(so.findCrossingTime(n = 3, k = 2, time = [[1,9,1,8],[10,10,10,10]]))  # 50




