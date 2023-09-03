# 给定一个 N 叉树，返回其节点值的前序遍历。
#
# 例如，给定一个 3叉树 :

#
# 返回其前序遍历: [1,3,5,6,2,4]。
#
#  
#
# 说明: 递归法很简单，你可以使用迭代法完成此题吗?



from typing import List
import collections

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack, res = collections.deque([root]), []
        while len(stack) > 0:
            cur = stack.popleft()
            res.append(cur.val)
            if cur.children is not None:
                stack.extendleft(cur.children[::-1])
        return res


so = Solution()

