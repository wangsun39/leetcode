# 给定一个 N 叉树，返回其节点值的后序遍历。
#
# 例如，给定一个3叉树:
#
#
#
#
#
#
#
# 返回其后序遍历: [5,6,3,2,4,1].
#
#
#
# 说明:递归法很简单，你可以使用迭代法完成此题吗?


from typing import List
import collections

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        Queue, res = collections.deque([root]), []
        while len(Queue) > 0:
            cur = Queue.pop()
            res.insert(0, cur.val)
            if cur.children is not None:
                Queue.extend(cur.children)

        return res


so = Solution()
root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])

print(so.postorder(root))

