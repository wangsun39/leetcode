# 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
#
# 你应当 保留 两个分区中每个节点的初始相对位置。
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
        l1 = []
        l2 = []
        node = head
        while node:
            if node.val < x:
                l1.append(node.val)
            else:
                l2.append(node.val)
            node = node.next
        ans = ListNode(0)
        cur = ans
        for x in l1:
            cur.next = ListNode(x)
            cur = cur.next
        for x in l2:
            cur.next = ListNode(x)
            cur = cur.next
        return ans.next




so = Solution()
print(so.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(so.maximalRectangle([["0","0"]]))
print(so.maximalRectangle([["1"]]))

