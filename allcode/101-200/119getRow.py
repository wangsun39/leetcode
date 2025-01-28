# 给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex行。
#
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。

# 示例 1:
#
# 输入: rowIndex = 3
# 输出: [1,3,3,1]
# 示例 2:
#
# 输入: rowIndex = 0
# 输出: [1]
# 示例 3:
#
# 输入: rowIndex = 1
# 输出: [1,1]
#
#
# 提示:
#
# 0 <= rowIndex <= 33
#
#
# 进阶：
#
# 你可以优化你的算法到 O(rowIndex) 空间复杂度吗？



from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(1, rowIndex + 1):
            line = [0] * (i + 1)
            line[0], line[-1] = 1, 1
            for j in range(1, i):
                line[j] = res[j - 1] + res[j]
            res = line
        return res


so = Solution()
print(so.getRow(3))

