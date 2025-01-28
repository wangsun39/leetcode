# 给定一个非负整数numRows，生成「杨辉三角」的前numRows行。
#
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。
#
#
#
#
#
# 示例 1:
#
# 输入: numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# 示例2:
#
# 输入: numRows = 1
# 输出: [[1]]

# 提示:
#
# 1 <= numRows <= 30

from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            line = [0] * (i + 1)
            line[0], line[-1] = 1, 1
            for j in range(1, i):
                line[j] = res[-1][j - 1] + res[-1][j]
            res.append(line)
        return res


so = Solution()
print(so.generate(5))

