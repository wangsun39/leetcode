# 给你一棵根节点为 0 的二叉树，它总共有 n个节点，节点编号为0到n - 1。同时给你一个下标从0开始的整数数组parents表示这棵树，其中parents[i]是节点 i的父节点。由于节点 0是根，所以parents[0] == -1。
#
# 一个子树的 大小为这个子树内节点的数目。每个节点都有一个与之关联的分数。求出某个节点分数的方法是，将这个节点和与它相连的边全部 删除，剩余部分是若干个 非空子树，这个节点的 分数为所有这些子树 大小的乘积。
#
# 请你返回有 最高得分节点的 数目。
#
# 
#
# 示例1:
#
#
#
# 输入：parents = [-1,2,0,2,0]
# 输出：3
# 解释：
# - 节点 0 的分数为：3 * 1 = 3
# - 节点 1 的分数为：4 = 4
# - 节点 2 的分数为：1 * 1 * 2 = 2
# - 节点 3 的分数为：4 = 4
# - 节点 4 的分数为：4 = 4
# 最高得分为 4 ，有三个节点得分为 4 （分别是节点 1，3 和 4 ）。
# 示例 2：
#
#
#
# 输入：parents = [-1,2,0]
# 输出：2
# 解释：
# - 节点 0 的分数为：2 = 2
# - 节点 1 的分数为：2 = 2
# - 节点 2 的分数为：1 * 1 = 1
# 最高分数为 2 ，有两个节点分数为 2 （分别为节点 0 和 1 ）。
# 
#
# 提示：
#
# n == parents.length
# 2 <= n <= 105
# parents[0] == -1
# 对于i != 0，有0 <= parents[i] <= n - 1
# parents表示一棵二叉树。






from leetcode.allcode.competition.mypackage import *
# Definition for a binary tree node.
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        N = len(parents)
        children = [[] for _ in range(N)]
        for i, e in enumerate(parents):
            if e == -1:
                root = i
            else:
                children[e].append(i)
        noOfChildren = [-1] * N
        print(children)
        def calc(i):
            if noOfChildren[i] != -1:
                return noOfChildren[i]
            noOfChildren[i] = 0
            for j in children[i]:
                noOfChildren[i] += (calc(j) + 1)
            return noOfChildren[i]
        calc(root)
        print(noOfChildren)
        res = 0
        maxScore = 0
        for i in range(N):
            score = 1
            for j in children[i]:
                score *= (noOfChildren[j] + 1)
            if parents[i] != -1:
                score *= (N - 1 - noOfChildren[i])
            if maxScore < score:
                res = 1
                maxScore = score
            elif maxScore == score:
                res += 1
        return res




so = Solution()
print(so.countHighestScoreNodes([-1,2,0,2,0]))
print(so.countHighestScoreNodes([-1,2,0]))

