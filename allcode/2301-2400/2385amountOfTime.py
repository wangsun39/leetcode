# 给你一棵二叉树的根节点 root ，二叉树中节点的值 互不相同 。另给你一个整数 start 。在第 0 分钟，感染 将会从值为 start 的节点开始爆发。
#
# 每分钟，如果节点满足以下全部条件，就会被感染：
#
# 节点此前还没有感染。
# 节点与一个已感染节点相邻。
# 返回感染整棵树需要的分钟数。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,5,3,null,4,10,6,9,2], start = 3
# 输出：4
# 解释：节点按以下过程被感染：
# - 第 0 分钟：节点 3
# - 第 1 分钟：节点 1、10、6
# - 第 2 分钟：节点5
# - 第 3 分钟：节点 4
# - 第 4 分钟：节点 9 和 2
# 感染整棵树需要 4 分钟，所以返回 4 。
# 示例 2：
#
#
# 输入：root = [1], start = 1
# 输出：0
# 解释：第 0 分钟，树中唯一一个节点处于感染状态，返回 0 。
#
#
# 提示：
#
# 树中节点的数目在范围 [1, 105] 内
# 1 <= Node.val <= 105
# 每个节点的值 互不相同
# 树中必定存在值为 start 的节点


from leetcode.allcode.competition.mypackage import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        tree = defaultdict(set)
        def construct(node: TreeNode):
            array = [node]
            while len(array) > 0:
                cur = array.pop(0)
                if cur.left is not None:
                    tree[cur.val].add(cur.left.val)
                    tree[cur.left.val].add(cur.val)
                    array.append(cur.left)
                if cur.right is not None:
                    tree[cur.val].add(cur.right.val)
                    tree[cur.right.val].add(cur.val)
                    array.append(cur.right)

        def bfs(val):
            ans = 0
            infect = set()
            array = [val, '#']
            while len(array) > 1:
                cur = array.pop(0)
                if cur == '#':
                    ans += 1
                    array.append('#')
                    continue
                infect.add(cur)
                for e in tree[cur]:
                    if e not in infect:
                        array.append(e)
            return ans

        construct(root)
        return bfs(start)

root = TreeNode(1)
root.left = TreeNode(5)
root.right = TreeNode(3)


so = Solution()
print(so.amountOfTime(root, 3))




