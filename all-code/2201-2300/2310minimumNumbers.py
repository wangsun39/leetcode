# 给你两个整数 num 和 k ，考虑具有以下属性的正整数多重集：
#
# 每个整数个位数字都是 k 。
# 所有整数之和是 num 。
# 返回该多重集的最小大小，如果不存在这样的多重集，返回 -1 。
#
# 注意：
#
# 多重集与集合类似，但多重集可以包含多个同一整数，空多重集的和为 0 。
# 个位数字 是数字最右边的数位。
#  
#
# 示例 1：
#
# 输入：num = 58, k = 9
# 输出：2
# 解释：
# 多重集 [9,49] 满足题目条件，和为 58 且每个整数的个位数字是 9 。
# 另一个满足条件的多重集是 [19,39] 。
# 可以证明 2 是满足题目条件的多重集的最小长度。
# 示例 2：
#
# 输入：num = 37, k = 2
# 输出：-1
# 解释：个位数字为 2 的整数无法相加得到 37 。
# 示例 3：
#
# 输入：num = 0, k = 7
# 输出：0
# 解释：空多重集的和为 0 。
#  
#
# 提示：
#
# 0 <= num <= 3000
# 0 <= k <= 9


from typing import List
from collections import deque
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)
#import random
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

# Map = [['U' for _ in range(n)] for _ in range(m)]

from functools import lru_cache
from typing import List
# @lru_cache(None)

class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        candidate = []
        cur = k if k > 0 else 10
        while cur <= num:
            candidate.append(cur)
            cur += 10

        # ans = -1
        @lru_cache(None)
        def dfs(target):
            # n = len(candidate)
            res = 9999999999
            for e in candidate:
                if target < e:
                    break
                if target == e:
                    return 1
                x = dfs(target - e)
                if x != -1:
                    res = min(res, x + 1)
            return -1 if res == 9999999999 else res
        ans = dfs(num)
        return ans


so = Solution()
print(so.minimumNumbers(num = 3000, k = 0))
print(so.minimumNumbers(num = 4, k = 0))
print(so.minimumNumbers(num = 58, k = 9))
print(so.minimumNumbers(num = 37, k = 2))
print(so.minimumNumbers(num = 0, k = 7))




