# 给你一个链表的头节点 head，请你编写代码，反复删去链表中由 总和 值为 0 的连续节点组成的序列，直到不存在这样的序列为止。
#
# 删除完毕后，请你返回最终结果链表的头节点。
#
#
#
# 你可以返回任何满足题目要求的答案。
#
# （注意，下面示例中的所有序列，都是对 ListNode 对象序列化的表示。）
#
# 示例 1：
#
# 输入：head = [1,2,-3,3,1]
# 输出：[3,1]
# 提示：答案 [1,2,1] 也是正确的。
# 示例 2：
#
# 输入：head = [1,2,3,-3,4]
# 输出：[1,2,4]
# 示例 3：
#
# 输入：head = [1,2,3,-3,-2]
# 输出：[1]
#
#
# 提示：
#
# 给你的链表中可能有 1 到 1000 个节点。
# 对于链表中的每个节点，节点的值：-1000 <= node.val <= 1000.
from itertools import accumulate
from typing import List, Optional
from functools import cache
from math import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        node = head
        while node:
            l.append(node.val)
            node = node.next
        s = list(accumulate(l, initial=0))  # 前缀和
        l = [[0, 0]] + [[x, 1] for x in l]
        s = [[i, x] for i, x in enumerate(s)]
        i = 1
        while i < len(s):
            for j in range(i):
                if s[j][1] == s[i][1]:
                    # 删除 [j + 1, i]
                    for k in range(j + 1, i + 1):
                        l[s[k][0]][1] = 0
                    s[j + 1: i + 1] = []
                    i = j
                    break
            i += 1
        ll = [v for v, flg in l if flg]
        if len(ll) == 0:
            return None
        pre = first = ListNode(ll[0])
        for x in ll[1:]:
            pre.next = ListNode(x)
            pre = pre.next
        return first

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(-3)
head.next.next.next.next = ListNode(-2)
so = Solution()
print(so.removeZeroSumSublists(head))  # 14



