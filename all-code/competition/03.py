
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
# lowbit(i) 即i&-i	返回i的最后一位1
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


class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        d = {}
        ans = 1e10
        maxA = 0
        for num in nums:
            remain = num % space
            if remain in d:
                d[remain][0] += 1
                d[remain][1] = min(d[remain][1], num)
            else:
                d[remain] = [1, num]
            if d[remain][0] > maxA:
                ans = d[remain][1]
                maxA = d[remain][0]
            elif d[remain][0] == maxA:
                ans = min(ans, d[remain][1])
        return ans



so = Solution()
print(so.destroyTargets(nums = [3,7,8,1,1,5], space = 2))
print(so.destroyTargets(nums = [1,5,3,2,2], space = 10000))
print(so.destroyTargets(nums = [3,7,8,1,1,5], space = 2))
print(so.destroyTargets(nums = [1,3,5,2,4,6], space = 2))
print(so.destroyTargets(nums = [6,2,5], space = 100))




