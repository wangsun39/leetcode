# m*n 的二维数组 plants 记录了园林景观的植物排布情况，具有以下特性：
#
# 每行中，每棵植物的右侧相邻植物不矮于该植物；
# 每列中，每棵植物的下侧相邻植物不矮于该植物。
#
#
# 请判断 plants 中是否存在目标高度值 target。
#
#
#
# 示例 1：
#
# 输入：plants = [[2,3,6,8],[4,5,8,9],[5,9,10,12]], target = 8
#
# 输出：true
#
#
# 示例 2：
#
# 输入：plants = [[1,3,5],[2,5,7]], target = 4
#
# 输出：false
#
#
# 提示：
#
# 0 <= n <= 1000
# 0 <= m <= 1000
# 注意：本题与主站 240 题相同： https://leetcode-cn.com/problems/search-a-2d-matrix-ii/

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findTargetIn2DPlants(self, plants: List[List[int]], target: int) -> bool:
        if len(plants) == 0 or len(plants[0]) == 0 or plants[0][0] > target: return False
        right = len(plants[0])
        for row in plants:
            p = bisect_left(row, target, 0, right)
            if p < right and row[p] == target: return True
            right = min(right, p)  # 逐步左移右端点
        return False


so = Solution()
print(so.findTargetIn2DPlants([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], 8))
print(so.findTargetIn2DPlants([[2,3,6,8],[4,5,8,9],[5,9,10,12]], 8))
print(so.findTargetIn2DPlants([[1,4],[2,5]], 2))



