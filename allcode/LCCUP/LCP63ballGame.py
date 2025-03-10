# 欢迎各位来到「力扣嘉年华」，接下来将为各位介绍在活动中广受好评的弹珠游戏。
#
# N*M 大小的弹珠盘的初始状态信息记录于一维字符串型数组 plate 中，数组中的每个元素为仅由 "O"、"W"、"E"、"." 组成的字符串。其中：
#
# "O" 表示弹珠洞（弹珠到达后会落入洞中，并停止前进）；
# "W" 表示逆时针转向器（弹珠经过时方向将逆时针旋转 90 度）；
# "E" 表示顺时针转向器（弹珠经过时方向将顺时针旋转 90 度）；
# "." 表示空白区域（弹珠可通行）。
# 游戏规则要求仅能在边缘位置的 空白区域 处（弹珠盘的四角除外）沿 与边缘垂直 的方向打入弹珠，并且打入后的每颗弹珠最多能 前进 num 步。请返回符合上述要求且可以使弹珠最终入洞的所有打入位置。你可以 按任意顺序 返回答案。
#
# 注意：
#
# 若弹珠已到达弹珠盘边缘并且仍沿着出界方向继续前进，则将直接出界。
# 示例 1：
#
# 输入：
# num = 4
# plate = ["..E.",".EOW","..W."]
#
# 输出：[[2,1]]
#
# 解释：
# 在 [2,1] 处打入弹珠，弹珠前进 1 步后遇到转向器，前进方向顺时针旋转 90 度，再前进 1 步进入洞中。
#
#
# 示例 2：
#
# 输入：
# num = 5
# plate = [".....","..E..",".WO..","....."]
#
# 输出：[[0,1],[1,0],[2,4],[3,2]]
#
# 解释：
# 在 [0,1] 处打入弹珠，弹珠前进 2 步，遇到转向器后前进方向逆时针旋转 90 度，再前进 1 步进入洞中。
# 在 [1,0] 处打入弹珠，弹珠前进 2 步，遇到转向器后前进方向顺时针旋转 90 度，再前进 1 步进入洞中。
# 在 [2,4] 处打入弹珠，弹珠前进 2 步后进入洞中。
# 在 [3,2] 处打入弹珠，弹珠前进 1 步后进入洞中。
#
#
# 示例 3：
#
# 输入：
# num = 3
# plate = [".....","....O","....O","....."]
#
# 输出：[]
#
# 解释：
# 由于弹珠被击中后只能前进 3 步，且不能在弹珠洞和弹珠盘四角打入弹珠，故不存在能让弹珠入洞的打入位置。
#
# 提示：
#
# 1 <= num <= 10^6
# 1 <= plate.length, plate[i].length <= 1000
# plate[i][j] 仅包含 "O"、"W"、"E"、"."
#
# https://leetcode.cn/problems/EXvqDp
from leetcode.allcode.competition.mypackage import *

class Solution:
    def ballGame(self, num: int, plate: List[str]) -> List[List[int]]:
        row, col = len(plate), len(plate[0])
        target = set()
        for i in range(row):
            for j in range(col):
                if plate[i][j] == 'O':
                    target.add((i, j))
        def change(pre, cur):
            if cur == '.' or cur == 'O':
                return pre
            if pre == 'U':
                return 'R' if cur == 'E' else 'L'
            if pre == 'L':
                return 'U' if cur == 'E' else 'D'
            if pre == 'D':
                return 'L' if cur == 'E' else 'R'
            if pre == 'R':
                return 'D' if cur == 'E' else 'U'
        ans = []
        ok, nak = {}, {}
        @lru_cache(None)
        def dfs(x, y, dir, step):
            # if x == t1 and y == t2:
            if (x, y) in target and step != num:
                return True
            if step == 0:
                return False
            if (x, y, dir) in ok and step >= ok[(x, y, dir)]:
                return True
            if (x, y, dir) in nak and step <= nak[(x, y, dir)]:
                return False
            next = change(dir, plate[x][y]) if step != num else dir
            xx, yy = x + dirs[next][0], y + dirs[next][1]
            if 0 <= xx < row and 0 <= yy < col:
                res = dfs(xx, yy, next, step - 1)
                if res:
                    ok[(x, y, dir)] = min(ok[(x, y, dir)], step) if (x, y, dir) in ok else step
                    return True
                else:
                    nak[(x, y, dir)] = max(nak[(x, y, dir)], step) if (x, y, dir) in ok else step
                    return False
            return False

        dirs = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}
        for i in range(1, col - 1):
            if plate[0][i] == '.' and dfs(0, i, 'D', num):
                ans.append([0, i])
            if plate[row - 1][i] == '.' and row > 1 and dfs(row - 1, i, 'U', num):
                ans.append([row - 1, i])
        for i in range(1, row - 1):
            if plate[i][0] == '.' and dfs(i, 0, 'R', num):
                ans.append([i, 0])
            if plate[i][col - 1] == '.' and col > 1 and dfs(i, col - 1, 'L', num):
                ans.append([i, col - 1])
        return list(ans)



so = Solution()
print(so.ballGame(41, ["E...W..WW",".E...O...","...WO...W","..OWW.O..",".W.WO.W.E","O..O.W...",".OO...W..","..EW.WEE."]))
print(so.ballGame(3, [".....","....O","....O","....."]))
print(so.ballGame(5, [".....","..E..",".WO..","....."]))
print(so.ballGame(4, ["..E.",".EOW","..W."]))




