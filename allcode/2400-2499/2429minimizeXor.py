# 给你两个正整数 num1 和 num2 ，找出满足下述条件的整数 x ：
#
# x 的置位数和 num2 相同，且
# x XOR num1 的值 最小
# 注意 XOR 是按位异或运算。
#
# 返回整数 x 。题目保证，对于生成的测试用例， x 是 唯一确定 的。
#
# 整数的 置位数 是其二进制表示中 1 的数目。
#
#  
#
# 示例 1：
#
# 输入：num1 = 3, num2 = 5
# 输出：3
# 解释：
# num1 和 num2 的二进制表示分别是 0011 和 0101 。
# 整数 3 的置位数与 num2 相同，且 3 XOR 3 = 0 是最小的。
# 示例 2：
#
# 输入：num1 = 1, num2 = 12
# 输出：3
# 解释：
# num1 和 num2 的二进制表示分别是 0001 和 1100 。
# 整数 3 的置位数与 num2 相同，且 3 XOR 1 = 2 是最小的。
#  
#
# 提示：
#
# 1 <= num1, num2 <= 109
#
# https://leetcode.cn/problems/minimize-xor

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
    def minimizeXor(self, num1: int, num2: int) -> int:
        def count(x):
            res = 0
            while x:
                x &= (x - 1)
                res += 1
            return res
        count1, count2 = count(num1), count(num2)
        # l1, l2 = num1.bit_count(), num2.bit_count()
        s1 = bin(num1)[2:]
        s2 = ''
        if count1 >= count2:
            cnt = 0
            for s in s1:
                if cnt >= count2:
                    s2 += ('0' * (len(s1) - len(s2)))
                    break
                if s == '1':
                    s2 += '1'
                    cnt += 1
                else:
                    s2 += '0'
        elif count2 >= len(s1):
            return int('1' * count2, 2)
        else:
            cnt = 0
            for s in s1:
                if cnt >= count1:
                    delta = min(count2 - count1, len(s1) - len(s2))
                    s2 = s2 + ('0' * (len(s1) - len(s2) - delta)) + ('1' * delta)
                    break
                if s == '1':
                    s2 += '1'
                    cnt += 1
                else:
                    s2 += '0'
            if s2.count('1') < count2:
                delta = count2 - s2.count('1')
                while delta > 0:
                    pos = s2.rfind('0')
                    s2 = s2[:pos] + '1' + s2[pos + 1:]
                    delta -= 1
        print(s2)

        return int(s2, 2)



so = Solution()
print(so.minimizeXor(num1 = 3756, num2 = 7038))
print(so.minimizeXor(num1 = 65, num2 = 84))
print(so.minimizeXor(num1 = 1, num2 = 12))
print(so.minimizeXor(num1 = 3, num2 = 5))
print(so.minimizeXor(num1 = 8, num2 = 3))




