# 给定一个头节点为 head 的链表用于记录一系列核心肌群训练项目编号，请查找并返回倒数第 cnt 个训练项目编号。
#
#
#
# 示例 1：
#
# 输入：head = [2,4,7,8], cnt = 1
# 输出：8
#
#
# 提示：
#
# 1 <= head.length <= 100
# 0 <= head[i] <= 100
# 1 <= cnt <= head.length

from leetcode.allcode.competition.mypackage import *

class Solution:
    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next
        return arr[-cnt]


so = Solution()




