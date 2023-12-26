# 给你一个 m * n 的矩阵 seats 表示教室中的座位分布。如果座位是坏的（不可用），就用 '#' 表示；否则，用 '.' 表示。
#
# 学生可以看到左侧、右侧、左上、右上这四个方向上紧邻他的学生的答卷，但是看不到直接坐在他前面或者后面的学生的答卷。请你计算并返回该考场可以容纳的同时参加考试且无法作弊的 最大 学生人数。
#
# 学生必须坐在状况良好的座位上。
#
#
#
# 示例 1：
#
#
#
# 输入：seats = [["#",".","#","#",".","#"],
#               [".","#","#","#","#","."],
#               ["#",".","#","#",".","#"]]
# 输出：4
# 解释：教师可以让 4 个学生坐在可用的座位上，这样他们就无法在考试中作弊。
# 示例 2：
#
# 输入：seats = [[".","#"],
#               ["#","#"],
#               ["#","."],
#               ["#","#"],
#               [".","#"]]
# 输出：3
# 解释：让所有学生坐在可用的座位上。
# 示例 3：
#
# 输入：seats = [["#",".",".",".","#"],
#               [".","#",".","#","."],
#               [".",".","#",".","."],
#               [".","#",".","#","."],
#               ["#",".",".",".","#"]]
# 输出：10
# 解释：让学生坐在第 1、3 和 5 列的可用座位上。
#
#
# 提示：
#
# seats 只包含字符 '.' 和'#'
# m == seats.length
# n == seats[i].length
# 1 <= m <= 8
# 1 <= n <= 8

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        seats.insert(0, ['.'] * len(seats[0]))
        r, c = len(seats), len(seats[0])
        def check(pos): # 一行考生的展位情况，返回是否互相间隔
            s = bin(pos)[2:]
            return '11' not in s
        @cache
        def dfs(row, bits: int):  # 从第row行的占位情况为bits时，下面行最多的考生数
            if row == r - 1:
                return bits.bit_count()
            possible = (1 << c) - 1  # row+1行，所有可能坐考生的位置
            for i in range(c):
                if (bits >> i) & 1:
                    if i > 0:
                        possible &= ~(1 << (i - 1))
                    if i < c - 1:
                        possible &= ~(1 << (i + 1))
                if seats[row + 1][i] == '#':
                    possible &= ~(1 << i)

            res = dfs(row + 1, 0)  # 本行不选
            sub = possible  # 遍历每个子集
            while sub:
                # 处理 sub 的逻辑
                if check(sub):
                    res = max(res, dfs(row + 1, sub))
                sub = (sub - 1) & possible

            return res + bits.bit_count()
        return dfs(0, 0)




so = Solution()
print(so.maxStudents(seats = [["#",".",".",".","#"],
              [".","#",".","#","."],
              [".",".","#",".","."],
              [".","#",".","#","."],
              ["#",".",".",".","#"]]))
print(so.maxStudents(seats = [[".","#"],
              ["#","#"],
              ["#","."],
              ["#","#"],
              [".","#"]]))
print(so.maxStudents(seats = [["#",".","#","#",".","#"],
              [".","#","#","#","#","."],
              ["#",".","#","#",".","#"]]))




