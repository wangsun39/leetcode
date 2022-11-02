# 给你一个字符串 s 和一个机器人，机器人当前有一个空字符串 t 。执行以下操作之一，直到 s 和 t 都变成空字符串：
#
# 删除字符串 s 的 第一个 字符，并将该字符给机器人。机器人把这个字符添加到 t 的尾部。
# 删除字符串 t 的 最后一个 字符，并将该字符给机器人。机器人将该字符写到纸上。
# 请你返回纸上能写出的字典序最小的字符串。
#
#
#
# 示例 1：
#
# 输入：s = "zza"
# 输出："azz"
# 解释：用 p 表示写出来的字符串。
# 一开始，p="" ，s="zza" ，t="" 。
# 执行第一个操作三次，得到 p="" ，s="" ，t="zza" 。
# 执行第二个操作三次，得到 p="azz" ，s="" ，t="" 。
# 示例 2：
#
# 输入：s = "bac"
# 输出："abc"
# 解释：用 p 表示写出来的字符串。
# 执行第一个操作两次，得到 p="" ，s="c" ，t="ba" 。
# 执行第二个操作两次，得到 p="ab" ，s="c" ，t="" 。
# 执行第一个操作，得到 p="ab" ，s="" ，t="c" 。
# 执行第二个操作，得到 p="abc" ，s="" ，t="" 。
# 示例 3：
#
# 输入：s = "bdda"
# 输出："addb"
# 解释：用 p 表示写出来的字符串。
# 一开始，p="" ，s="bdda" ，t="" 。
# 执行第一个操作四次，得到 p="" ，s="" ，t="bdda" 。
# 执行第二个操作四次，得到 p="addb" ，s="" ，t="" 。
#
#
# 提示：
#
# 1 <= s.length <= 105
# s 只包含小写英文字母。
# https://leetcode.cn/problems/using-a-robot-to-print-the-lexicographically-smallest-string/

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
# string.lowercase：包含所有小写字母的字符串
# string.printable：包含所有可打印字符的字符串
# string.punctuation：包含所有标点的字符串
# string.uppercase：包含所有大写字母的字符串

# f-string用法
# name = 'sun'
# f"Hello, my name is {name}"

class Solution:
    def robotWithString(self, s: str) -> str:
        counter = Counter(s)




so = Solution()
print(so.robotWithString("bydizfve"))  # "bdevfziy"
print(so.robotWithString("zza"))
print(so.robotWithString("bac"))
print(so.robotWithString("bdda"))




