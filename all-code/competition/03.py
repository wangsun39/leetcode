
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

class Solution:

    def squareFreeSubsets(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        primes = [2,3,5,7,11,13,17,19,23,29]
        m = 1024
        nums = [x for x in nums if x % 4 and x % 9 and x % 16 and x % 25]
        # print(nums)
        n = len(nums)
        if n == 0: return 0
        bi = [0] * n
        for i, x in enumerate(nums):
            bb = 0
            for j, p in enumerate(primes):
                if x % p == 0:
                    bb |= (1 << j)
            bi[i] = bb
        # print(bi)
        dp = [[0] * m for _ in range(n)]  # 前 i 个数中，乘积为 j 的子数组数量
        for i in range(n):
            dp[i][bi[i]] = 1
        # print(dp)
        for i in range(1, n):
            for j in range(m):
                dp[i][j] += dp[i - 1][j]
                dp[i][j] %= MOD
            for j in range(m):
                if bi[i] & j == 0:
                    dp[i][bi[i] | j] += dp[i - 1][j]
                    dp[i][bi[i] | j] %= MOD
        ans = 0
        for i in range(m):
            # print(i)
            ans += dp[-1][i]
        return ans % MOD




so = Solution()
print(so.squareFreeSubsets([1,23,25,1,2,1]))  # 31
print(so.squareFreeSubsets([14,5,21,22,20,21,22]))  # 19
print(so.squareFreeSubsets([16,25,4,4,25,16,9,4,4,16,9,4,16,4,9,25,9,4,25,25,25,16,25,9,9,4,25,25,4,16,9,9,16,25,25,25,4,4,4,25,9,9,16,4,4,25,16,16,4,4,9,9,4,16,25,16,25,4,9,25,4,9,25,9,16,4,16,16,9,9,4,9,25,9,9,9,4,16,25,4,25,9,4,25,16,4,25,25,16,16,16,9,16,9,25,25,4,9,4,25]))
print(so.squareFreeSubsets([14,5,21,22,20,21,22,29,25,22,18,13,8,6,2,1,23,25,1,2,1,14,24,1,4,22,12,26,12,12,16,23,14,27,1,14,10,24,25,10,8,8,26,26,10,15,11,3,29,29,19,26,10,5,15,29,15,9,27,20,14,29,22,28,1,4,11,21,30,30,26,19,14,11,29,12,24,18,9,23,15,18,9,11,1,18,8,10,13,3,17,22,1,10,22,11]))
print(so.squareFreeSubsets([3,4,4,5]))
print(so.squareFreeSubsets([1]))




