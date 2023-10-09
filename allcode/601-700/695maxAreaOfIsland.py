class Solution:
    def maxAreaOfIsland(self, grid):
        self.grid = grid
        self.row, self.column = len(grid), len(grid[0])
        self.checkMatrix = [[0] * (self.column) for _ in range(self.row)]
        maxArea = 0
        for i in range(self.row):
            for j in range(self.column):
                if grid[i][j] == 1 and self.checkMatrix[i][j] == 0:
                    maxArea = max(self.GetAreaOfPoint(i, j, 0), maxArea)
        return maxArea
    def GetAreaOfPoint(self, i, j, Area):
        if i >= self.row or j >= self.column or i < 0 or j < 0 \
            or self.checkMatrix[i][j] == 1 or self.grid[i][j] == 0:
            return Area
        self.checkMatrix[i][j] = 1
        Area += 1
        Area = self.GetAreaOfPoint(i+1, j, Area)
        Area = self.GetAreaOfPoint(i, j+1, Area)
        Area = self.GetAreaOfPoint(i-1, j, Area)
        Area = self.GetAreaOfPoint(i, j-1, Area)
        return Area


so = Solution()
print(so.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]))
