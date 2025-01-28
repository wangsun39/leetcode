# 给你下标从 0 开始、长度为 n的字符串pattern，它包含两种字符，'I'表示 上升，'D'表示 下降。
#
# 你需要构造一个下标从 0开始长度为n + 1的字符串，且它要满足以下条件：
#
# num包含数字'1'到'9'，其中每个数字至多使用一次。
# 如果pattern[i] == 'I'，那么num[i] < num[i + 1]。
# 如果pattern[i] == 'D'，那么num[i] > num[i + 1]。
# 请你返回满足上述条件字典序 最小的字符串num。
#
#
#
# 示例 1：
#
# 输入：pattern = "IIIDIDDD"
# 输出："123549876"
# 解释：
# 下标 0 ，1 ，2 和 4 处，我们需要使 num[i] < num[i+1] 。
# 下标 3 ，5 ，6 和 7 处，我们需要使 num[i] > num[i+1] 。
# 一些可能的 num 的值为 "245639871" ，"135749862" 和 "123849765" 。
# "123549876" 是满足条件最小的数字。
# 注意，"123414321" 不是可行解因为数字 '1' 使用次数超过 1 次。
# 示例 2：
#
# 输入：pattern = "DDD"
# 输出："4321"
# 解释：
# 一些可能的 num 的值为 "9876" ，"7321" 和 "8742" 。
# "4321" 是满足条件最小的数字。
#
#
# 提示：
#
# 1 <= pattern.length <= 8
# pattern只包含字符'I' 和'D' 。


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
    def smallestNumber(self, pattern: str) -> str:
        def helper(pattern):
            if pattern == 'I':
                return '12'
            if pattern == 'D':
                return '21'
            n = len(pattern)
            pos = pattern.rfind('I')
            ans = ''
            if pos == -1:
                for i in range(n + 1, 0, -1):
                    ans += str(i)
                return ans
            sub2 = ''
            i = n + 1
            count = 0
            # for i in range(n + 1, n - pos + 1, -1):
            while count < n - pos:
                sub2 += str(i)
                count += 1
                i -= 1
            sub1 = helper(pattern[:pos])
            return sub1 + sub2
        return helper(pattern)



so = Solution()
print(so.smallestNumber("IIIDDD"))
print(so.smallestNumber("IIIDIDDD"))
print(so.smallestNumber("DDD"))




