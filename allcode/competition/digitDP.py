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

from functools import lru_cache, cache
from typing import List


# @lru_cache(None)

# bit位 函数：
# n.bit_length()
# value = int(s, 2)

# 数位DP，https://leetcode.cn/problems/count-special-integers/

# 将 n 转换成字符串 s，定义 f(i,mask,isLimit,isNum) 表示构造从左往右第 i 位及其之后数位的合法方案数，其余参数的含义为：
#
# mask 表示前面选过的数字集合，换句话说，第 i 位要选的数字不能在 mask 中。
# isLimit 表示当前是否受到了 n 的约束。若为真，则第 i 位填入的数字至多为 s[i]，否则可以是 9。如果在受到约束的情况下填了 s[i]，那么后续填入的数字仍会受到 n 的约束。
# isNum 表示 i 前面的数位是否填了数字。若为假，则当前位可以跳过（不填数字），或者要填入的数字至少为 1；若为真，则要填入的数字可以从 0 开始。
# 后面两个参数可适用于其它数位 DP 题目。
#
# 枚举要填入的数字，具体实现逻辑见代码。
#
# 下面代码中 Java/C++/Go 只需要记忆化 (i,mask) 这个状态，因为：
#
# 对于一个固定的 (i,mask)，这个状态受到 isLimit 或 isNum 的约束在整个递归过程中至多会出现一次，没必要记忆化。
# 另外，如果只记忆化 (i,mask)，dp 数组的含义就变成在不受到约束时的合法方案数，所以要在 !isLimit && isNum 成立时才去记忆化。


class Solution:

    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)

        @cache
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

    # 2719
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        # 改造用数位DP的模板
        MOD = 10 ** 9 + 7

        def f(num: str):  # 数字 <= num 满足条件的所有数字
            @cache
            def digitDp(i: int, is_limit: bool, s: int) -> int:
                if s > max_sum: return 0
                if i == len(num):
                    return min_sum <= s <= max_sum
                ans = 0
                upper = int(num[i]) if is_limit else 9  # 判断当前位是否受约束
                for j in range(upper + 1):
                    ans += digitDp(i + 1, is_limit and j == upper, s + j)
                return ans
            return digitDp(0, True, 0)

        num1 = str(int(num1) - 1)
        return (f(num2) + MOD - f(num1)) % MOD


so = Solution()
print(so.removeDigit(123456))