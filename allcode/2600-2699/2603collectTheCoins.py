
from leetcode.allcode.competition.mypackage import *


class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        g = defaultdict(set)
        n = len(coins)
        deg = [0] * n
        for x, y in edges:
            g[x].add(y)
            g[y].add(x)
            deg[y] += 1
            deg[x] += 1


        # 先删除没有用的叶子节点
        no_use = deque([i for i in range(n) if deg[i] <= 1 and coins[i] == 0])
        if len(no_use) == n: return 0
        while len(no_use):
            q = no_use.popleft()
            if deg[q] > 0:
                deg[q] -= 1
            for x in g[q]:
                if deg[x] == 0: continue
                deg[x] -= 1
                if deg[x] == 1 and coins[x] == 0:
                    no_use.append(x)
        print(deg)

        leaf = deque([i for i in range(n) if deg[i] == 1])
        q2 = deque()
        #剩余的叶子节点都是有金币的，用拓扑排序连删两轮叶子节点
        for _ in range(2):
            while len(leaf):
                q = leaf.popleft()
                deg[q] -= 1
                for x in g[q]:
                    if deg[x] == 0: continue
                    deg[x] -= 1
                    if deg[x] == 1:
                        q2.append(x)
            leaf, q2 = q2, deque()
        left = sum(1 for x in deg if x > 0)
        if left == 0:
            return 0
        return (left - 1) * 2


so = Solution()
print(so.collectTheCoins([1,0,0,1,1,0,0,0,0,1,0,0],
[[0,1],[1,2],[1,3],[2,4],[4,5],[5,6],[5,7],[4,8],[7,9],[7,10],[10,11]]))
print(so.collectTheCoins(coins = [1], edges = []))  # 0
print(so.collectTheCoins(coins = [0], edges = []))  # 0
print(so.collectTheCoins(coins = [1,0,0,0,0,1], edges = [[0,1],[1,2],[2,3],[3,4],[4,5]]))  # 2
print(so.collectTheCoins(coins = [0,0,0,1,1,0,0,1], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[5,6],[5,7]]))  # 2




