# 「力扣嘉年华」的中心广场放置了一个巨型的二叉树形状的装饰树。每个节点上均有一盏灯和三个开关。节点值为 0 表示灯处于「关闭」状态，节点值为 1 表示灯处于「开启」状态。每个节点上的三个开关各自功能如下：
#
# 开关 1：切换当前节点的灯的状态；
# 开关 2：切换 以当前节点为根 的子树中，所有节点上的灯的状态，；
# 开关 3：切换 当前节点及其左右子节点（若存在的话） 上的灯的状态；
# 给定该装饰的初始状态 root，请返回最少需要操作多少次开关，可以关闭所有节点的灯。
#
# 示例 1：
#
# 输入：root = [1,1,0,null,null,null,1]
#
# 输出：2
#
# 解释：以下是最佳的方案之一，如图所示b71b95bf405e3b223e00b2820a062ba4.gif
#
# 示例 2：
#
# 输入：root = [1,1,1,1,null,null,1]
#
# 输出：1
#
# 解释：以下是最佳的方案，如图所示a4091b6448a0089b4d9e8f0390ff9ac6.gif
#
# 示例 3：
#
# 输入：root = [0,null,0]
#
# 输出：0
#
# 解释：无需操作开关，当前所有节点上的灯均已关闭
#
# 提示：
#
# 1 <= 节点个数 <= 10^5
# 0 <= Node.val <= 1

from leetcode.allcode.competition.mypackage import *

class Solution:
    def closeLampInTree(self, root: TreeNode) -> int:
        # 4种状态, 1: 子树全关，2: 子树全开，3: 根节点开，下面全关，4: 根节点关，下面全开
        @cache
        def dfs(node: TreeNode, st):  # 将节点node变成状态 st 的最小操作数
            if node is None: return 0  # 节点为空，认为可以是任何一种状态，操作数为0
            if node.left is None and node.right is None:
                if st == 1 or st == 4:
                    return 0 if node.val == 0 else 1
                return 0 if node.val == 1 else 1
            l1, l2, l3, l4 = dfs(node.left, 1), dfs(node.left, 2), dfs(node.left, 3), dfs(node.left, 4)
            r1, r2, r3, r4 = dfs(node.right, 1), dfs(node.right, 2), dfs(node.right, 3), dfs(node.right, 4)
            to_0 = 0 if node.val == 0 else 1
            to_1 = 1 - to_0
            if st == 1:
                res = min(l1 + r1 + to_0, l2 + r2 + to_1 + 1, l3 + r3 + to_1 + 1, l4 + r4 + to_0 + 2)
            elif st == 2:
                res = min(l1 + r1 + to_0 + 1, l2 + r2 + to_1, l3 + r3 + to_1 + 2, l4 + r4 + to_0 + 1)
            elif st == 3:
                res = min(l1 + r1 + to_1, l2 + r2 + to_0 + 1, l3 + r3 + to_0 + 1, l4 + r4 + to_1 + 2)
            else:
                res = min(l1 + r1 + to_1 + 1, l2 + r2 + to_0, l3 + r3 + to_0 + 2, l4 + r4 + to_1 + 1)
            return res

        return dfs(root, 1)


so = Solution()
