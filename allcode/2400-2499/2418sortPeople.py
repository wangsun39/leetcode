# 给你一个字符串数组 names ，和一个由 互不相同 的正整数组成的数组 heights 。两个数组的长度均为 n 。
#
# 对于每个下标 i，names[i] 和 heights[i] 表示第 i 个人的名字和身高。
#
# 请按身高 降序 顺序返回对应的名字数组 names 。
#
#
#
# 示例 1：
#
# 输入：names = ["Mary","John","Emma"], heights = [180,165,170]
# 输出：["Mary","Emma","John"]
# 解释：Mary 最高，接着是 Emma 和 John 。
# 示例 2：
#
# 输入：names = ["Alice","Bob","Bob"], heights = [155,185,150]
# 输出：["Bob","Alice","Bob"]
# 解释：第一个 Bob 最高，然后是 Alice 和第二个 Bob 。
#
#
# 提示：
#
# n == names.length == heights.length
# 1 <= n <= 103
# 1 <= names[i].length <= 20
# 1 <= heights[i] <= 105
# names[i] 由大小写英文字母组成
# heights 中的所有值互不相同
#
# https://leetcode.cn/problems/sort-the-people

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
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # arr = zip(names, heights)
        arr = []
        n = len(names)
        for i in range(n):
            arr.append([heights[i], names[i]])
        # print(arr)
        arr.sort(reverse= True)
        ans = [x[1] for x in arr]
        return ans


so = Solution()
print(so.sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170]))
print(so.sortPeople(names = ["Alice","Bob","Bob"], heights = [155,185,150]))




