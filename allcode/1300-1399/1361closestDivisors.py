# 二叉树上有 n 个节点，按从 0 到 n - 1 编号，其中节点 i 的两个子节点分别是 leftChild[i] 和 rightChild[i]。
#
# 只有 所有 节点能够形成且 只 形成 一颗 有效的二叉树时，返回 true；否则返回 false。
#
# 如果节点 i 没有左子节点，那么 leftChild[i] 就等于 -1。右子节点也符合该规则。
#
# 注意：节点没有值，本问题中仅仅使用节点编号。
#
#
#
# 示例 1：
#
#
#
# 输入：n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
# 输出：true
# 示例 2：
#
#
#
# 输入：n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
# 输出：false
# 示例 3：
#
#
#
# 输入：n = 2, leftChild = [1,0], rightChild = [-1,-1]
# 输出：false
#
#
# 提示：
#
# n == leftChild.length == rightChild.length
# 1 <= n <= 104
# -1 <= leftChild[i], rightChild[i] <= n - 1

from leetcode.allcode.competition.mypackage import *

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # 先找根节点，再用BFS遍历整个数
        fa = [-1] * n
        for i in range(n):
            left, right = leftChild[i], rightChild[i]
            if (left != -1 and fa[left] != -1) or (right != -1 and fa[right] != -1):
                return False
            if left != -1:
                fa[left] = i
            if right != -1:
                fa[right] = i
        vis = [0] * n
        if fa.count(-1) != 1:
            return False
        root = fa.index(-1)
        vis[root] = 1
        dq1 = deque([root])
        while dq1:
            dq2 = deque()
            while dq1:
                x = dq1.popleft()
                l, r = leftChild[x], rightChild[x]
                if l != -1:
                    if vis[l]:
                        return False
                    else:
                        dq2.append(l)
                        vis[l] = 1
                if r != -1:
                    if vis[r]:
                        return False
                    else:
                        dq2.append(r)
                        vis[r] = 1
            dq1 = dq2

        return all(x == 1 for x in vis)


so = Solution()
print(so.validateBinaryTreeNodes(4,[1,0,3,-1],[-1,-1,-1,-1]))
print(so.validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]))
print(so.validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]))
print(so.validateBinaryTreeNodes(n = 2, leftChild = [1,0], rightChild = [-1,-1]))




