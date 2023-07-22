# 给你一个下标从 0 开始的字符串 word ，字符串只包含小写英文字母。你需要选择 一个 下标并 删除 下标处的字符，使得 word 中剩余每个字母出现 频率 相同。
#
# 如果删除一个字母后，word 中剩余所有字母的出现频率都相同，那么返回 true ，否则返回 false 。
#
# 注意：
#
# 字母 x 的 频率 是这个字母在字符串中出现的次数。
# 你 必须 恰好删除一个字母，不能一个字母都不删除。
#
#
# 示例 1：
#
# 输入：word = "abcc"
# 输出：true
# 解释：选择下标 3 并删除该字母，word 变成 "abc" 且每个字母出现频率都为 1 。
# 示例 2：
#
# 输入：word = "aazz"
# 输出：false
# 解释：我们必须删除一个字母，所以要么 "a" 的频率变为 1 且 "z" 的频率为 2 ，要么两个字母频率反过来。所以不可能让剩余所有字母出现频率相同。
#
#
# 提示：
#
# 2 <= word.length <= 100
# word 只包含小写英文字母。

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

from functools import lru_cache
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

class Solution:
    def equalFrequency(self, word: str) -> bool:
        ct = Counter(word)
        ct2 = Counter(ct.values())
        if len(ct2) > 2: return False
        if len(ct2) == 1: return 1 in ct2.keys() or 1 in ct2.values()
        if ct2[1] == 1: return True
        k = sorted(list(ct2.keys()))
        return k[1] - k[0] == 1 and ( ct2[k[1]] == 1)

    def equalFrequency1(self, word: str) -> bool:
        # 2023/7/8
        counter = Counter(word)
        cc = sorted(list(counter.values()))
        cc[-1] -= 1  # 删除第一个
        if all(x == cc[0] for x in cc):
            return True
        cc[-1] += 1
        if cc[0] == 1 and all(x == cc[1] for x in cc[1:]):  # 删除最后一个
            return True

        return False






so = Solution()
print(so.equalFrequency(word = "acbda"))  # True
print(so.equalFrequency(word = "cbccca"))  # False
print(so.equalFrequency(word = "cccd"))  # True
print(so.equalFrequency(word = "abcc"))  # True
print(so.equalFrequency(word = "zz"))  # True
print(so.equalFrequency(word = "ddaccb"))  # False
print(so.equalFrequency(word = "bac"))  # True
print(so.equalFrequency(word = "aazz"))  # False




