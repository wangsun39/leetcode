# 给定两个以 有序链表 形式记录的训练计划 l1、l2，分别记录了两套核心肌群训练项目编号，请合并这两个训练计划，按训练项目编号 升序 记录于链表并返回。
#
# 注意：新链表是通过拼接给定的两个链表的所有节点组成的。
#
#
#
# 示例 1：
#
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
# 示例 2：
#
# 输入：l1 = [], l2 = []
# 输出：[]
# 示例 3：
#
# 输入：l1 = [], l2 = [0]
# 输出：[0]
#
#
# 提示：
#
# 0 <= 链表长度 <= 1000
#
#
#
# 注意：本题与主站 21 题相同： https://leetcode-cn.com/problems/merge-two-sorted-lists/

from leetcode.allcode.competition.mypackage import *

class Solution:
    def trainningPlan(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = l1, l2
        cur = pre = ListNode(0)
        while n1 and n2:
            if n1.val < n2.val:
                cur.next = n1
                n1 = n1.next
            else:
                cur.next = n2
                n2 = n2.next
            cur = cur.next
        if n1:
            cur.next = n1
        if n2:
            cur.next = n2
        return pre.next


so = Solution()




