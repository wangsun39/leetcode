# 给你一个仅由数字（0 - 9）组成的字符串 num 。
#
# 请你找出能够使用 num 中数字形成的 最大回文 整数，并以字符串形式返回。该整数不含 前导零 。
#
# 注意：
#
# 你 无需 使用 num 中的所有数字，但你必须使用 至少 一个数字。
# 数字可以重新排序。
#
#
# 示例 1：
#
# 输入：num = "444947137"
# 输出："7449447"
# 解释：
# 从 "444947137" 中选用数字 "4449477"，可以形成回文整数 "7449447" 。
# 可以证明 "7449447" 是能够形成的最大回文整数。
# 示例 2：
#
# 输入：num = "00009"
# 输出："9"
# 解释：
# 可以证明 "9" 能够形成的最大回文整数。
# 注意返回的整数不应含前导零。
#
#
# 提示：
#
# 1 <= num.length <= 105
# num 由数字（0 - 9）组成


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

class Solution:
    def largestPalindromic(self, num: str) -> str:
        counter = Counter(num)
        s = []
        single = -1
        for x in counter:
            if counter[x] % 2 == 0:
                s.append([x, counter[x]])
            else:
                if counter[x] > 1:
                    s.append([x, counter[x] - 1])
                if int(x) > single:
                    single = int(x)
        s.sort(reverse=True)
        if len(s) and s[0][0] == '0':
            if single != -1:
                return str(single)
            else:
                return '0'
        ans = ''
        for e in s:
            ans += (e[0] * (e[1] // 2))
        ans1 = ans[::-1]
        if single != -1:
            ans += str(single)
        return ans + ans1




so = Solution()
print(so.largestPalindromic("0"))
print(so.largestPalindromic("00"))
print(so.largestPalindromic("000"))
print(so.largestPalindromic("9"))
print(so.largestPalindromic("09"))
print(so.largestPalindromic("00009"))
print(so.largestPalindromic("444947137"))




