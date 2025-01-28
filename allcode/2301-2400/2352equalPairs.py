# 给你一个下标从 0 开始、大小为 n x n 的整数矩阵 grid ，返回满足 Ri 行和 Cj 列相等的行列对 (Ri, Cj) 的数目。
#
# 如果行和列以相同的顺序包含相同的元素（即相等的数组），则认为二者是相等的。
#
#
#
# 示例 1：
#
#
#
# 输入：grid = [[3,2,1],[1,7,6],[2,7,7]]
# 输出：1
# 解释：存在一对相等行列对：
# - (第 2 行，第 1 列)：[2,7,7]
# 示例 2：
#
#
#
# 输入：grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# 输出：3
# 解释：存在三对相等行列对：
# - (第 0 行，第 0 列)：[3,1,2,2]
# - (第 2 行, 第 2 列)：[2,4,2,2]
# - (第 3 行, 第 2 列)：[2,4,2,2]
#
#
# 提示：
#
# n == grid.length == grid[i].length
# 1 <= n <= 200
# 1 <= grid[i][j] <= 105

from typing import List
from typing import Optional
from collections import deque
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)
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

# Map = [['U' for _ in range(n)] for _ in range(m)]

from functools import lru_cache
from typing import List
# @lru_cache(None)

# bit位 函数：
# n.bit_length()
# value = int(s, 2)

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def equal(r, c):
            for i in range(n):
                if grid[r][i] != grid[i][c]:
                    return False
            return True
        ans = 0
        for i in range(n):
            for j in range(n):
                if equal(i, j):
                    print(i, j)
                    ans += 1

        return ans


so = Solution()
print(so.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))
print(so.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))




