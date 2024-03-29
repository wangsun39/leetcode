# 给你一个由正整数组成的数组nums 。
#
# 你必须取出数组中的每个整数，反转其中每个数位，并将反转后得到的数字添加到数组的末尾。这一操作只针对nums中原有的整数执行。
#
# 返回结果数组中
# 不同
# 整数的数目。
#
#
#
# 示例1：
#
# 输入：nums = [1, 13, 10, 12, 31]
# 输出：6
# 解释：反转每个数字后，结果数组是[1, 13, 10, 12, 31, 1, 31, 1, 21, 13] 。
# 反转后得到的数字添加到数组的末尾并按斜体加粗表示。注意对于整数10 ，反转之后会变成01 ，即1 。
# 数组中不同整数的数目为6（数字1、10、12、13、21和31）。
# 示例2：
#
# 输入：nums = [2, 2, 2]
# 输出：1
# 解释：反转每个数字后，结果数组是[2, 2, 2, 2, 2, 2] 。数组中不同整数的数目为1（数字2）。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 106

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
    def countDistinctIntegers(self, nums: List[int]) -> int:
        s2 = set()
        for x in nums:
            s2.add(int(str(x)[::-1]))
        return len(set(nums) | s2)


so = Solution()
print(so.countDistinctIntegers([1,13,10,12,31]))
print(so.countDistinctIntegers([2,2,2]))




