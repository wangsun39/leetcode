# 给定一个由 0 和 1 组成的矩阵 mat，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。
#
# 两个相邻元素间的距离为 1 。
#
#
#
# 示例 1：
#
#
#
# 输入：mat = [[0,0,0],[0,1,0],[0,0,0]]
# 输出：[[0,0,0],[0,1,0],[0,0,0]]
# 示例 2：
#
#
#
# 输入：mat = [[0,0,0],[0,1,0],[1,1,1]]
# 输出：[[0,0,0],[0,1,0],[1,2,1]]
#
#
# 提示：
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# mat[i][j] is either 0 or 1.
# mat 中至少有一个 0



from typing import List
from collections import defaultdict

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        M, N = len(mat), len(mat[0])
        dp = [[200000] * (N + 2) for _ in range(M + 2)]
        offset = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        scanSet = set()
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if mat[i - 1][j - 1] == 0:
                    dp[i][j] = 0
                    for o in offset:
                        if 0 < i + o[0] < M + 1 and 0 <= j + o[1] < N + 1 and mat[i + o[0] - 1][j + o[1] - 1] == 1:
                            # dp[i + o[0]][j + o[1]] = 100000 # 待下一轮更新
                            scanSet.add((i + o[0], j + o[1]))
        print(dp)
        cur = 1
        def update(dp):
            next = set()
            for e in scanSet:
                dp[e[0]][e[1]] = cur
                for o in offset:
                    if 0 < e[0] + o[0] < M + 1 and 0 < e[1] + o[1] < N + 1 and dp[e[0] + o[0]][e[1] + o[1]] == 200000 and (e[0] + o[0], e[1] + o[1]) not in scanSet:
                        next.add((e[0] + o[0], e[1] + o[1]))  # 待下一轮更新
            return next
        while len(scanSet) > 0:
            scanSet = update(dp)
            cur += 1

        dp = dp[1: M + 1]
        print(dp)
        dp = [dp[i][1: N + 1] for i in range(M)]
        return dp


so = Solution()
print('ans=', so.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
print('ans=', so.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
# print(so.updateMatrix([[0,1,1,0,1,0,1,0,1,0],[1,1,1,0,0,0,1,0,0,1],[0,1,1,1,0,1,1,0,1,1],[1,1,1,1,0,1,1,1,1,0],[1,0,1,1,1,1,1,1,1,1],[1,1,1,1,0,0,1,0,1,1],[1,1,0,1,0,0,1,1,1,1],[1,1,0,1,0,0,1,0,0,0],[0,0,1,0,1,0,1,1,1,0],[1,1,1,1,0,1,1,0,1,1]]))

