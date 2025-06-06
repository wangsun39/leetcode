# 堆箱子。给你一堆n个箱子，箱子宽 wi、深 di、高 hi。箱子不能翻转，将箱子堆起来时，下面箱子的宽度、高度和深度必须大于上面的箱子。实现一种方法，搭出最高的一堆箱子。箱堆的高度为每个箱子高度的总和。
#
# 输入使用数组[wi, di, hi]表示每个箱子。
#
# 示例 1：
#
#  输入：box = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
#  输出：6
# 示例 2：
#
#  输入：box = [[1, 1, 1], [2, 3, 4], [2, 6, 7], [3, 4, 5]]
#  输出：10
# 提示:
#
# 箱子的数目不大于3000个。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def pileBox(self, box: List[List[int]]) -> int:
        n = len(box)
        box.sort()
        dp = [b[2] for b in box]
        for i in range(n):
            for j in range(i):
                if box[j][0] < box[i][0] and box[j][1] < box[i][1] and box[j][2] < box[i][2]:
                    dp[i] = max(dp[i], dp[j] + box[i][2])
        return max(dp)


so = Solution()
print(so.pileBox(box = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]))




