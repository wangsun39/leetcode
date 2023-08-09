from typing import List
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        M, N = len(mat), len(mat[0])
        def isTrans2Zero(OperList):
            for i in range(M):
                for j in range(N):
                    res = mat[i][j] + operList[i*N+j]
                    if i > 0:
                        res += OperList[(i - 1) * N + j]
                    if j > 0:
                        res += OperList[i * N + j - 1]
                    if i < M-1:
                        res += OperList[(i + 1) * N + j]
                    if j < N-1:
                        res += OperList[i * N + j + 1]
                    if 1 == res % 2:
                        return False
            return True

        def num2OperList(num):
            res = []
            for _ in range(N*M):
                res.append(num & 1)
                num >>= 1
            return res

        res = -1
        for i in range(2**(N*M)):
            operList = num2OperList(i)
            if (isTrans2Zero(operList)):
                if -1 == res:
                    res = operList.count(1)
                res = min(res, operList.count(1))
        return res

obj = Solution()
print(obj.minFlips( [[0],[1],[1]]))
print(obj.minFlips( [[0,0],[0,1]]))
print(obj.minFlips( [[1,1,1],[1,0,1],[0,0,0]]))
print(obj.minFlips( [[1,0,0],[1,0,0]]))
