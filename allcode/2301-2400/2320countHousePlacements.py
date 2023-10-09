# 一条街道上共有 n * 2 个 地块 ，街道的两侧各有 n 个地块。每一边的地块都按从 1 到 n 编号。每个地块上都可以放置一所房子。
#
# 现要求街道同一侧不能存在两所房子相邻的情况，请你计算并返回放置房屋的方式数目。由于答案可能很大，需要对 109 + 7 取余后再返回。
#
# 注意，如果一所房子放置在这条街某一侧上的第 i 个地块，不影响在另一侧的第 i 个地块放置房子。
#
#  
#
# 示例 1：
#
# 输入：n = 1
# 输出：4
# 解释：
# 可能的放置方式：
# 1. 所有地块都不放置房子。
# 2. 一所房子放在街道的某一侧。
# 3. 一所房子放在街道的另一侧。
# 4. 放置两所房子，街道两侧各放置一所。
# 示例 2：
#
#
# 输入：n = 2
# 输出：9
# 解释：如上图所示，共有 9 种可能的放置方式。
#  
#
# 提示：
#
# 1 <= n <= 104

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

# bit位 函数：
# n.bit_length()
# value = int(s, 2)

class Solution:
    def countHousePlacements(self, n: int) -> int:
        MAX = int(1e9 + 7)
        arrange = [0] * n
        no_arrange = [0] * n
        arrange[0] = 1
        no_arrange[0] = 1
        for i in range(1, n):
            arrange[i] = no_arrange[i - 1] % MAX
            no_arrange[i] = (arrange[i - 1] + no_arrange[i - 1]) % MAX
        one_side = (arrange[-1] + no_arrange[-1]) % MAX
        ans = (one_side * one_side) % MAX
        return ans



so = Solution()
print(so.countHousePlacements(1))
print(so.countHousePlacements(2))




