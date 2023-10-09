# 给你一个字符串 s ，每个字符是数字 '1' 到 '9' ，再给你两个整数 k 和 minLength 。
#
# 如果对 s 的分割满足以下条件，那么我们认为它是一个 完美 分割：
#
# s 被分成 k 段互不相交的子字符串。
# 每个子字符串长度都 至少 为 minLength 。
# 每个子字符串的第一个字符都是一个 质数 数字，最后一个字符都是一个 非质数 数字。质数数字为 '2' ，'3' ，'5' 和 '7' ，剩下的都是非质数数字。
# 请你返回 s 的 完美 分割数目。由于答案可能很大，请返回答案对 109 + 7 取余 后的结果。
#
# 一个 子字符串 是字符串中一段连续字符串序列。
#
#
#
# 示例 1：
#
# 输入：s = "23542185131", k = 3, minLength = 2
# 输出：3
# 解释：存在 3 种完美分割方案：
# "2354 | 218 | 5131"
# "2354 | 21851 | 31"
# "2354218 | 51 | 31"
# 示例 2：
#
# 输入：s = "23542185131", k = 3, minLength = 3
# 输出：1
# 解释：存在一种完美分割方案："2354 | 218 | 5131" 。
# 示例 3：
#
# 输入：s = "3312958", k = 3, minLength = 1
# 输出：1
# 解释：存在一种完美分割方案："331 | 29 | 58" 。
#
#
# 提示：
#
# 1 <= k, minLength <= s.length <= 1000
# s 每个字符都为数字 '1' 到 '9' 之一。

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
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        MOD = int(1e9 + 7)
        n = len(s)
        if s[0] not in '2357' or s[-1] in '2357':
            return 0
        A = [0]  # 所有可能的分界点
        for i in range(n - 1):
            if s[i] not in '2357' and s[i + 1] in '2357':
                A.append(i)
        A.append(n - 1)
        m = len(A)
        print(A)
        dp = [[0] * m for _ in range(k)]  # dp[i][j] 表示 s[:A[:j+1]]中分i+1段的最大数量
        for i in range(1, m):
            if A[i] + 1 >= minLength:
                dp[0][i] = 1
        for i in range(1, k):
            ss = 0  # 前缀和
            idx = 0  # 前缀和加到了idx项
            for j in range(1, m):
                for t in range(idx, j):
                    if A[j] - A[t] >= minLength:
                        ss += dp[i - 1][t]
                        ss %= MOD
                        idx += 1
                dp[i][j] = ss
        print(dp)
        return dp[-1][-1]

so = Solution()
print(so.beautifulPartitions(s = "22", k = 1, minLength = 1))  # 0
print(so.beautifulPartitions(s = "3312958", k = 3, minLength = 1))  # 1
print(so.beautifulPartitions(s = "23542185131", k = 3, minLength = 2))  # 3
print(so.beautifulPartitions(s = "23542185131", k = 3, minLength = 3))  # 1




