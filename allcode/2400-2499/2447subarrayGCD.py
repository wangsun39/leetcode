# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 nums 的子数组中元素的最大公因数等于 k 的子数组数目。
#
# 子数组 是数组中一个连续的非空序列。
#
# 数组的最大公因数 是能整除数组中所有元素的最大整数。
#
#
#
# 示例 1：
#
# 输入：nums = [9,3,1,2,6,3], k = 3
# 输出：4
# 解释：nums 的子数组中，以 3 作为最大公因数的子数组如下：
# - [9,3,1,2,6,3]
# - [9,3,1,2,6,3]
# - [9,3,1,2,6,3]
# - [9,3,1,2,6,3]
# 示例 2：
#
# 输入：nums = [4], k = 7
# 输出：0
# 解释：不存在以 7 作为最大公因数的子数组。
#
#
# 提示：
#
# 1 <= nums.length <= 1000
# 1 <= nums[i], k <= 109
# https://leetcode.cn/problems/number-of-subarrays-with-gcd-equal-to-k/

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
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        nums1 = [e // k for e in nums]
        nums2 = [e % k for e in nums]
        n = len(nums1)
        cur = 0
        ans = 0
        def GCD(start, end):
            x = nums1[start]
            for i in range(start, end + 1):
                x = math.gcd(x, nums1[i])
                if x == 1:
                    return 1
            return x
        print(nums1)
        print(nums2)
        for i in range(n):
            if nums2[i] != 0:
                cur = i + 1
                continue
            for j in range(cur, i + 1):
                if GCD(j, i) == 1:
                    ans += 1
        return ans



so = Solution()
print(so.subarrayGCD([3,12,9,6], 3))
print(so.subarrayGCD(nums = [9,3,1,2,6,3], k = 3))
print(so.subarrayGCD(nums = [4], k = 7))




