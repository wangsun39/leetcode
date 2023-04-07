# 在一个长度 无限 的数轴上，第 i 颗石子的位置为 stones[i]。如果一颗石子的位置最小/最大，那么该石子被称作 端点石子 。
#
# 每个回合，你可以将一颗端点石子拿起并移动到一个未占用的位置，使得该石子不再是一颗端点石子。
#
# 值得注意的是，如果石子像 stones = [1,2,5] 这样，你将 无法 移动位于位置 5 的端点石子，因为无论将它移动到任何位置（例如 0 或 3），该石子都仍然会是端点石子。
#
# 当你无法进行任何移动时，即，这些石子的位置连续时，游戏结束。
#
# 要使游戏结束，你可以执行的最小和最大移动次数分别是多少？ 以长度为 2 的数组形式返回答案：answer = [minimum_moves, maximum_moves] 。
#
#
#
# 示例 1：
#
# 输入：[7,4,9]
# 输出：[1,2]
# 解释：
# 我们可以移动一次，4 -> 8，游戏结束。
# 或者，我们可以移动两次 9 -> 5，4 -> 6，游戏结束。
# 示例 2：
#
# 输入：[6,5,4,3,10]
# 输出：[2,3]
# 解释：
# 我们可以移动 3 -> 8，接着是 10 -> 7，游戏结束。
# 或者，我们可以移动 3 -> 7, 4 -> 8, 5 -> 9，游戏结束。
# 注意，我们无法进行 10 -> 2 这样的移动来结束游戏，因为这是不合要求的移动。
# 示例 3：
#
# 输入：[100,101,104,102,103]
# 输出：[0,0]
#
#
# 提示：
#
# 3 <= stones.length <= 10^4
# 1 <= stones[i] <= 10^9
# stones[i] 的值各不相同。

from typing import List
from functools import cache
from math import *
from bisect import *

class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)
        diff = []  # 记录石头间的空格数
        for i in range(1, n):
            if stones[i] - stones[i - 1] - 1 > 0:
                diff.append(stones[i] - stones[i - 1] - 1)

        if len(diff) == 0: return [0, 0]
        def calc_max():
            if len(diff) == 1:
                return diff[0]
            s = sum(diff)
            return max(s - diff[0], s - diff[-1])

        def calc_min():
            if len(diff) == 1:
                return min(2, diff[0])
            res = inf
            start, end = stones[0], stones[-1]
            for i in range(n):
                pos = bisect_left(stones, stones[i] + n - 1)
                if pos >= n or stones[pos] >= end + 1:
                    break
                if stones[pos] == stones[i] + n - 1:
                    res = min(res, n - (pos - i + 1))
                else:
                    res = min(res, n - (pos - i))
            return res

        return [calc_min(), calc_max()]





obj = Solution()
print(obj.numMovesStonesII([7,4,9]))
print(obj.numMovesStonesII([6,5,4,3,10]))
print(obj.numMovesStonesII([100,101,104,102,103]))

