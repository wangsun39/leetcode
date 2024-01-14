# 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,3,4,4,5]
# 输出：[1,2,5]
# 示例 2：
#
#
# 输入：head = [1,1,1,2,3]
# 输出：[2,3]
#
#
# 提示：
#
# 链表中节点数目在范围 [0, 300] 内
# -100 <= Node.val <= 100
# 题目数据保证链表已经按升序 排列

from leetcode.allcode.competition.mypackage import *

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(-1)
        root.next = head
        cur = root.next
        pre = root
        while cur:
            if cur.next is None:
                break
            if cur.val == cur.next.val:
                while cur.next.next and cur.val == cur.next.next.val:
                    cur.next = cur.next.next
                pre.next = cur.next.next
                cur = pre.next
            else:
                pre = cur
                cur = cur.next

        return root.next

r = ListNode(1)
r.next = ListNode(2)
r.next.next = ListNode(2)

so = Solution()
print(so.deleteDuplicates(r))




