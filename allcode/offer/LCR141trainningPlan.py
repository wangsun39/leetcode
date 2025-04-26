# 给定一个头节点为 head 的单链表用于记录一系列核心肌群训练编号，请将该系列训练编号 倒序 记录于链表并返回。
#
#
#
# 示例 1：
#
# 输入：head = [1,2,3,4,5]
# 输出：[5,4,3,2,1]
#
#
# 示例 2：
#
# 输入：head = [1,2]
# 输出：[2,1]
#
#
# 示例 3：
#
# 输入：head = []
# 输出：[]
#
#
# 提示：
#
# 链表中节点的数目范围是 [0, 5000]
# -5000 <= Node.val <= 5000
#
#
# 注意：本题与主站 206 题相同： https://leetcode-cn.com/problems/reverse-linked-list/

from leetcode.allcode.competition.mypackage import *

class Solution:
    def trainningPlan(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return head
        pre = None
        cur = head
        while cur:
            t = cur.next
            cur.next = pre
            pre = cur
            if t is None:
                return cur
            cur = t


so = Solution()




