
# 给你链表的头结点head，请将其按 升序 排列并返回 排序后的链表 。
#
# 进阶：
#
# 你可以在O(nlogn) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
# #
#
# 示例 1：
#
#
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
# 示例 2：
#
#
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
# 示例 3：
#
# 输入：head = []
# 输出：[]
#
#
# 提示：
#
# 链表中节点的数目在范围[0, 5 * 104]内
# -105<= Node.val <= 105




from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        def getListNum(node):
            i = 0
            cur = node
            while cur is not None:
                i += 1
                cur = cur.next
            return i
        N = getListNum(head)
        def merge(h1, h2):
            h = h1 if h1.val <= h2.val else h2
            if h1.val <= h2.val:
                h = h1
                h1 = h1.next
            else:
                h = h2
                h2 = h2.next
            cur = h
            while h1 is not None or h2 is not None:
                if h1 is None:
                    cur.next = h2
                    cur = h2
                    h2 = h2.next
                elif h2 is None:
                    cur.next = h1
                    cur = h1
                    h1 = h1.next
                else:
                    if h1.val <= h2.val:
                        cur.next = h1
                        cur = h1
                        h1 = h1.next
                    else:
                        cur.next = h2
                        cur = h2
                        h2 = h2.next
            return h
        def sortListN(head, N):
            if N <= 1:
                return head
            if 2 == N:
                if head.val > head.next.val:
                    res = head.next
                    head.next.next = head
                    head.next = None
                    return res
                else:
                    return head
            N1 = N // 2
            N2 = N - N1
            i, cur = 0, head
            while i < N1 - 1:
                i += 1
                cur = cur.next
            mid = cur.next
            cur.next = None
            h1 = sortListN(head, N1)
            h2 = sortListN(mid, N2)
            return merge(h1, h2)
        return sortListN(head, N)


so = Solution()

z = ListNode(4)
z.next = ListNode(2)
z.next.next = ListNode(1)
z.next.next.next = ListNode(3)
print(so.sortList(z))

z = ListNode(-1)
z.next = ListNode(5)
z.next.next = ListNode(3)
z.next.next.next = ListNode(4)
z.next.next.next.next = ListNode(0)
print(so.sortList(z))
