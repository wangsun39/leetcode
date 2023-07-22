# 给你一个长度为 n 的 整数 数组 pref 。找出并返回满足下述条件且长度为 n 的数组 arr ：
#
# pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
# 注意 ^ 表示 按位异或（bitwise-xor）运算。
#
# 可以证明答案是 唯一 的。
#
#
#
# 示例 1：
#
# 输入：pref = [5,2,0,3,1]
# 输出：[5,7,2,3,2]
# 解释：从数组 [5,7,2,3,2] 可以得到如下结果：
# - pref[0] = 5
# - pref[1] = 5 ^ 7 = 2
# - pref[2] = 5 ^ 7 ^ 2 = 0
# - pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3
# - pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1
# 示例 2：
#
# 输入：pref = [13]
# 输出：[13]
# 解释：pref[0] = arr[0] = 13
#
#
# 提示：
#
# 1 <= pref.length <= 105
# 0 <= pref[i] <= 106
# https://leetcode.cn/problems/find-the-original-array-of-prefix-xor/

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
    def findArray(self, pref: List[int]) -> List[int]:
        # arr[i] = pref[i] ^ pref[i - 1]
        ans = [pref[0]]
        for i, e in enumerate(pref[1:], 1):
            ans.append(e ^ pref[i - 1])
        return ans



so = Solution()
print(so.findArray([5,2,0,3,1]))
print(so.findArray([13]))




