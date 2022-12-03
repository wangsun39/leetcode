# 给你数字字符串 s ，请你返回 s 中长度为 5 的 回文子序列 数目。由于答案可能很大，请你将答案对 109 + 7 取余 后返回。
#
# 提示：
#
# 如果一个字符串从前往后和从后往前读相同，那么它是 回文字符串 。
# 子序列是一个字符串中删除若干个字符后，不改变字符顺序，剩余字符构成的字符串。
#
#
# 示例 1：
#
# 输入：s = "103301"
# 输出：2
# 解释：
# 总共有 6 长度为 5 的子序列："10330" ，"10331" ，"10301" ，"10301" ，"13301" ，"03301" 。
# 它们中有两个（都是 "10301"）是回文的。
# 示例 2：
#
# 输入：s = "0000000"
# 输出：21
# 解释：所有 21 个长度为 5 的子序列都是 "00000" ，都是回文的。
# 示例 3：
#
# 输入：s = "9999900000"
# 输出：2
# 解释：仅有的两个回文子序列是 "99999" 和 "00000" 。
#
#
# 提示：
#
# 1 <= s.length <= 104
# s 只包含数字字符。
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
    def countPalindromes(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)
        c1, c2 = [[0] * 10 for _ in range(n)], [[0] * 10 for _ in range(n)]  # i 左右(包括i)分别有多少个 0 - 9
        c3, c4 = [[0] * 100 for _ in range(n)], [[0] * 100 for _ in range(n)]  # i 左右(包括i)分别有多少个 00 - 99
        for i in range(n):
            num = int(s[i])
            if i > 0:
                c1[i] = [e for e in c1[i - 1]]
                c3[i] = [e for e in c3[i - 1]]
            c1[i][num] += 1
            if i > 0:
                for j in range(10):
                    idx = j * 10 + num
                    c3[i][idx] += c1[i - 1][j]

        for i in range(n - 1, -1, -1):
            num = int(s[i])
            if i < n - 1:
                c2[i] = [e for e in c2[i + 1]]
                c4[i] = [e for e in c4[i + 1]]
            c2[i][num] += 1
            if i < n - 1:
                for j in range(10):
                    idx = num * 10 + j
                    c4[i][idx] += c2[i + 1][j]
        # print(c1)
        # print(c2)
        # print(c3)
        # print(c4)
        ans = 0
        for i in range(2, n - 2):
            for j in range(100):
                left = c3[i - 1][j]
                right = c4[i + 1][(j%10)*10 + j // 10]
                ans += (left * right)
                ans %= MOD
        return ans

so = Solution()
print(so.countPalindromes("00000"))
print(so.countPalindromes("103301"))
print(so.countPalindromes("0000000"))
print(so.countPalindromes("9999900000"))




