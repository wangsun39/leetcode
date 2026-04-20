# 给你两个整数 l 和 r，以及一个由 恰好 三个 'D' 字符和三个 'R' 字符组成的字符串 directions。
#
# 对于范围 [l, r]（包含边界）内的每个整数 x，执行以下步骤：
#
# 如果 x 的位数少于 16 位，请在其左侧填充 前导零 ，使其成为 16 位的字符串。
# 将这 16 个数字以 行优先 的顺序放入一个 4 × 4 的网格中（前 4 个数字从左到右构成第一行，接下来的 4 个数字构成第二行，依此类推）。
# 从左上角单元格（row = 0，column = 0）开始，按顺序应用 directions 中的 6 个字符：
# 'D' 使行数加 1。
# 'R' 使列数加 1。
# 记录沿路径访问的数字序列（包括起始单元格），生成一个长度为 7 的序列。
# 如果记录的序列是 非递减 的，则认为整数 x 是一个 好 整数。
#
# 返回一个整数，表示在范围 [l, r] 内好整数的数量。
#
#
#
# 示例 1：
#
# 输入： l = 8, r = 10, directions = "DDDRRR"
#
# 输出： 2
#
# 解释：
#
# x = 8 的网格：
#
# 0	0	0	0
# 0	0	0	0
# 0	0	0	0
# 0	0	0	8
# 路径：(0,0) → (1,0) → (2,0) → (3,0) → (3,1) → (3,2) → (3,3)
# 访问的数字序列为 [0, 0, 0, 0, 0, 0, 8]。
# 由于访问的数字序列是非递减的，因此 8 是一个好整数。
# x = 9 的网格：
#
# 0	0	0	0
# 0	0	0	0
# 0	0	0	0
# 0	0	0	9
# 访问的数字序列为 [0, 0, 0, 0, 0, 0, 9]。
# 由于访问的数字序列是非递减的，因此 9 是一个好整数。
# x = 10 的网格：
#
# 0	0	0	0
# 0	0	0	0
# 0	0	0	0
# 0	0	1	0
# 访问的数字序列为 [0, 0, 0, 0, 0, 1, 0]。
# 由于访问的数字序列不是非递减的，因此 10 不是一个好整数。
# 因此，只有 8 和 9 是好整数，在该范围内总共有 2 个好整数。
# 示例 2：
#
# 输入： l = 123456789, r = 123456790, directions = "DDRRDR"
#
# 输出： 1
#
# 解释：
#
# x = 123456789 的网格：
#
# 0	0	0	0
# 0	0	0	1
# 2	3	4	5
# 6	7	8	9
# 路径：(0,0) → (1,0) → (2,0) → (2,1) → (2,2) → (3,2) → (3,3)
# 访问的数字序列为 [0, 0, 2, 3, 4, 8, 9]。
# 由于访问的数字序列是非递减的，因此 123456789 是一个好整数。
# x = 123456790 的网格：
#
# 0	0	0	0
# 0	0	0	1
# 2	3	4	5
# 6	7	9	0
# 访问的数字序列为 [0, 0, 2, 3, 4, 9, 0]。
# 由于访问的数字序列不是非递减的，因此 123456790 不是一个好整数。
# 因此，只有 123456789 是好整数，在该范围内总共有 1 个好整数。
# 示例 3：
#
# 输入： l = 1288561398769758, r = 1288561398769758, directions = "RRRDDD"
#
# 输出： 0
#
# 解释：
#
# x = 1288561398769758 的网格：
#
# 1	2	8	8
# 5	6	1	3
# 9	8	7	6
# 9	7	5	8
# 路径：(0,0) → (0,1) → (0,2) → (0,3) → (1,3) → (2,3) → (3,3)
# 访问的数字序列为 [1, 2, 8, 8, 3, 6, 8]。
# 由于访问的数字序列不是非递减的，因此 1288561398769758 不是一个好整数。
# 没有好整数，在该范围内总共有 0 个好整数。
#
#
# 提示：
#
# 1 <= l <= r <= 9 × 1015
# directions.length == 6
# directions 由 恰好 三个 'D' 字符和三个 'R' 字符组成。

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def countGoodIntegersOnPath(self, l: int, r: int, directions: str) -> int:

        def build_path_indices(directions: str):
            r0, c0 = 0, 0
            path = [r0 * 4 + c0]
            for ch in directions:
                if ch == 'D':
                    r0 += 1
                else:
                    c0 += 1
                path.append(r0 * 4 + c0)
            return path

        path = build_path_indices(directions)
        # print(path)

        def f(num: int):  # 数字 <= num 满足条件的所有数字
            num = str(num)
            num = '0' * (16 - len(str(num))) + num

            @cache
            def dfs(pos: int, is_limit: bool, k: int, last: int) -> int:
                # pos: 当前处理的位 [0..16)
                # is_limit: 是否与上界前缀相等 (0/1)
                # k: 已访问的路径点个数 (0..7)
                # last: 上一个路径点的数字，若 k==0 则 last==-1 if pos ==16:
                # 到达末尾，路径上的7个位置必然都已遇到（因为 P 单调递增且 <=15）
                if pos == 16:
                    return 1
                upper = int(num[pos]) if is_limit else 9
                res = 0
                is_path_pos = (k < 7 and pos == path[k])
                for j in range(0, upper + 1):
                    if is_path_pos:
                        if k > 0 and j < last:
                            continue
                        nk = k + 1
                        nlast = j
                    else:
                        nk = k
                        nlast = last

                    res += dfs(pos + 1, is_limit and j == upper, nk, nlast)
                return res

            return dfs(0, 1, 0, -1)

        return f(r) - f(l - 1)


so = Solution()
print(so.countGoodIntegersOnPath(l = 8, r = 10, directions = "DDDRRR"))




