# 假设你有一个长度为 n 的数组，初始情况下所有的数字均为 0，你将会被给出 k​​​​​​​ 个更新的操作。
#
# 其中，每个操作会被表示为一个三元组：[startIndex, endIndex, inc]，你需要将子数组 A[startIndex ... endIndex]（包括 startIndex 和 endIndex）增加 inc。
#
# 请你返回 k 次操作后的数组。
#
# 示例:
#
# 输入: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
# 输出: [-2,0,3,5,3]
# 解释:
#
# 初始状态:
# [0,0,0,0,0]
#
# 进行了操作 [1,3,2] 后的状态:
# [0,2,2,2,0]
#
# 进行了操作 [2,4,3] 后的状态:
# [0,2,5,5,3]
#
# 进行了操作 [0,2,-2] 后的状态:
# [-2,0,3,5,3]

from leetcode.allcode.competition.mypackage import *

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        diff = [0] * (length + 1)
        for x, y, i in updates:
            diff[x] += i
            diff[y + 1] -= i
        return list(accumulate(diff))[:-1]



so = Solution()
print(so.getModifiedArray(length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]))




