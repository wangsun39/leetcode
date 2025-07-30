# 教学过程中，教练示范一次，学员跟做三次。该过程被混乱剪辑后，记录于数组 actions，其中 actions[i] 表示做出该动作的人员编号。请返回教练的编号。
#
#
#
# 示例 1：
#
# 输入：actions = [5, 7, 5, 5]
# 输出：7
# 示例 2：
#
# 输入：actions = [12, 1, 6, 12, 6, 12, 6]
# 输出：1
#
#
# 提示：
#
# 1 <= actions.length <= 10000
# 1 <= actions[i] < 2^31

from leetcode.allcode.competition.mypackage import *

class Solution:
    def trainingPlan(self, actions: List[int]) -> int:
        counter = Counter(actions)
        k0, v0 = None, None
        for k, v in counter.items():
            if v != v0 and v0 is not None:
                return k0 if v0 < v else k
            k0, v0 = k, v


so = Solution()
print(so.trainingPlan([5, 7, 5, 5]))




