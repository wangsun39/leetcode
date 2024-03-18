# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[4,5,1,2,3]
# 示例 2：
#
#
# 输入：head = [0,1,2], k = 4
# 输出：[2,0,1]
#
#
# 提示：
#
# 链表中节点的数目在范围 [0, 500] 内
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        cur = head
        tail = None
        while cur:
            tail = cur
            n += 1
            cur = cur.next
        if n == 0 or k % n == 0:
            return head
        k %= n
        k = n - k
        cur = head
        cnt = 1
        while True:
            if cnt == k:
                break
            cur = cur.next
            cnt += 1
        res = cur.next
        tail.next = head
        cur.next = None
        return res








