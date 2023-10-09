# 小力正在通过残局练习来备战「力扣挑战赛」中的「五子棋」项目，他想请你能帮他预测当前残局的输赢情况。棋盘中的棋子分布信息记录于二维数组 pieces 中，其中 pieces[i] = [x,y,color] 表示第 i 枚棋子的横坐标为 x，纵坐标为 y，棋子颜色为 color(0 表示黑棋，1 表示白棋)。假如黑棋先行，并且黑棋和白棋都按最优策略落子，请你求出当前棋局在三步（按 黑、白、黑 的落子顺序）之内的输赢情况（三步之内先构成同行、列或对角线连续同颜色的至少 5 颗即为获胜）：
#
# 黑棋胜, 请返回 "Black"
# 白棋胜, 请返回 "White"
# 仍无胜者, 请返回 "None"
# 注意：
#
# 和传统的五子棋项目不同，「力扣挑战赛」中的「五子棋」项目 不存在边界限制，即可在 任意位置 落子；
# 黑棋和白棋均按 3 步内的输赢情况进行最优策略的选择
# 测试数据保证所给棋局目前无胜者；
# 测试数据保证不会存在坐标一样的棋子。
# 示例 1：
#
# 输入：
# pieces = [[0,0,1],[1,1,1],[2,2,0]]
#
# 输出："None"
#
# 解释：无论黑、白棋以何种方式落子，三步以内都不会产生胜者。
#
# 示例 2：
#
# 输入：
# pieces = [[1,2,1],[1,4,1],[1,5,1],[2,1,0],[2,3,0],[2,4,0],[3,2,1],[3,4,0],[4,2,1],[5,2,1]]
#
# 输出："Black"
#
# 解释：三步之内黑棋必胜，以下是一种可能的落子情况：
#
#
# 提示：
#
# 0 <= pieces.length <= 1000
# pieces[i].length = 3
# -10^9 <= pieces[i][0], pieces[i][1] <=10^9
# 0 <= pieces[i][2] <=1
#
# https://leetcode.cn/problems/fsa7oZ




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

from functools import lru_cache, cache
from typing import List
# @lru_cache(None)

class Solution:
    def gobang(self, pieces: List[List[int]]) -> str:
        f1, f2 = set(), set()
        pieces.sort()
        for p in pieces:
            if p[2] == 0:
                f1.add((p[0], p[1]))
            else:
                f2.add((p[0], p[1]))
        dir = [[1, 0], [0, 1], [-1, 1], [1, 1]]
        def find(ff1, ff2):  # 返回ff1方下一步致胜点，>= 1只返回两点
            s1 = set()
            for x, y in ff1:
                for d1, d2 in dir:
                    if (x + d1, y + d2) in ff1 and (x + d1 * 2, y + d2 * 2) in ff1 and (x + d1 * 3, y + d2 * 3) in ff1:
                        if (x - d1, y - d2) not in ff2:
                            s1.add((x - d1, y - d2))
                        if (x + d1 * 4, y + d2 * 4) not in ff2:
                            s1.add((x + d1 * 4, y + d2 * 4))
                    if (x + d1 * 2, y + d2 * 2) in ff1 and (x + d1 * 3, y + d2 * 3) in ff1 and (x + d1 * 4, y + d2 * 4) in ff1:
                        if (x + d1, y + d2) not in ff2:
                            s1.add((x + d1, y + d2))
                    if (x + d1, y + d2) in ff1 and (x + d1 * 3, y + d2 * 3) in ff1 and (x + d1 * 4, y + d2 * 4) in ff1:
                        if (x + d1 * 2, y + d2 * 2) not in ff2:
                            s1.add((x + d1 * 2, y + d2 * 2))
                    if (x + d1, y + d2) in ff1 and (x + d1 * 2, y + d2 * 2) in ff1 and (x + d1 * 4, y + d2 * 4) in ff1:
                        if (x + d1 * 3, y + d2 * 3) not in ff2:
                            s1.add((x + d1 * 3, y + d2 * 3))
                if len(s1) > 1:
                    return s1  # ff1方获胜
            return s1

        black = find(f1, f2)
        if len(black) >= 1:
            return 'Black'
        white = find(f2, f1)
        if len(white) > 1:
            return 'White'
        if len(white) == 1:
            f1.add(list(white)[0])
            black = find(f1, f2)
            if len(black) > 1:
                return 'Black'
            return 'None'
        s1 = set()
        for x, y in f1:
            dir2 = [[0, 1], [0, -1], [-1, 0], [-1, 1], [-1, -1], [1, -1], [1, 0], [1, 1],
                    [0, 2], [0, -2], [-2, 0], [-2, 2], [-2, -2], [2, -2], [2, 0], [2, 2]]
            for d in dir2:
                x1, y1 = x + d[0], y + d[1]
                if (x1, y1) in s1:
                    continue
                if (x1, y1) not in f1 and (x1, y1) not in f2:
                    f1.add((x1, y1))
                    if len(find(f1, f2)) > 1:
                        return 'Black'
                    f1.remove((x1, y1))
                    s1.add((x1, y1))
        return 'None'

so = Solution()
print(so.gobang( [[0,0,1],[0,1,0],[0,2,0],[0,3,0],[0,7,0],[0,8,0],[0,9,0],[0,10,1]]))  # Black
print(so.gobang( [[0,-2,1],[0,0,0],[0,1,0],[0,2,0],[0,4,1],[1,4,0],[2,4,0],[4,4,0]]))  # None
print(so.gobang( [[0,0,0],[0,6,0],[1,1,0],[1,5,0],[3,0,1],[3,1,1],[3,2,1],[3,4,1],[4,2,0],[4,4,0]]))  # Black
print(so.gobang( [[0,0,1],[1,1,1],[2,2,0]]))  # None
print(so.gobang( [[1,2,1],[1,4,1],[1,5,1],[2,1,0],[2,3,0],[2,4,0],[3,2,1],[3,4,0],[4,2,1],[5,2,1]]))  # Black

