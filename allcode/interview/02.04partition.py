# 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
#
# 你不需要 保留 每个分区中各节点的初始相对位置。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,4,3,2,5,2], x = 3
# 输出：[1,2,2,4,3,5]
# 示例 2：
#
# 输入：head = [2,1], x = 2
# 输出：[1,2]
#
#
# 提示：
#
# 链表中节点的数目在范围 [0, 200] 内
# -100 <= Node.val <= 100
# -200 <= x <= 200

from leetcode.allcode.competition.mypackage import *

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = cur1 = None
        larger = cur2 = None
        cur = head
        while cur:
            if cur.val < x:
                if less:
                    cur1.next = ListNode(cur.val)
                else:
                    less = ListNode(cur.val)
                    cur1 = less
            else:
                if larger:
                    cur2.next = ListNode(cur.val)
                else:
                    larger = ListNode(cur.val)
                    cur2 = larger
        if less is None or larger is None:
            return head
        cur1.next = larger
        return cur1







