# 给你一个字符串数组 board 表示井字游戏的棋盘。当且仅当在井字游戏过程中，棋盘有可能达到 board 所显示的状态时，才返回 true 。
#
# 井字游戏的棋盘是一个 3 x 3 数组，由字符 ' '，'X' 和 'O' 组成。字符 ' ' 代表一个空位。
#
# 以下是井字游戏的规则：
#
# 玩家轮流将字符放入空位（' '）中。
# 玩家 1 总是放字符 'X' ，而玩家 2 总是放字符 'O' 。
# 'X' 和 'O' 只允许放置在空位中，不允许对已放有字符的位置进行填充。
# 当有 3 个相同（且非空）的字符填充任何行、列或对角线时，游戏结束。
# 当所有位置非空时，也算为游戏结束。
# 如果游戏结束，玩家不允许再放置字符。
#
#
# 示例 1：
#
#
# 输入：board = ["O  ","   ","   "]
# 输出：false
# 解释：玩家 1 总是放字符 "X" 。
# 示例 2：
#
#
# 输入：board = ["XOX"," X ","   "]
# 输出：false
# 解释：玩家应该轮流放字符。
# 示例 3:
#
#
# 输入：board = ["XOX","O O","XOX"]
# 输出：true
#
#
# 提示：
#
# board.length == 3
# board[i].length == 3
# board[i][j] 为 'X'、'O' 或 ' '

from typing import List


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        c0 = c1 = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'O':
                    c0 += 1
                elif board[i][j] == 'X':
                    c1 += 1
        if not 0 <= c1 - c0 <= 1: return False
        def triple(ch):
            flg = 0
            if ch * 3 in board:
                flg = 1
            else:
                for i in range(3):
                    if board[0][i] == board[1][i] == board[2][i] == ch:
                        flg = 1
                if board[0][0] == board[1][1] == board[2][2] == ch or \
                        board[0][2] == board[1][1] == board[2][0] == ch:
                    flg = 1
            return flg
        if triple('O') and c1 > c0: return False
        if triple('X') and c1 == c0: return False
        return True


so = Solution()
print(so.validTicTacToe(board=["XO ","XO ","XO "]))
print(so.validTicTacToe(board=["O  ", "   ", "   "]))
