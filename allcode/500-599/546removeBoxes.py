# 给出一些不同颜色的盒子 boxes ，盒子的颜色由不同的正数表示。
#
# 你将经过若干轮操作去去掉盒子，直到所有的盒子都去掉为止。每一轮你可以移除具有相同颜色的连续 k 个盒子（k >= 1），这样一轮之后你将得到 k * k 个积分。
#
# 返回 你能获得的最大积分和 。
#
#
#
# 示例 1：
#
# 输入：boxes = [1,3,2,2,2,3,4,3,1]
# 输出：23
# 解释：
# [1, 3, 2, 2, 2, 3, 4, 3, 1]
# ----> [1, 3, 3, 4, 3, 1] (3*3=9 分)
# ----> [1, 3, 3, 3, 1] (1*1=1 分)
# ----> [1, 1] (3*3=9 分)
# ----> [] (2*2=4 分)
# 示例 2：
#
# 输入：boxes = [1,1,1]
# 输出：9
# 示例 3：
#
# 输入：boxes = [1]
# 输出：1
#
#
# 提示：
#
# 1 <= boxes.length <= 100
# 1 <= boxes[i] <= 100

from leetcode.allcode.competition.mypackage import *

max = lambda a, b: b if b > a else a

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)

        @cache
        def dfs(l, r, k):
            if l > r: return 0
            if l == r:
                return (k + 1) * (k + 1)
            res = dfs(l, r - 1, 0) + (k + 1) * (k + 1)
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    res = max(res, dfs(l, i, k + 1) + dfs(i + 1, r - 1, 0))
            return res
        return dfs(0, n - 1, 0)

so = Solution()
print(so.removeBoxes([6,10,1,7,1,3,10,2,1,3]))
print(so.removeBoxes([1,3,2,2,2,3,4,3,1]))

