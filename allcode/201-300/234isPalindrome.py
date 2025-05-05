# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,2,1]
# 输出：true
# 示例 2：
#
#
# 输入：head = [1,2]
# 输出：false
#
#
# 提示：
#
# 链表中节点数目在范围[1, 105] 内
# 0 <= Node.val <= 9

from leetcode.allcode.competition.mypackage import *

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next
        n = len(nums)
        for i in range(n // 2):
            if nums[i] != nums[n - 1 - i]:
                return False
        return True


so = Solution()



