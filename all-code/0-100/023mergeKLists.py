# 给你一个链表数组，每个链表都已经按升序排列。
#
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
#
#
#
# 示例 1：
#
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
# 示例 2：
#
# 输入：lists = []
# 输出：[]
# 示例 3：
#
# 输入：lists = [[]]
# 输出：[]
#
#
# 提示：
#
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] 按 升序 排列
# lists[i].length 的总和不超过 10^4
from heapq import *
from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hq = []
        ll = [x for x in lists]
        for i, x in enumerate(lists):
            if x:
                heappush(hq, [x.val, i])
        pre = ListNode(0)  # 伪头节点
        cur = pre
        while hq:
            v, i = heappop(hq)
            cur.next = ll[i]
            cur = cur.next
            ll[i] = ll[i].next
            if ll[i]:
                heappush(hq, [ll[i].val, i])
        cur.next = None
        return pre.next



l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)


l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

so = Solution()
print(so.mergeKLists([l1, l2]))
