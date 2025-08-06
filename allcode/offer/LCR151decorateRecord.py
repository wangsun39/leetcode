# 一棵圣诞树记作根节点为 root 的二叉树，节点值为该位置装饰彩灯的颜色编号。请按照如下规则记录彩灯装饰结果：
#
# 第一层按照从左到右的顺序记录
# 除第一层外每一层的记录顺序均与上一层相反。即第一层为从左到右，第二层为从右到左。
#
#
# 示例 1：
#
#
#
# 输入：root = [8,17,21,18,null,null,6]
# 输出：[[8],[21,17],[18,6]]
#
#
# 提示：
#
# 节点总数 <= 1000

from leetcode.allcode.competition.mypackage import *

class Solution:
    def decorateRecord(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq1 = deque([root])
        ans = []
        dir = True
        while dq1:
            dq2 = deque()
            lv = []
            while dq1:
                x = dq1.popleft()
                if x:
                    lv.append(x.val)
                    dq2.append(x.left)
                    dq2.append(x.right)
            dq1 = dq2
            if lv:
                if dir:
                    ans.append(lv)
                else:
                    ans.append(lv[::-1])
            dir = not dir
        return ans



so = Solution()
print(so. verifyTreeOrder([4,9,6,5,8]))




