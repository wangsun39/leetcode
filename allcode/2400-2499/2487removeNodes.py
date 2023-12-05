# 给你一个链表的头节点 head 。
#
# 对于列表中的每个节点 node ，如果其右侧存在一个具有 严格更大 值的节点，则移除 node 。
#
# 返回修改后链表的头节点 head 。
#
#
#
# 示例 1：
#
#
#
# 输入：head = [5,2,13,3,8]
# 输出：[13,8]
# 解释：需要移除的节点是 5 ，2 和 3 。
# - 节点 13 在节点 5 右侧。
# - 节点 13 在节点 2 右侧。
# - 节点 8 在节点 3 右侧。
# 示例 2：
#
# 输入：head = [1,1,1,1]
# 输出：[1,1,1,1]
# 解释：每个节点的值都是 1 ，所以没有需要移除的节点。
#
#
# 提示：
#
# 给定列表中的节点数目在范围 [1, 105] 内
# 1 <= Node.val <= 105

from leetcode.allcode.competition.mypackage import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        stack = []
        while cur:
            while len(stack) and stack[-1].val < cur.val:
                stack.pop()
                if len(stack):
                    stack[-1].next = cur
            stack.append(cur)
            cur = cur.next
        return stack[0]

head = ListNode(5)
head.next = ListNode(2)
head.next.next = ListNode(13)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(8)

so = Solution()
print(so.removeNodes(head))




