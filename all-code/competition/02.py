
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
    # def takeCharacters1(self, s: str, k: int) -> int:
    #     if k == 0: return 0
    #     left, right = {'a': [], 'b': [], 'c': []}, {'a': [], 'b': [], 'c': []}
    #     n = len(s)
    #     f1 = False
    #     for i in range(n):
    #         if len(left[s[i]]) < k:
    #             left[s[i]].append(i + 1)
    #         if len(left['a']) >= k and len(left['b']) >= k and len(left['c']) >= k:
    #             f1 = True
    #             break
    #     if not f1:
    #         return -1
    #     for i in range(n):
    #         if len(right[s[n - i - 1]]) < k:
    #             right[s[n - i - 1]].append(i + 1)
    #         if len(right['a']) >= k and len(right['b']) >= k and len(right['c']) >= k:
    #             break
    #     print(left, right)
    #     ma = min(left['a'][i] + right['a'][k - i - 2] for i in range(k - 1))
    #     ma = min(ma, left['a'][k - 1], right['a'][k - 1])
    #     mb = min(left['b'][i] + right['b'][k - i - 2] for i in range(k - 1))
    #     mb = min(mb, left['b'][k - 1], right['b'][k - 1])
    #     mc = min(left['c'][i] + right['c'][k - i - 2] for i in range(k - 1))
    #     mc = min(mc, left['c'][k - 1], right['c'][k - 1])
    #
    #     m = min(left['a'][i] + right['a'][k - i - 2] +  for i in range(k - 1))
    #     m = min(m, left['a'][k - 1], right['a'][k - 1])
    #     print(ma, mb, mc)
    #     return max(ma, mb, mc)

    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0: return 0
        n = len(s)
        left, right = {'a': [0], 'b': [0], 'c': [0]}, {'a': [0], 'b': [0], 'c': [0]}
        for i in range(n):
            left['a'].append(left['a'][-1])
            right['a'].append(right['a'][-1])
            left['b'].append(left['b'][-1])
            right['b'].append(right['b'][-1])
            left['c'].append(left['c'][-1])
            right['c'].append(right['c'][-1])
            left[s[i]][-1] += 1
            right[s[n - i - 1]][-1] += 1
        print(left)
        if left['a'][-1] < k or left['b'][-1] < k or left['c'][-1] < k:
            return -1
        for i in range(n + 1):
            if left['a'][i] >= k and left['b'][i] >= k and left['c'][i] >= k:
                pl = i
                ans = i
                break
        for i in range(n + 1):
            if right['a'][i] >= k and right['b'][i] >= k and right['c'][i] >= k:
                pr = i
                ans = min(ans, pr)
                break
        pl = 1
        while pr > 0:
            while left['a'][pl] + right['a'][pr] >= k and left['b'][pl] + right['b'][pr] >= k and left['c'][pl] + right['c'][pr] >= k and pr > 0:
                ans = min(ans, pl + pr)
                pr -= 1
            pl += 1
            if left['a'][pl] + right['a'][pr] >= k and left['b'][pl] + right['b'][pr] >= k and left['c'][pl] + right['c'][pr] >= k:
                ans = min(ans, pl + pr)
        return ans


so = Solution()
print(so.takeCharacters(s = "aabaaaacaabc", k = 2))
print(so.takeCharacters(s = "a", k = 1))
# print(so.takeCharacters(s = "aabaaaacaabc", k = 2))




