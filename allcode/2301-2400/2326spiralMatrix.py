# 给你两个整数：m 和 n ，表示矩阵的维数。
#
# 另给你一个整数链表的头节点 head 。
#
# 请你生成一个大小为 m x n 的螺旋矩阵，矩阵包含链表中的所有整数。链表中的整数从矩阵 左上角 开始、顺时针 按 螺旋 顺序填充。如果还存在剩余的空格，则用 -1 填充。
#
# 返回生成的矩阵。
#
# 
#
# 示例 1：
#
#
# 输入：m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
# 输出：[[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
# 解释：上图展示了链表中的整数在矩阵中是如何排布的。
# 注意，矩阵中剩下的空格用 -1 填充。
# 示例 2：
#
#
# 输入：m = 1, n = 4, head = [0,1,2]
# 输出：[[0,1,2,-1]]
# 解释：上图展示了链表中的整数在矩阵中是如何从左到右排布的。
# 注意，矩阵中剩下的空格用 -1 填充。
# 
#
# 提示：
#
# 1 <= m, n <= 105
# 1 <= m * n <= 105
# 链表中节点数目在范围 [1, m * n] 内
# 0 <= Node.val <= 1000
from leetcode.allcode.competition.mypackage import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans = [[-1 for _ in range(n)] for _ in range(m)]
        cur = head
        i, j = 0, 0
        startx, endx, dx = 0, n - 1, 1
        starty, endy, dy = 1, m - 1, 1
        dir = 1
        while cur is not None:
            if dir == 1:
                for j in range(startx, endx + dx, dx):
                    ans[i][j] = cur.val
                    cur = cur.next
                    if cur is None:
                        break
                startx, endx, dx = endx - dx, startx, -dx
                dir = 2
            elif dir == 2:
                for i in range(starty, endy + dy, dy):
                    ans[i][j] = cur.val
                    cur = cur.next
                    if cur is None:
                        break
                starty, endy, dy = endy - dy, starty, -dy
                dir = 1
            if cur is None:
                break
            # cur = cur.next
        return ans


root = ListNode(3)
root.next = ListNode(0)
root.next.next = ListNode(2)
root.next.next.next = ListNode(6)
root.next.next.next.next = ListNode(8)
root.next.next.next.next.next = ListNode(1)
root.next.next.next.next.next.next = ListNode(7)
root.next.next.next.next.next.next.next = ListNode(9)
root.next.next.next.next.next.next.next.next = ListNode(4)
root.next.next.next.next.next.next.next.next.next = ListNode(2)
root.next.next.next.next.next.next.next.next.next.next = ListNode(5)
root.next.next.next.next.next.next.next.next.next.next.next = ListNode(5)
root.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)

so = Solution()
print(so.spiralMatrix(m = 3, n = 5, head = root))
root = ListNode(0)
root.next = ListNode(1)
root.next.next = ListNode(2)
print(so.spiralMatrix(m = 1, n = 4, head = root))




