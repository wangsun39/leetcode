# 给你一个由字符组成的 m x n 矩阵 grid 和一个字符串 pattern。
#
# 水平子串 是从左到右的一段连续字符序列。如果子串到达了某行的末尾，它将换行并从下一行的第一个字符继续。不会 从最后一行回到第一行。
#
# 垂直子串 是从上到下的一段连续字符序列。如果子串到达了某列的底部，它将换列并从下一列的第一个字符继续。不会 从最后一列回到第一列。
#
# 请统计矩阵中满足以下条件的单元格数量：
#
# 该单元格必须属于 至少 一个等于 pattern 的水平子串，且属于 至少 一个等于 pattern 的垂直子串。
# 返回满足条件的单元格数量。
# 
#
#
# 示例 1：
#
#
# 输入： grid = [["a","a","c","c"],["b","b","b","c"],["a","a","b","a"],["c","a","a","c"],["a","a","b","a"]], pattern = "abaca"
#
# 输出： 1
#
# 解释：
#
# "abaca" 作为一个水平子串（蓝色）和一个垂直子串（红色）各出现一次，并在一个单元格（紫色）处相交。
#
# 示例 2：
#
#
# 输入： grid = [["c","a","a","a"],["a","a","b","a"],["b","b","a","a"],["a","a","b","a"]], pattern = "aba"
#
# 输出： 4
#
# 解释：
#
# 上述被标记的单元格都同时属于至少一个 "aba" 的水平和垂直子串。
#
# 示例 3：
#
# 输入： grid = [["a"]], pattern = "a"
#
# 输出： 1
#
#
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 1000
# 1 <= m * n <= 105
# 1 <= pattern.length <= m * n
# grid 和 pattern 仅由小写英文字母组成。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        r, c = len(grid), len(grid[0])
        m = len(pattern)
        row = []
        col = []
        for i in range(r):
            row += grid[i]
        for co in list(zip(*grid)):
            col += list(co)
        row = ''.join(row)
        col = ''.join(col)
        # print(row, col)

        def kmp(text: str, pattern: str) -> List[int]:
            m = len(pattern)
            pi = [0] * m
            c = 0
            for i in range(1, m):
                v = pattern[i]
                while c and pattern[c] != v:
                    c = pi[c - 1]
                if pattern[c] == v:
                    c += 1
                pi[i] = c

            res = []
            c = 0
            for i, v in enumerate(text):
                v = text[i]
                while c and pattern[c] != v:
                    c = pi[c - 1]
                if pattern[c] == v:
                    c += 1
                if c == len(pattern):
                    res.append(i - m + 1)
                    c = pi[c - 1]
            return res

        idx1 = kmp(row, pattern)
        idx2 = kmp(col, pattern)
        # print(idx1, idx2)
        diff1 = [0] * (r * c)
        diff2 = [0] * (r * c)
        for x in idx1:
            diff1[x] += 1
            if x + m < r * c:
                diff1[x + m] -= 1
        for x in idx2:
            diff2[x] += 1
            if x + m < r * c:
                diff2[x + m] -= 1
        s1 = list(accumulate(diff1))
        s2 = list(accumulate(diff2))
        print(s1, s2)
        s1 = set((i//c, i%c) for i, x in enumerate(s1) if x)
        s2 = [(i%r, i//r) for i, x in enumerate(s2) if x]
        print(s1, s2)
        return len([x for x in s2 if x in s1])





so = Solution()
print(so.countCells(grid = [["a","a","c","c"],["b","b","b","c"],["a","a","b","a"],["c","a","a","c"],["a","a","b","a"]], pattern = "abaca"))




