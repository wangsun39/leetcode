# 给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。
#
# 示例 1：
#
# 输入: s1 = "abc", s2 = "bca"
# 输出: true
# 示例 2：
#
# 输入: s1 = "abc", s2 = "bad"
# 输出: false
# 说明：
#
# 0 <= len(s1) <= 100
# 0 <= len(s2) <= 100
#
# https://leetcode.cn/problems/check-permutation-lcci



from leetcode.allcode.competition.mypackage import *

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range((n + 1) // 2):
            for j in range(n // 2):
                matrix[j][n-1-i],matrix[n-1-i][n-1-j],matrix[n-1-j][i],matrix[i][j]=matrix[i][j],matrix[j][n-1-i],matrix[n-1-i][n-1-j],matrix[n-1-j][i]
        return

