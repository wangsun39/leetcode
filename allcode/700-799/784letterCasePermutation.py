# 一个n x n的二维网络board仅由0和1组成。每次移动，你能任意交换两列或是两行的位置。
#
# 返回 将这个矩阵变为 “棋盘”所需的最小移动次数。如果不存在可行的变换，输出 -1。
#
# “棋盘” 是指任意一格的上下左右四个方向的值均与本身不同的矩阵。
#
# 给定一个字符串 s ，通过将字符串 s 中的每个字母转变大小写，我们可以获得一个新的字符串。
#
# 返回 所有可能得到的字符串集合 。以 任意顺序 返回输出。
#
#
#
# 示例 1：
#
# 输入：s = "a1b2"
# 输出：["a1b2", "a1B2", "A1b2", "A1B2"]
# 示例 2:
#
# 输入: s = "3z4"
# 输出: ["3z4","3Z4"]
#
#
# 提示:
#
# 1 <= s.length <= 12
# s 由小写英文字母、大写英文字母和数字组成
# https://leetcode.cn/problems/letter-case-permutation/

from typing import List
from collections import Counter

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        n = len(s)
        def dfs(prefix):
            if len(prefix) == n:
                ans.append(prefix)
                return
            idx = len(prefix)
            if s[idx].isalpha():
                dfs(prefix + s[idx].lower())
                dfs(prefix + s[idx].upper())
                return
            dfs(prefix + s[idx])
        dfs('')
        return ans


so = Solution()
print(so.letterCasePermutation("a1b2"))  #

