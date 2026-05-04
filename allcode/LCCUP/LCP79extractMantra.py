# 随着兽群逐渐远去，一座大升降机缓缓的从地下升到了远征队面前。借由这台升降机，他们将能够到达地底的永恒至森。 在升降机的操作台上，是一个由魔法符号组成的矩阵，为了便于辨识，我们用小写字母来表示。 matrix[i][j] 表示矩阵第 i 行 j 列的字母。该矩阵上有一个提取装置，可以对所在位置的字母提取。 提取装置初始位于矩阵的左上角 [0,0]，可以通过每次操作移动到上、下、左、右相邻的 1 格位置中。提取装置每次移动或每次提取均记为一次操作。
#
# 远征队需要按照顺序，从矩阵中逐一取出字母以组成 mantra，才能够成功的启动升降机。请返回他们 最少 需要消耗的操作次数。如果无法完成提取，返回 -1。
#
# 注意：
#
# 提取装置可对同一位置的字母重复提取，每次提取一个
# 提取字母时，需按词语顺序依次提取
# 示例 1：
#
# 输入：matrix = ["sd","ep"], mantra = "speed"
#
# 输出：10
#
# 解释：如下图所示矩阵 (2).gif
#
# 示例 2：
#
# 输入：matrix = ["abc","daf","geg"]， mantra = "sad"
#
# 输出：-1
#
# 解释：矩阵中不存在 s ，无法提取词语
#
# 提示：
#
# 0 < matrix.length, matrix[i].length <= 100
# 0 < mantra.length <= 100
# matrix 和 mantra 仅由小写字母组成

from leetcode.allcode.competition.mypackage import *

class Solution:
    def extractMantra(self, matrix: List[str], mantra: str) -> int:
        n = len(mantra)
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        s = set()
        for line in matrix:
            for x in line:
                s.add(x)
        if not all(x in s for x in mantra): return -1
        vis = defaultdict(int)
        r, c = len(matrix), len(matrix[0])
        dq = deque([[0,0,0]])  # 行/列/匹配到的下标
        vis[(0, 0, 0)] = 0  # 保存3元组的最小步数
        while True:
            x, y, idx = dq.popleft()
            dxy = vis[(x, y, idx)]
            idx_n = idx
            if matrix[x][y] == mantra[idx]:
                idx_n += 1
                if idx_n == n:
                    return dxy + n
                if (x, y, idx_n) not in vis:
                    dq.append((x, y, idx_n))
                    vis[(x, y, idx_n)] = dxy

            for dx, dy in dir:
                # 这个地方的移动不能使用 idx_n，有可能会有连续在x,y位置的多次匹配，如果这个地方使用idx_n，就不能进行这种连续匹配了
                u, v = x + dx, y + dy
                if 0 <= u < r and 0 <= v < c and (u, v, idx) not in vis:
                    dq.append((u, v, idx))
                    vis[(u, v, idx)] = dxy + 1


so = Solution()
print(so.extractMantra(matrix = ["sd","ep"], mantra = "speed"))




