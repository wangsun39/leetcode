class Solution:
    def minPathSum(self, grid):
        # 动态规划
        row, column = len(grid), len(grid[0])
        Max = sum([sum(grid[i]) for i in range(row)])#max(max([grid[i][0] for i in range(len(grid))]))
        M = [[Max] * (column + 1) for _ in range(row + 1)]
        M[0][0], M[1][0], M[0][1] = grid[0][0], 0, 0
        for i in range(1, row+1):
            for j in range(1, column+1):
                if i==1 and j==5:
                    print(grid[i-1][j-1], M[i-1][j], M[i][j-1])
                M[i][j] = min(grid[i-1][j-1] + M[i-1][j], grid[i-1][j-1] + M[i][j-1])
        for i in range(row):
            print(grid[i])
        for i in range(row+1):
            print(M[i])
        return M[row][column]



so = Solution()
print(so.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))

print(so.minPathSum([[1,4,8,6,2,2,1,7],[4,7,3,1,4,5,5,1],[8,8,2,1,1,8,0,1],[8,9,2,9,8,0,8,9],[5,7,5,7,1,8,5,5],[7,0,9,4,5,6,5,6],[4,9,9,7,9,1,9,0]]))