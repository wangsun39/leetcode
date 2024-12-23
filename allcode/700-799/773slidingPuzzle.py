# 在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示。一次 移动 定义为选择 0 与一个相邻的数字（上下左右）进行交换.
#
# 最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。
#
# 给出一个谜板的初始状态 board ，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。
#
#
#
# 示例 1：
#
#
#
# 输入：board = [[1,2,3],[4,0,5]]
# 输出：1
# 解释：交换 0 和 5 ，1 步完成
# 示例 2:
#
#
#
# 输入：board = [[1,2,3],[5,4,0]]
# 输出：-1
# 解释：没有办法完成谜板
# 示例 3:
#
#
#
# 输入：board = [[4,1,2],[5,0,3]]
# 输出：5
# 解释：
# 最少完成谜板的最少移动次数是 5 ，
# 一种移动路径:
# 尚未移动: [[4,1,2],[5,0,3]]
# 移动 1 次: [[4,1,2],[0,5,3]]
# 移动 2 次: [[0,1,2],[4,5,3]]
# 移动 3 次: [[1,0,2],[4,5,3]]
# 移动 4 次: [[1,2,0],[4,5,3]]
# 移动 5 次: [[1,2,3],[4,5,0]]
#
#
# 提示：
#
# board.length == 2
# board[i].length == 3
# 0 <= board[i][j] <= 5
# board[i][j] 中每个值都 不同

from leetcode.allcode.competition.mypackage import *

vis = {(1,2,3,4,5,0): 1}
dq1 = deque([(1,2,3,4,5,0)])
lev = 0
while dq1:
    dq2 = deque()
    lev += 1
    while dq1:
        l = list(dq1.popleft())
        p0 = l.index(0)
        if p0 > 0 and p0 != 3:
            l[p0], l[p0 - 1] = l[p0 - 1], l[p0]
            tu = tuple(l)
            if tu not in vis:
                vis[tu] = lev
                dq2.append(tu)
            l[p0], l[p0 - 1] = l[p0 - 1], l[p0]
        if p0 < 5 and p0 != 2:
            l[p0], l[p0 + 1] = l[p0 + 1], l[p0]
            tu = tuple(l)
            if tu not in vis:
                vis[tu] = lev
                dq2.append(tu)
            l[p0], l[p0 + 1] = l[p0 + 1], l[p0]
        if p0 < 3:
            l[p0], l[p0 + 3] = l[p0 + 3], l[p0]
            tu = tuple(l)
            if tu not in vis:
                vis[tu] = lev
                dq2.append(tu)
            l[p0], l[p0 + 3] = l[p0 + 3], l[p0]
        else:
            l[p0], l[p0 - 3] = l[p0 - 3], l[p0]
            tu = tuple(l)
            if tu not in vis:
                vis[tu] = lev
                dq2.append(tu)
            l[p0], l[p0 - 3] = l[p0 - 3], l[p0]
    dq1 = dq2



class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        board = tuple(board[0] + board[1])
        if board in vis:
            return vis[board]
        return -1


so = Solution()
print(so.slidingPuzzle(board = [[3,2,4],[1,5,0]]))
print(so.slidingPuzzle(board = [[4,1,2],[5,0,3]]))
print(so.slidingPuzzle(board = [[1,2,3],[4,0,5]]))

