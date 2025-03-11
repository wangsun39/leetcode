# 给你一个 有向图 ，它含有 n 个节点和 m 条边。节点编号从 0 到 n - 1 。
#
# 给你一个字符串 colors ，其中 colors[i] 是小写英文字母，表示图中第 i 个节点的 颜色 （下标从 0 开始）。同时给你一个二维数组 edges ，其中 edges[j] = [aj, bj] 表示从节点 aj 到节点 bj 有一条 有向边 。
#
# 图中一条有效 路径 是一个点序列 x1 -> x2 -> x3 -> ... -> xk ，对于所有 1 <= i < k ，从 xi 到 xi+1 在图中有一条有向边。路径的 颜色值 是路径中 出现次数最多 颜色的节点数目。
#
# 请你返回给定图中有效路径里面的 最大颜色值 。如果图中含有环，请返回 -1 。
#
#
#
# 示例 1：
#
#
#
# 输入：colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
# 输出：3
# 解释：路径 0 -> 2 -> 3 -> 4 含有 3 个颜色为 "a" 的节点（上图中的红色节点）。
# 示例 2：
#
#
#
# 输入：colors = "a", edges = [[0,0]]
# 输出：-1
# 解释：从 0 到 0 有一个环。
#
#
# 提示：
#
# n == colors.length
# m == edges.length
# 1 <= n <= 105
# 0 <= m <= 105
# colors 只含有小写英文字母。
# 0 <= aj, bj < n

from leetcode.allcode.competition.mypackage import *

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        g = defaultdict(set)
        dp = [[0] * 26 for _ in range(n)]  # dp[i][j] 表示以 i 结尾的点中，每种颜色 j 最多多少个
        preNum = [0] * n
        for x, y in edges:
            if y not in g[x]:
                g[x].add(y)
                preNum[y] += 1
        ans = 0
        queue = deque([i for i in range(n) if preNum[i] == 0])  # deque 在操作大数组时，性能比 list 好很多
        s = 0
        while len(queue):
            q = queue.popleft()
            s += 1
            dp[q][ord(colors[q]) - ord('a')] += 1
            if dp[q][ord(colors[q]) - ord('a')] > ans:
                ans = dp[q][ord(colors[q]) - ord('a')]
            for x in g[q]:
                preNum[x] -= 1
                for i in range(26):
                    dp[x][i] = max(dp[q][i], dp[x][i])
                if preNum[x] == 0:
                    queue.append(x)
        print(dp)
        if s == n:
            return ans
        return -1


so = Solution()

print(so.largestPathValue("nnllnzznn", [[0,1],[1,2],[2,3],[2,4],[3,5],[4,6],[3,6],[5,6],[6,7],[7,8]]))
print(so.largestPathValue(colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]))
print(so.largestPathValue(colors = "a", edges = [[0,0]]))




