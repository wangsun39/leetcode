# 给你一个 m x n 的字符矩阵 boxGrid ，它表示一个箱子的侧视图。箱子的每一个格子可能为：
#
# '#' 表示石头
# '*' 表示固定的障碍物
# '.' 表示空位置
# 这个箱子被 顺时针旋转 90 度 ，由于重力原因，部分石头的位置会发生改变。每个石头会垂直掉落，直到它遇到障碍物，另一个石头或者箱子的底部。重力 不会 影响障碍物的位置，同时箱子旋转不会产生惯性 ，也就是说石头的水平位置不会发生改变。
#
# 题目保证初始时 boxGrid 中的石头要么在一个障碍物上，要么在另一个石头上，要么在箱子的底部。
#
# 请你返回一个 n x m 的矩阵，表示按照上述旋转后，箱子内的结果。
#
#
#
# 示例 1：
#
#
#
# 输入：box = [["#",".","#"]]
# 输出：[["."],
#       ["#"],
#       ["#"]]
# 示例 2：
#
#
#
# 输入：box = [["#",".","*","."],
#             ["#","#","*","."]]
# 输出：[["#","."],
#       ["#","#"],
#       ["*","*"],
#       [".","."]]
# 示例 3：
#
#
#
# 输入：box = [["#","#","*",".","*","."],
#             ["#","#","#","*",".","."],
#             ["#","#","#",".","#","."]]
# 输出：[[".","#","#"],
#       [".","#","#"],
#       ["#","#","*"],
#       ["#","*","."],
#       ["#",".","*"],
#       ["#",".","."]]
#
#
# 提示：
#
# m == boxGrid.length
# n == boxGrid[i].length
# 1 <= m, n <= 500
# boxGrid[i][j] 只可能是 '#' ，'*' 或者 '.' 。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        r, c = len(boxGrid), len(boxGrid[0])
        for i in range(r):
            k = c - 1
            for j in range(c - 1, -1, -1):
                if boxGrid[i][j] == '#':
                    boxGrid[i][k], boxGrid[i][j] = boxGrid[i][j], boxGrid[i][k]
                    k -= 1
                elif boxGrid[i][j] == '*':
                    k = j - 1

        ans = list(zip(*boxGrid[::-1]))
        ans = [list(x) for x in ans]
        return ans



so = Solution()

print(so.rotateTheBox([["#",".","#"]]))





