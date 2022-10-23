# 给你一个下标从 0 开始的 m x n 整数矩阵 grid 和一个整数 k 。你从起点 (0, 0) 出发，每一步只能往 下 或者往 右 ，你想要到达终点 (m - 1, n - 1) 。
#
# 请你返回路径和能被 k 整除的路径数目，由于答案可能很大，返回答案对 109 + 7 取余 的结果。
#
#
#
# 示例 1：
#
#
#
# 输入：grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3
# 输出：2
# 解释：有两条路径满足路径上元素的和能被 k 整除。
# 第一条路径为上图中用红色标注的路径，和为 5 + 2 + 4 + 5 + 2 = 18 ，能被 3 整除。
# 第二条路径为上图中用蓝色标注的路径，和为 5 + 3 + 0 + 5 + 2 = 15 ，能被 3 整除。
# 示例 2：
#
#
# 输入：grid = [[0,0]], k = 5
# 输出：1
# 解释：红色标注的路径和为 0 + 0 = 0 ，能被 5 整除。
# 示例 3：
#
#
# 输入：grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]], k = 1
# 输出：10
# 解释：每个数字都能被 1 整除，所以每一条路径的和都能被 k 整除。
#
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 5 * 104
# 1 <= m * n <= 5 * 104
# 0 <= grid[i][j] <= 100
# 1 <= k <= 50
# https://leetcode.cn/problems/paths-in-matrix-whose-sum-is-divisible-by-k/

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
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = int(1e9 + 7)
        row, col = len(grid), len(grid[0])
        dp = [[[0 for _ in range(k)] for _ in range(col)] for _ in range(row)]
        print(dp)
        dp[0][0][grid[0][0] % k] = 1
        for i in range(row):
            for j in range(col):
                for l in range(k):
                    idx = (l + grid[i][j]) % k
                    if i > 0:
                        dp[i][j][idx] += dp[i - 1][j][l]
                        dp[i][j][idx] %= MOD
                    if j > 0:
                        dp[i][j][idx] += dp[i][j - 1][l]
                        dp[i][j][idx] %= MOD
        return dp[-1][-1][0]


so = Solution()
print(so.numberOfPaths(grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3))
print(so.numberOfPaths(grid = [[0,0]], k = 5))
print(so.numberOfPaths(grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]], k = 1))




