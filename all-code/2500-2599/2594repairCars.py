# 给你一个整数数组 ranks ，表示一些机械工的 能力值 。ranksi 是第 i 位机械工的能力值。能力值为 r 的机械工可以在 r * n2 分钟内修好 n 辆车。
#
# 同时给你一个整数 cars ，表示总共需要修理的汽车数目。
#
# 请你返回修理所有汽车 最少 需要多少时间。
#
# 注意：所有机械工可以同时修理汽车。
#
#
#
# 示例 1：
#
# 输入：ranks = [4,2,3,1], cars = 10
# 输出：16
# 解释：
# - 第一位机械工修 2 辆车，需要 4 * 2 * 2 = 16 分钟。
# - 第二位机械工修 2 辆车，需要 2 * 2 * 2 = 8 分钟。
# - 第三位机械工修 2 辆车，需要 3 * 2 * 2 = 12 分钟。
# - 第四位机械工修 4 辆车，需要 1 * 4 * 4 = 16 分钟。
# 16 分钟是修理完所有车需要的最少时间。
# 示例 2：
#
# 输入：ranks = [5,1,8], cars = 6
# 输出：16
# 解释：
# - 第一位机械工修 1 辆车，需要 5 * 1 * 1 = 5 分钟。
# - 第二位机械工修 4 辆车，需要 1 * 4 * 4 = 16 分钟。
# - 第三位机械工修 1 辆车，需要 8 * 1 * 1 = 8 分钟。
# 16 分钟时修理完所有车需要的最少时间。
#
#
# 提示：
#
# 1 <= ranks.length <= 105
# 1 <= ranks[i] <= 100
# 1 <= cars <= 106

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

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def check(val): # 给定一个时间，计算是否能修完所有汽车
            s = sum(int((val / x) ** 0.5) for x in ranks)
            return s >= cars
        lo, hi = 0, ranks[0] * cars * cars
        while lo < hi - 1:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid
        return hi


so = Solution()
print(so.repairCars(ranks = [4,2,3,1], cars = 10))
print(so.repairCars(ranks = [5,1,8], cars = 6))




