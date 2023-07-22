# 给你一个顾客访问商店的日志，用一个下标从 0 开始且只包含字符 'N' 和 'Y' 的字符串 customers 表示：
#
# 如果第 i 个字符是 'Y' ，它表示第 i 小时有顾客到达。
# 如果第 i 个字符是 'N' ，它表示第 i 小时没有顾客到达。
# 如果商店在第 j 小时关门（0 <= j <= n），代价按如下方式计算：
#
# 在开门期间，如果某一个小时没有顾客到达，代价增加 1 。
# 在关门期间，如果某一个小时有顾客到达，代价增加 1 。
# 请你返回在确保代价 最小 的前提下，商店的 最早 关门时间。
#
# 注意，商店在第 j 小时关门表示在第 j 小时以及之后商店处于关门状态。
#
#
#
# 示例 1：
#
# 输入：customers = "YYNY"
# 输出：2
# 解释：
# - 第 0 小时关门，总共 1+1+0+1 = 3 代价。
# - 第 1 小时关门，总共 0+1+0+1 = 2 代价。
# - 第 2 小时关门，总共 0+0+0+1 = 1 代价。
# - 第 3 小时关门，总共 0+0+1+1 = 2 代价。
# - 第 4 小时关门，总共 0+0+1+0 = 1 代价。
# 在第 2 或第 4 小时关门代价都最小。由于第 2 小时更早，所以最优关门时间是 2 。
# 示例 2：
#
# 输入：customers = "NNNNN"
# 输出：0
# 解释：最优关门时间是 0 ，因为自始至终没有顾客到达。
# 示例 3：
#
# 输入：customers = "YYYY"
# 输出：4
# 解释：最优关门时间是 4 ，因为每一小时均有顾客到达。
#
#
# 提示：
#
# 1 <= customers.length <= 105
# customers 只包含字符 'Y' 和 'N' 。
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
    def bestClosingTime(self, customers: str) -> int:
        customers += 'N'
        n = len(customers)
        # s1, s2 = [0 if customers[0] == 'Y' else 1], [1 if customers[-1] == 'Y' else 0]
        s1, s2 = [0] * n, [0] * n
        if customers[0] == 'N':
            s1[0] = 1
        if customers[-1] == 'Y':
            s2[n - 1] = 1
        for i in range(1, n):
            s1[i] = s1[i - 1]
            if customers[i] == 'N':
                s1[i] += 1
        # for c in customers[n - 2::-1]:
        for i in range(n - 2, -1, -1):
            s2[i] = s2[i + 1]
            if customers[i] == 'Y':
                s2[i] += 1
        # print(s1, s2)
        cost = s2[0]
        ans = 0
        for i in range(1, n):
            if s1[i - 1] + s2[i] < cost:
                cost = s1[i - 1] + s2[i]
                ans = i
        # if cost > s1[-1]:
        #     return n
        return ans


so = Solution()
print(so.bestClosingTime("YNYY"))
print(so.bestClosingTime("YYNY"))
print(so.bestClosingTime("NNNNN"))
print(so.bestClosingTime("YYYY"))




