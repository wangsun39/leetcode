# 给你一个长度为 n 的整数数组 nums 。
#
# 考虑 nums 中进行 按位与（bitwise AND）运算得到的值 最大 的 非空 子数组。
#
# 换句话说，令 k 是 nums 任意 子数组执行按位与运算所能得到的最大值。那么，只需要考虑那些执行一次按位与运算后等于 k 的子数组。
# 返回满足要求的 最长 子数组的长度。
#
# 数组的按位与就是对数组中的所有数字进行按位与运算。
#
# 子数组 是数组中的一个连续元素序列。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3,3,2,2]
# 输出：2
# 解释：
# 子数组按位与运算的最大值是 3 。
# 能得到此结果的最长子数组是 [3,3]，所以返回 2 。
# 示例 2：
#
# 输入：nums = [1,2,3,4]
# 输出：1
# 解释：
# 子数组按位与运算的最大值是 4 。
# 能得到此结果的最长子数组是 [4]，所以返回 1 。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 106
#
# https://leetcode.cn/problems/longest-subarray-with-maximum-bitwise-and

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
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        m = max(nums)
        ans = 1
        cur = 0
        for i in range(n):
            if nums[i] == m:
                cur += 1
                ans = max(ans, cur)
            else:
                cur = 0
        return ans



so = Solution()
print(so.longestSubarray([1,2,3,3,2,2]))
print(so.longestSubarray([1,2,3,4]))




