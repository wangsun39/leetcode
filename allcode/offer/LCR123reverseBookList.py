# 书店店员有一张链表形式的书单，每个节点代表一本书，节点中的值表示书的编号。为更方便整理书架，店员需要将书单倒过来排列，就可以从最后一本书开始整理，逐一将书放回到书架上。请倒序返回这个书单链表。
#
#
#
# 示例 1：
#
# 输入：head = [3,6,4,1]
#
# 输出：[1,4,6,3]
#
#
# 提示：
#
# 0 <= 链表长度 <= 10000

from leetcode.allcode.competition.mypackage import *

class Solution:
    def reverseBookList(self, head: Optional[ListNode]) -> List[int]:
        cur = head
        nums = []
        while cur:
            nums.append(cur.val)
            cur = cur.next
        nums = nums[::-1]
        return nums


so = Solution()


