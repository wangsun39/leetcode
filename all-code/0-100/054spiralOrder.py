# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
#
#
#
# 示例 1：
#
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 示例 2：
#
#
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#
#
# 提示：
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100


from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r, c = len(matrix), len(matrix[0])
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        di = 0
        s = {(0,0)}
        i, j = 0,0
        ans = []
        while True:
            ans.append(matrix[i][j])
            u, v = i + dir[di][0], j + dir[di][1]
            if u < 0 or u >= r or v < 0 or v >= c or (u,v) in s:
                di += 1
                di %= 4
                u, v = i + dir[di][0], j + dir[di][1]
            if u < 0 or u >= r or v < 0 or v >= c or (u,v) in s:
                break
            s.add((u,v))
            i,j=u,v

        return ans




so = Solution()
print(so.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
print(so.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
