# 给你一个 n 个节点的树（也就是一个无环连通无向图），节点编号从 0 到 n - 1 ，且恰好有 n - 1 条边，每个节点有一个值。树的 根节点 为 0 号点。
#
# 给你一个整数数组 nums 和一个二维数组 edges 来表示这棵树。nums[i] 表示第 i 个点的值，edges[j] = [uj, vj] 表示节点 uj 和节点 vj 在树中有一条边。
#
# 当 gcd(x, y) == 1 ，我们称两个数 x 和 y 是 互质的 ，其中 gcd(x, y) 是 x 和 y 的 最大公约数 。
#
# 从节点 i 到 根 最短路径上的点都是节点 i 的祖先节点。一个节点 不是 它自己的祖先节点。
#
# 请你返回一个大小为 n 的数组 ans ，其中 ans[i]是离节点 i 最近的祖先节点且满足 nums[i] 和 nums[ans[i]] 是 互质的 ，如果不存在这样的祖先节点，ans[i] 为 -1 。
#
#
#
# 示例 1：
#
#
#
# 输入：nums = [2,3,3,2], edges = [[0,1],[1,2],[1,3]]
# 输出：[-1,0,0,1]
# 解释：上图中，每个节点的值在括号中表示。
# - 节点 0 没有互质祖先。
# - 节点 1 只有一个祖先节点 0 。它们的值是互质的（gcd(2,3) == 1）。
# - 节点 2 有两个祖先节点，分别是节点 1 和节点 0 。节点 1 的值与它的值不是互质的（gcd(3,3) == 3）但节点 0 的值是互质的(gcd(2,3) == 1)，所以节点 0 是最近的符合要求的祖先节点。
# - 节点 3 有两个祖先节点，分别是节点 1 和节点 0 。它与节点 1 互质（gcd(3,2) == 1），所以节点 1 是离它最近的符合要求的祖先节点。
# 示例 2：
#
#
#
# 输入：nums = [5,6,10,2,3,6,15], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
# 输出：[-1,0,-1,0,0,0,-1]
#
#
# 提示：
#
# nums.length == n
# 1 <= nums[i] <= 50
# 1 <= n <= 105
# edges.length == n - 1
# edges[j].length == 2
# 0 <= uj, vj < n
# uj != vj
import math

from leetcode.allcode.competition.mypackage import *

prime = defaultdict(list)
for i in range(1, 51):
    for j in range(i, 51):
        if math.gcd(i, j) == 1:
            prime[i].append(j)
            prime[j].append(i)

class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        ans = [-1] * n
        g = defaultdict(list)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        def dfs(x, fa, lev, vis):
            # vis[i] == [a, b] 表示i出现的最大层数为a，节点为b
            if len(prime[nums[x]]) > 0:
                ans[x] = max(vis[u] for u in prime[nums[x]])[1]
            tmp = vis[nums[x]][:]
            vis[nums[x]] = [lev, x]
            for y in g[x]:
                if y != fa:
                    dfs(y, x, lev + 1, vis)
            vis[nums[x]] = tmp[:]
        dfs(0, -1, 0, [[-1] * 2 for _ in range(51)])
        return ans



so = Solution()
print(so.getCoprimes(nums = [18,10,23,47,11,20,7,44,14,43,43,42,2,23,5,31,18,40,49,27,50,21,19,35,23,30,31,8,7,50,7,11,4,43,1,5,24,44,24,25,24,19,48,5,37,13,50,6,20,38,43,45,34,15,42,41,5,44,16,21,26,31,12,35,13,36,2,21,29,36,7,24,1,37,40,6,19,30,12,42,30,50,20,15,34,36,49,2,34,36,38,8,11,33,46,19,24,41,2,31,14,32,9,29,12,6,45,47,32,24,37,4,25,50,24,10,31,40,5,12,22,7,23,2,27,42,8,6,1,15,16,32,32,38,29,24,33,22,33,29,17],
                     edges = [[57,0],[5,57],[76,5],[85,76],[46,85],[127,85],[25,0],[114,25],[7,114],[45,114],[100,25],[122,100],[17,122],[12,17],[48,100],[40,48],[60,40],[88,48],[108,48],[10,108],[11,10],[121,11],[9,121],[109,11],[111,109],[91,109],[118,91],[53,118],[26,53],[47,26],[126,47],[133,109],[123,133],[59,123],[81,48],[31,81],[15,31],[24,15],[132,81],[119,132],[21,119],[63,81],[128,63],[73,128],[34,63],[72,34],[38,72],[97,72],[3,97],[30,3],[13,30],[80,13],[33,80],[66,80],[102,66],[8,80],[77,8],[79,77],[42,79],[19,42],[78,19],[20,78],[55,79],[37,55],[49,37],[89,49],[36,89],[83,89],[95,49],[64,95],[28,64],[32,28],[92,32],[93,92],[86,93],[39,86],[87,39],[2,87],[134,93],[135,49],[110,3],[29,110],[52,29],[136,29],[99,136],[50,99],[84,50],[56,84],[51,99],[112,51],[101,112],[41,29],[74,41],[103,74],[129,74],[6,129],[137,129],[61,29],[104,61],[131,104],[58,104],[14,58],[18,14],[138,18],[117,138],[125,138],[106,125],[120,18],[130,120],[124,130],[62,124],[82,62],[4,62],[113,4],[139,130],[1,104],[67,1],[70,1],[43,70],[96,70],[98,96],[69,98],[94,69],[115,94],[75,1],[44,75],[68,44],[16,68],[54,68],[65,68],[27,65],[71,65],[105,65],[35,105],[107,65],[116,65],[90,116],[23,90],[140,1],[22,140]]))
print(so.getCoprimes(nums = [2,3,3,2], edges = [[0,1],[1,2],[1,3]]))
print(so.getCoprimes(nums = [5,6,10,2,3,6,15], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]))




