# 如果一个正方形矩阵满足下述 全部 条件，则称之为一个 X 矩阵 ：
#
# 矩阵对角线上的所有元素都 不是 0
# 矩阵中所有其他元素都是 0
# 给你一个大小为 n x n 的二维整数数组 grid ，表示一个正方形矩阵。如果 grid 是一个 X 矩阵 ，返回 true ；否则，返回 false 。
#
#  
#
# 示例 1：
#
#
# 输入：grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
# 输出：true
# 解释：矩阵如上图所示。
# X 矩阵应该满足：绿色元素（对角线上）都不是 0 ，红色元素都是 0 。
# 因此，grid 是一个 X 矩阵。
# 示例 2：
#
#
# 输入：grid = [[5,7,0],[0,3,1],[0,5,0]]
# 输出：false
# 解释：矩阵如上图所示。
# X 矩阵应该满足：绿色元素（对角线上）都不是 0 ，红色元素都是 0 。
# 因此，grid 不是一个 X 矩阵。
#  
#
# 提示：
#
# n == grid.length == grid[i].length
# 3 <= n <= 100
# 0 <= grid[i][j] <= 105

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
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if i == j or i + j == n - 1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        return True


so = Solution()
print(so.checkXMatrix( [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]))
print(so.checkXMatrix( [[5,7,0],[0,3,1],[0,5,0]]))




