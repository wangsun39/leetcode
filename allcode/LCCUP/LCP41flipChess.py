# 在 n*m 大小的棋盘中，有黑白两种棋子，黑棋记作字母 "X", 白棋记作字母 "O"，空余位置记作 "."。当落下的棋子与其他相同颜色的棋子在行、列或对角线完全包围（中间不存在空白位置）另一种颜色的棋子，则可以翻转这些棋子的颜色。
#
#
#
# 「力扣挑战赛」黑白翻转棋项目中，将提供给选手一个未形成可翻转棋子的棋盘残局，其状态记作 chessboard。若下一步可放置一枚黑棋，请问选手最多能翻转多少枚白棋。
#
# 注意：
#
# 若翻转白棋成黑棋后，棋盘上仍存在可以翻转的白棋，将可以 继续 翻转白棋
# 输入数据保证初始棋盘状态无可以翻转的棋子且存在空余位置
# 示例 1：
#
# 输入：chessboard = ["....X.","....X.","XOOO..","......","......"]
#
# 输出：3
#
# 解释：
# 可以选择下在 [2,4] 处，能够翻转白方三枚棋子。
#
# 示例 2：
#
# 输入：chessboard = [".X.",".O.","XO."]
#
# 输出：2
#
# 解释：
# 可以选择下在 [2,2] 处，能够翻转白方两枚棋子。
#
#
# 示例 3：
#
# 输入：chessboard = [".......",".......",".......","X......",".O.....","..O....","....OOX"]
#
# 输出：4
#
# 解释：
# 可以选择下在 [6,3] 处，能够翻转白方四枚棋子。
#
#
# 提示：
#
# 1 <= chessboard.length, chessboard[i].length <= 8
# chessboard[i] 仅包含 "."、"O" 和 "X"




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
    def flipChess(self, chessboard: List[str]) -> int:
        dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        def search(x, y, d1, d2, cb):
            cnt = 1
            ans = []
            find = False
            while 0 <= x + d1 * cnt < n and 0 <= y + d2 * cnt < m:
                if cb[x + d1 * cnt][y + d2 * cnt] == 'O':
                    ans.append([x + d1 * cnt, y + d2 * cnt])
                    cnt += 1
                elif cb[x + d1 * cnt][y + d2 * cnt] == 'X':
                    find = True
                    break
                else:
                    break
            return ans if find else []
        def helper(x, y, cb):
            ans = 0
            for dir in dirs:
                xx, yy = x + dir[0], y + dir[1]
                if 0 <= xx < n and 0 <= yy < m and cb[xx][yy] == 'O':
                    white = search(x, y, dir[0], dir[1], cb)
                    for w1, w2 in white:
                        cb[w1] = cb[w1][:w2] + 'X' + cb[w1][w2 + 1:]
                        ans += 1
                    for w1, w2 in white:
                        ans += helper(w1, w2, cb)
            return ans

        ans = 0
        n, m = len(chessboard), len(chessboard[0])
        for i in range(n):
            for j in range(m):
                if chessboard[i][j] == '.':
                    cb = [cc for cc in chessboard]
                    cb[i] = cb[i][:j] + 'X' + cb[i][j + 1:]
                    res = helper(i, j, cb)
                    ans = max(ans, res)
        return ans

    def flipChess1(self, chessboard: List[str]) -> int:
        # 2023/6/21  改进写法
        dir = [[-1, 0], [1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1], [0, -1], [0, 1]]
        r, c = len(chessboard), len(chessboard[0])
        ans = 0
        for i in range(r):
            for j in range(c):
                if chessboard[i][j] != '.': continue
                cnt = 0
                cb = [list(x) for x in chessboard]
                dq = deque([[i, j]])  # 刚变成黑子的位置
                while dq:
                    x, y = dq.popleft()
                    for u, v in dir:
                        xx, yy = x + u, y + v
                        while 0 <= xx < r and 0 <= yy < c and cb[xx][yy] == 'O':
                            xx, yy = xx + u, yy + v
                        if abs(xx - x) == 1 or not (0 <= xx < r and 0 <= yy < c) or cb[xx][yy] == '.':
                            continue
                        xx, yy = xx - u, yy - v
                        while xx != x or yy != y:
                            dq.append([xx, yy])
                            cb[xx][yy] = 'X'
                            xx, yy = xx - u, yy - v
                            cnt += 1

                ans = max(ans, cnt)

        return ans


so = Solution()
print(so.flipChess([".....",".....","X....","OX...","OOOOX","OOO..",".OO..","X..X."]))  # 10
print(so.flipChess([".......",".......",".......","X......",".O.....","..O....","....OOX"]))  # 4
print(so.flipChess(["....X.","....X.","XOOO..","......","......"]))  # 3
print(so.flipChess(chessboard = [".X.",".O.","XO."]))  # 2




