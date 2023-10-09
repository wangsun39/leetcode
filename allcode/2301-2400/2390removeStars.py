# 给你一个包含若干星号 * 的字符串 s 。
#
# 在一步操作中，你可以：
#
# 选中 s 中的一个星号。
# 移除星号 左侧 最近的那个 非星号 字符，并移除该星号自身。
# 返回移除 所有 星号之后的字符串。
#
# 注意：
#
# 生成的输入保证总是可以执行题面中描述的操作。
# 可以证明结果字符串是唯一的。
#  
#
# 示例 1：
#
# 输入：s = "leet**cod*e"
# 输出："lecoe"
# 解释：从左到右执行移除操作：
# - 距离第 1 个星号最近的字符是 "leet**cod*e" 中的 't' ，s 变为 "lee*cod*e" 。
# - 距离第 2 个星号最近的字符是 "lee*cod*e" 中的 'e' ，s 变为 "lecod*e" 。
# - 距离第 3 个星号最近的字符是 "lecod*e" 中的 'd' ，s 变为 "lecoe" 。
# 不存在其他星号，返回 "lecoe" 。
# 示例 2：
#
# 输入：s = "erase*****"
# 输出：""
# 解释：整个字符串都会被移除，所以返回空字符串。
#  
#
# 提示：
#
# 1 <= s.length <= 105
# s 由小写英文字母和星号 * 组成
# s 可以执行上述操作


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
# heap.heapify(nums)
# heapq.heappop() 函数弹出堆中最小值
# heapq.heappush(nums, 1)
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

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for e in s:
            if e == '*':
                stack.pop()
            else:
                stack.append(e)
        return ''.join(stack)


so = Solution()
print(so.removeStars("leet**cod*e"))
print(so.removeStars("erase*****"))




