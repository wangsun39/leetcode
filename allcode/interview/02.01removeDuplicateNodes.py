# 编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。
#
# 示例1：
#
#  输入：[1, 2, 3, 3, 2, 1]
#  输出：[1, 2, 3]
# 示例2：
#
#  输入：[1, 1, 1, 1, 2]
#  输出：[1, 2]
# 提示：
#
# 链表长度在[0, 20000]范围内。
# 链表元素在[0, 20000]范围内。
# 进阶：
#
# 如果不得使用临时缓冲区，该怎么解决？

from leetcode.allcode.competition.mypackage import *

class Solution:
    def removeDuplicateNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        cur = head
        cur2 = head
        vis = {head.val}
        while cur:
            if cur not in vis:
                vis.add(cur.val)
                cur2.next = cur
                cur2 = cur2.next
                cur = cur.next
            else:
                cur = cur.next
        return head







