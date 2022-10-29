# 给你两个正整数数组 nums 和 target ，两个数组长度相等。
#
# 在一次操作中，你可以选择两个 不同 的下标 i 和 j ，其中 0 <= i, j < nums.length ，并且：
#
# 令 nums[i] = nums[i] + 2 且
# 令 nums[j] = nums[j] - 2 。
# 如果两个数组中每个元素出现的频率相等，我们称两个数组是 相似 的。
#
# 请你返回将 nums 变得与 target 相似的最少操作次数。测试数据保证 nums 一定能变得与 target 相似。
#
#
#
# 示例 1：
#
# 输入：nums = [8,12,6], target = [2,14,10]
# 输出：2
# 解释：可以用两步操作将 nums 变得与 target 相似：
# - 选择 i = 0 和 j = 2 ，nums = [10,12,4] 。
# - 选择 i = 1 和 j = 2 ，nums = [10,14,2] 。
# 2 次操作是最少需要的操作次数。
# 示例 2：
#
# 输入：nums = [1,2,5], target = [4,1,3]
# 输出：1
# 解释：一步操作可以使 nums 变得与 target 相似：
# - 选择 i = 1 和 j = 2 ，nums = [1,4,3] 。
# 示例 3：
#
# 输入：nums = [1,1,1,1,1], target = [1,1,1,1,1]
# 输出：0
# 解释：数组 nums 已经与 target 相似。
#
#
# 提示：
#
# n == nums.length == target.length
# 1 <= n <= 105
# 1 <= nums[i], target[i] <= 106
# nums 一定可以变得与 target 相似。
# https://leetcode.cn/problems/minimum-number-of-operations-to-make-arrays-similar/

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
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        n = len(nums)
        def proc(l):
            for i in range(n):
                if l[i] % 2: l[i] = -l[i]
            l.sort()
        proc(nums)
        proc(target)
        print(nums, target)
        return sum(abs(nums[i] - target[i]) for i in range(n)) // 4

so = Solution()
print(so.makeSimilar(nums = [8,12,6], target = [2,14,10]))
print(so.makeSimilar(nums = [1,2,5], target = [4,1,3]))




