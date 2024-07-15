# 给你一个整数数组 nums 和一个链表的头节点 head。从链表中移除所有存在于 nums 中的节点后，返回修改后的链表的头节点。
#
#
#
# 示例 1：
#
# 输入： nums = [1,2,3], head = [1,2,3,4,5]
#
# 输出： [4,5]
#
# 解释：
#
#
#
# 移除数值为 1, 2 和 3 的节点。
#
# 示例 2：
#
# 输入： nums = [1], head = [1,2,1,2,1,2]
#
# 输出： [2,2,2]
#
# 解释：
#
#
#
# 移除数值为 1 的节点。
#
# 示例 3：
#
# 输入： nums = [5], head = [1,2,3,4]
#
# 输出： [1,2,3,4]
#
# 解释：
#
#
#
# 链表中不存在值为 5 的节点。
#
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
# nums 中的所有元素都是唯一的。
# 链表中的节点数在 [1, 105] 的范围内。
# 1 <= Node.val <= 105
# 输入保证链表中至少有一个值没有在 nums 中出现过。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        l1 = []
        cur = head
        while cur:
            if cur.val not in nums:
                l1.append(cur)
            cur = cur.next
        if len(l1) == 0:
            return None
        head = l1[0]
        cur = head
        for x in l1[1:]:
            cur.next = x
            cur = cur.next
        return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

so = Solution()
print(so.modifiedList([1,2,3], head))




