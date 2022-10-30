# 给你两个正整数 n 和 target 。
#
# 如果某个整数每一位上的数字相加小于或等于 target ，则认为这个整数是一个 美丽整数 。
#
# 找出并返回满足 n + x 是 美丽整数 的最小非负整数 x 。生成的输入保证总可以使 n 变成一个美丽整数。
#
#
#
# 示例 1：
#
# 输入：n = 16, target = 6
# 输出：4
# 解释：最初，n 是 16 ，且其每一位数字的和是 1 + 6 = 7 。在加 4 之后，n 变为 20 且每一位数字的和变成 2 + 0 = 2 。可以证明无法加上一个小于 4 的非负整数使 n 变成一个美丽整数。
# 示例 2：
#
# 输入：n = 467, target = 6
# 输出：33
# 解释：最初，n 是 467 ，且其每一位数字的和是 4 + 6 + 7 = 17 。在加 33 之后，n 变为 500 且每一位数字的和变成 5 + 0 + 0 = 5 。可以证明无法加上一个小于 33 的非负整数使 n 变成一个美丽整数。
# 示例 3：
#
# 输入：n = 1, target = 1
# 输出：0
# 解释：最初，n 是 1 ，且其每一位数字的和是 1 ，已经小于等于 target 。
#
#
# 提示：
#
# 1 <= n <= 1012
# 1 <= target <= 150
# 生成的输入保证总可以使 n 变成一个美丽整数。
# https://leetcode.cn/problems/minimum-addition-to-make-integer-beautiful/

from typing import List
from typing import Optional
from collections import deque
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
# n.bit_length()
# value = int(s, 2)

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

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        mi, ma = min(nums), max(nums)
        n = len(nums)
        z = [[nums[i], cost[i]] for i in range(n)]
        z.sort()
        C1, C2 = z[0][1], sum(cost) - z[0][1]
        cur = ans = sum(z[i][1] * (z[i][0] - mi) for i in range(n))
        idx = 1
        for i in range(mi + 1, ma + 1):
            cur = cur + C1 - C2
            ans = min(cur, ans)
            while idx < n and z[idx][0] == i:
                C2 -= z[idx][1]
                C1 += z[idx][1]
                idx += 1
        return ans

    # def minCost(self, nums: List[int], cost: List[int]) -> int: # 利用一个性质：最小值一定能在 i == 某个nums中的值 取到
    #     mi, ma = min(nums), max(nums)
    #     n = len(nums)
    #     z = [[nums[i], cost[i]] for i in range(n)]
    #     z.sort()
    #     C1, C2 = z[0][1], sum(cost) - z[0][1]
    #     cur = ans = sum(z[i][1] * (z[i][0] - mi) for i in range(n))
    #     idx = 1
    #     for i in range(mi + 1, ma + 1):
    #         cur = cur + C1 - C2
from typing import List
from typing import Optional
from cmath import inf
from collections import deque
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
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def sumof(num):
            s = str(num)
            return sum(int(ss) for ss in s)
        n1 = n
        dec = 10
        while sumof(n1) > target:
            while n1 % dec == 0:
                dec *= 10
            tail = n1 % dec
            add = dec - tail
            n1 = n1 + add
        return n1 - n


so = Solution()
print(so.makeIntegerBeautiful(n = 467, target = 4))
print(so.makeIntegerBeautiful(n = 467, target = 6))
print(so.makeIntegerBeautiful(n = 16, target = 6))








