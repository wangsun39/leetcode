# 给你root1 和 root2这两棵二叉搜索树。请你返回一个列表，其中包含两棵树中的所有整数并按 升序 排序。.
#
# 
#
# 示例 1：
#
#
#
# 输入：root1 = [2,1,4], root2 = [1,0,3]
# 输出：[0,1,1,2,3,4]
# 示例 2：
#
#
#
# 输入：root1 = [1,null,8], root2 = [8,1]
# 输出：[1,1,8,8]
# 
#
# 提示：
#
# 每棵树的节点数在[0, 5000] 范围内
# -105<= Node.val <= 105


from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def toList(root):
            def dfs(root):
                left, right = [], []
                if root.left is not None:
                    left = dfs(root.left)
                if root.right is not None:
                    right = dfs(root.right)
                return left + [root.val] + right
            return dfs(root) if root is not None else []
        l1, l2 = toList(root1), toList(root2)
        res = []
        i, j = 0, 0
        if len(l1) == 0:
            return l2
        if len(l2) == 0:
            return l1
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                res.append(l1[i])
                i += 1
            elif l1[i] > l2[j]:
                res.append(l2[j])
                j += 1
            else:
                res.append(l1[i])
                res.append(l2[j])
                i += 1
                j += 1
            if i == len(l1):
                res += l2[j:]
                return res
            if j == len(l2):
                res += l1[i:]
                return res


so = Solution()
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(4)
root2 = TreeNode(1)
root2.left = TreeNode(0)
root2.right = TreeNode(3)
print(so.getAllElements(root1, root2))




