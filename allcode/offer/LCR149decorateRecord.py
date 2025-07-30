# 一棵圣诞树记作根节点为 root 的二叉树，节点值为该位置装饰彩灯的颜色编号。请按照从 左 到 右 的顺序返回每一层彩灯编号。
#
#
#
# 示例 1：
#
#
#
# 输入：root = [8,17,21,18,null,null,6]
# 输出：[8,17,21,18,6]
#
#
# 提示：
#
# 节点总数 <= 1000

from leetcode.allcode.competition.mypackage import *

class Solution:
    def decorateRecord(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        dq = deque([root])
        ans = []
        while dq:
            x = dq.popleft()
            ans.append(x.val)
            if x.left: dq.append(x.left)
            if x.right: dq.append(x.right)
        return ans



so = Solution()
print(so.decorateRecord(putIn = [6,7,8,9,10,11], takeOut = [11,9,8,10,6,7]))




