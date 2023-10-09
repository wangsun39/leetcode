
class Solution:
    def minFallingPathSum1(self, arr) -> int:
        N = len(arr)
        if 1 == N:
            return arr[0][0]
        F1 = arr[0]   # F1,F2 交替记录前k行中，F1[i],F2[i]第k行选择第i个元素的时候，结果的最小值
        for line in arr[1:]:
            F2 = [200] * N
            for i in range(N):
                for j in range(N):
                    if i != j:
                        F2[i] = min(F2[i], line[i]+F1[j])
            print(F2)
            F1 = F2
        return min(F1)

    def minFallingPathSum(self, arr) -> int:
        N = len(arr)
        if 1 == N:
            return arr[0][0]
        if 2 == N:
            return min(arr[0][1] + arr[1][0], arr[0][0] + arr[1][1])
        def top3Arr(): # 返回每行Top3最小值
            T = []
            for line in arr:
                top3 = [[100, -1],[100, -1],[100, -1]]
                for i, e in enumerate(line):
                    if e < top3[0][0]:
                        top3[0], top3[1], top3[2] = [e, i], top3[0], top3[1]
                    elif e < top3[1][0]:
                        top3[1], top3[2] = [e, i], top3[1]
                    elif e < top3[2][0]:
                        top3[2] = [e, i]
                T.append(top3)
            return T

        T = top3Arr()
        print(T)
        F1 = T[0]   # F1,F2 交替记录前k行中，F1[i],F2[i]第k行选择第i个元素的时候，结果的最小值
        for line in T[1:]:
            F2 = [[30000, -1], [30000, -1], [30000, -1]]
            for i in range(3):
                for j in range(3):
                    if line[i][1] != F1[j][1]:
                        if F2[i][0] > line[i][0]+F1[j][0]:
                            F2[i] = [line[i][0]+F1[j][0], line[i][1]]
            print(F2)
            g = lambda x:x[0]
            F1 = F2
        return min(F2, key=lambda x:x[0])[0]

    def minFallingPathSum2(self, grid: List[List[int]]) -> int:
        # 2023/8/10 性能不高
        n = len(grid)
        dp1, dp2 = [x for x in grid[0]], [0] * n
        for i in range(1, n):
            for j in range(n):
                dp2[j] = min(x for k, x in enumerate(dp1) if k != j) + grid[i][j]
            dp1, dp2 = dp2, [0] * n
        return min(dp1)

obj = Solution()
#print(obj.minFallingPathSum( [[1,2,3],[4,5,6],[7,8,9]]))

print(obj.minFallingPathSum( [[2,2,1,2,2],[2,2,1,2,2],[2,2,1,2,2],[2,2,1,2,2],[2,2,1,2,2]]))
