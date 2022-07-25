# 完全二叉树 是每一层（除最后一层外）都是完全填充（即，节点数达到最大）的，并且所有的节点都尽可能地集中在左侧。
#
# 设计一种算法，将一个新节点插入到一个完整的二叉树中，并在插入后保持其完整。
#
# 实现 CBTInserter 类:
#
# CBTInserter(TreeNode root) 使用头节点为 root 的给定树初始化该数据结构；
# CBTInserter.insert(int v)  向树中插入一个值为 Node.val == val的新节点 TreeNode。使树保持完全二叉树的状态，并返回插入节点 TreeNode 的父节点的值；
# CBTInserter.get_root() 将返回树的头节点。
#  
#
# 示例 1：
#
#
#
# 输入
# ["CBTInserter", "insert", "insert", "get_root"]
# [[[1, 2]], [3], [4], []]
# 输出
# [null, 1, 2, [1, 2, 3, 4]]
#
# 解释
# CBTInserter cBTInserter = new CBTInserter([1, 2]);
# cBTInserter.insert(3);  // 返回 1
# cBTInserter.insert(4);  // 返回 2
# cBTInserter.get_root(); // 返回 [1, 2, 3, 4]
#  
#
# 提示：
#
# 树中节点数量范围为 [1, 1000] 
# 0 <= Node.val <= 5000
# root 是完全二叉树
# 0 <= val <= 5000 
# 每个测试用例最多调用 insert 和 get_root 操作 104 次

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        dq = [root]
        self.array = [None]
        while len(dq):
            x = dq.pop(0)
            self.array.append(x)
            if x.left:
                dq.append(x.left)
            if x.right:
                dq.append(x.right)

    def insert(self, val: int) -> int:
        n = len(self.array)
        node = TreeNode(val)
        if self.array[n // 2].left is None:
            self.array[n // 2].left = node
        else:
            self.array[n // 2].right = node
        self.array.append(node)
        return self.array[n // 2].val


    def get_root(self) -> TreeNode:
        return self.root

root = TreeNode(1)

so = CBTInserter(root)
so.insert(2)
print(so.get_root())


root = TreeNode(1)
root.left = TreeNode(2)

so = CBTInserter(root)
so.insert(3)
so.insert(4)
print(so.get_root())