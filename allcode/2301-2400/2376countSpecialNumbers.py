# 如果一个正整数每一个数位都是 互不相同的，我们称它是 特殊整数 。
#
# 给你一个 正整数n，请你返回区间[1, n]之间特殊整数的数目。
#
#
# 
# 示例 1：
#
# 输入：n = 20
# 输出：19
# 解释：1 到 20 之间所有整数除了 11 以外都是特殊整数。所以总共有 19 个特殊整数。
# 示例 2：
#
# 输入：n = 5
# 输出：5
# 解释：1 到 5 所有整数都是特殊整数。
# 示例 3：
#
# 输入：n = 135
# 输出：110
# 解释：从 1 到 135 总共有 110 个整数是特殊整数。
# 不特殊的部分数字为：22 ，114 和 131 。
#
#
# 提示：
#
# 1 <= n <= 2 * 109


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


# 将 nn 转换成字符串 ss，定义 f(i,\textit{mask}, \textit{isLimit},\textit{isNum})f(i,mask,isLimit,isNum) 表示从构造 nn 从高到低第 ii 位及其之后位的方案数，其余参数的含义为：
#
# 要选的数字不能在 \textit{mask}mask 集合中。
# \textit{isLimit}isLimit 表示当前是否受到了 nn 的约束。若为真，则第 ii 位填入的数字至多为 s[i]s[i]，否则可以是 99。
# \textit{isNum}isNum 表示 ii 前面的位数是否填了数字。若为假，则当前位可以跳过（不填数字），或者要填入的数字至少为 11；若为真，则要填入的数字可以从 00 开始。


class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)
        @lru_cache(None)
        def helper(i: int, mask: int, is_limit: bool, is_num: bool) -> int:
            if i == len(s):
                return 1 if is_num else 0
            ans = 0
            if not is_num:
                ans = helper(i + 1, mask, False, False)
            upper = int(s[i]) if is_limit else 9  # 判断当前位是否受约束
            lower = 0 if is_num else 1
            for j in range(lower, upper + 1):
                if (1 << j) & mask == 0:
                    ans += helper(i + 1, mask | (1 << j), is_limit and j == upper, True)
            return ans
        return helper(0, 0, True, False)


so = Solution()
print(so.countSpecialNumbers(5))
print(so.countSpecialNumbers(20))
print(so.countSpecialNumbers(135))




