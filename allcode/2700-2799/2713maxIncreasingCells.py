# 给你一个下标从 1 开始、大小为 m x n 的整数矩阵 mat，你可以选择任一单元格作为 起始单元格 。
#
# 从起始单元格出发，你可以移动到 同一行或同一列 中的任何其他单元格，但前提是目标单元格的值 严格大于 当前单元格的值。
#
# 你可以多次重复这一过程，从一个单元格移动到另一个单元格，直到无法再进行任何移动。
#
# 请你找出从某个单元开始访问矩阵所能访问的 单元格的最大数量 。
#
# 返回一个表示可访问单元格最大数量的整数。
#
#
#
# 示例 1：
#
#
#
# 输入：mat = [[3,1],[3,4]]
# 输出：2
# 解释：上图展示了从第 1 行、第 2 列的单元格开始，可以访问 2 个单元格。可以证明，无论从哪个单元格开始，最多只能访问 2 个单元格，因此答案是 2 。
# 示例 2：
#
#
#
# 输入：mat = [[1,1],[1,1]]
# 输出：1
# 解释：由于目标单元格必须严格大于当前单元格，在本示例中只能访问 1 个单元格。
# 示例 3：
#
#
#
# 输入：mat = [[3,1,6],[-9,5,7]]
# 输出：4
# 解释：上图展示了从第 2 行、第 1 列的单元格开始，可以访问 4 个单元格。可以证明，无论从哪个单元格开始，最多只能访问 4 个单元格，因此答案是 4 。
#
#
# 提示：
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 105
# 1 <= m * n <= 105
# -105 <= mat[i][j] <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        r, c = len(mat), len(mat[0])
        rp = []  # 每一行一个优先队列，按值从大到小排
        for row in mat:
            hp = sorted([[x, i] for i, x in enumerate(row)], reverse=True)
            for i, [x, j] in enumerate(hp):
                if i == 0:
                    rp.append(deque([{j}]))
                    continue
                if hp[i - 1][0] == x:
                    rp[-1][-1].add(j)
                else:
                    rp[-1].append({j})
        print(rp)
        tmat = list(zip(*mat))  # 转置
        cp = []  # 每一列一个优先队列，按值从大到小排
        for row in tmat:
            hp = sorted([[x, i] for i, x in enumerate(row)], reverse=True)
            for i, [x, j] in enumerate(hp):
                if i == 0:
                    cp.append(deque([{j}]))
                    continue
                if hp[i - 1][0] == x:
                    cp[-1][-1].add(j)
                else:
                    cp[-1].append({j})
        print(cp)

        ans = 0
        while True:
            for row in range(r):
                # 取出当前每行的最大元素位置
                if len(rp[row]) == 0: continue
                s = rp[row][0]
                sd = set()  # s 中在本轮会删除的点
                for col in s:
                    if row in cp[col][0]:
                        sd.add(col)
            ans += 1


        # return ans


so = Solution()
print(so.maxIncreasingCells([[7,6,3],[-7,-5,6],[-7,0,-4],[6,6,0],[-8,6,0]]))
print(so.maxIncreasingCells([[1,1],[1,1]]))
print(so.maxIncreasingCells([[3,1,6],[-9,5,7]]))
print(so.maxIncreasingCells([[3, 1], [3, 4]]))
