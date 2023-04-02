# 给你四个整数 length ，width ，height 和 mass ，分别表示一个箱子的三个维度和质量，请你返回一个表示箱子 类别 的字符串。
#
# 如果满足以下条件，那么箱子是 "Bulky" 的：
# 箱子 至少有一个 维度大于等于 104 。
# 或者箱子的 体积 大于等于 109 。
# 如果箱子的质量大于等于 100 ，那么箱子是 "Heavy" 的。
# 如果箱子同时是 "Bulky" 和 "Heavy" ，那么返回类别为 "Both" 。
# 如果箱子既不是 "Bulky" ，也不是 "Heavy" ，那么返回类别为 "Neither" 。
# 如果箱子是 "Bulky" 但不是 "Heavy" ，那么返回类别为 "Bulky" 。
# 如果箱子是 "Heavy" 但不是 "Bulky" ，那么返回类别为 "Heavy" 。
# 注意，箱子的体积等于箱子的长度、宽度和高度的乘积。
#
#
#
# 示例 1：
#
# 输入：length = 1000, width = 35, height = 700, mass = 300
# 输出："Heavy"
# 解释：
# 箱子没有任何维度大于等于 104 。
# 体积为 24500000 <= 109 。所以不能归类为 "Bulky" 。
# 但是质量 >= 100 ，所以箱子是 "Heavy" 的。
# 由于箱子不是 "Bulky" 但是是 "Heavy" ，所以我们返回 "Heavy" 。
# 示例 2：
#
# 输入：length = 200, width = 50, height = 800, mass = 50
# 输出："Neither"
# 解释：
# 箱子没有任何维度大于等于 104 。
# 体积为 8 * 106 <= 109 。所以不能归类为 "Bulky" 。
# 质量小于 100 ，所以不能归类为 "Heavy" 。
# 由于不属于上述两者任何一类，所以我们返回 "Neither" 。
#
#
# 提示：
#
# 1 <= length, width, height <= 105
# 1 <= mass <= 103

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
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        v = length * width * height
        t1 = t2 = False
        if length >= 10 ** 4 or width >=10 ** 4 or height >= 10 ** 4  or v >= 10 ** 9:
            t1 = True
        if mass >= 100:
            t2 = True
        if t1 and t2:
            return "Both"
        if not t1 and not t2:
            return "Neither"
        if t1:
            return "Bulky"
        return "Heavy"


so = Solution()


