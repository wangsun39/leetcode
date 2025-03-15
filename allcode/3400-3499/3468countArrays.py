# 给你一个长度为 n 的数组 original 和一个长度为 n x 2 的二维数组 bounds，其中 bounds[i] = [ui, vi]。
#
# 你需要找到长度为 n 且满足以下条件的 可能的 数组 copy 的数量：
#
# 对于 1 <= i <= n - 1 ，都有 (copy[i] - copy[i - 1]) == (original[i] - original[i - 1]) 。
# 对于 0 <= i <= n - 1 ，都有 ui <= copy[i] <= vi 。
# 返回满足这些条件的数组数目。
#
#
#
# 示例 1
#
# 输入：original = [1,2,3,4], bounds = [[1,2],[2,3],[3,4],[4,5]]
#
# 输出：2
#
# 解释：
#
# 可能的数组为：
#
# [1, 2, 3, 4]
# [2, 3, 4, 5]
# 示例 2
#
# 输入：original = [1,2,3,4], bounds = [[1,10],[2,9],[3,8],[4,7]]
#
# 输出：4
#
# 解释：
#
# 可能的数组为：
#
# [1, 2, 3, 4]
# [2, 3, 4, 5]
# [3, 4, 5, 6]
# [4, 5, 6, 7]
# 示例 3
#
# 输入：original = [1,2,1,2], bounds = [[1,1],[2,3],[3,3],[2,3]]
#
# 输出：0
#
# 解释：
#
# 没有可行的数组。
#
#
#
# 提示：
#
# 2 <= n == original.length <= 105
# 1 <= original[i] <= 109
# bounds.length == n
# bounds[i].length == 2
# 1 <= bounds[i][0] <= bounds[i][1] <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        n = len(original)
        lo, hi = bounds[0]
        for i in range(1, n):
            d = original[i] - original[i - 1]
            lo, hi = lo + d, hi + d
            b1, b2 = bounds[i]
            # 取[lo, hi] 和 [b1, b2] 的交集
            if lo > b2 or hi < b1: return 0
            lo, hi = max(lo, b1), min(hi, b2)
        return hi - lo + 1



so = Solution()
print(so.countArrays(original = [1,2,3,4], bounds = [[1,2],[2,3],[3,4],[4,5]]))




