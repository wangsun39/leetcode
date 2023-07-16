

from collections import defaultdict
class Solution:
    def loudAndRich1(self, richer, quiet):
        res = {i:[quiet[i],[]] for i in quiet} # {idx:[max_quiet, [smaller1, smaler2, ...]]}
        quiet2node = {quiet[i]:i for i in quiet}

        def update_richer(element, cur_quiet):
            res[element][0] = min(res[element][0], cur_quiet)
            for e in res[element][1]:
                res[e][0] = min(res[e][0], cur_quiet)
                update_richer(e, cur_quiet)
        for rich in richer:
            update_richer(rich[1], min(res[rich[0]][0], quiet[rich[0]])) #比rich[1]小的节点都要更新quiet值
            res[rich[0]][1].append(rich[1])
        print(res)
        print(quiet2node[res[0][0]])
        return [quiet2node[res[i][0]] for i in range(len(quiet))]

    def loudAndRich(self, richer, quiet):
        # 拓扑排序  2023/1/15
        n = len(quiet)
        tree = defaultdict(set)
        ans = [i for i in range(n)]  # 比自己richer的最安静值对应的id
        preNum = [0] * n
        for x, y in richer:
            if y not in tree[x]:
                tree[x].add(y)
                preNum[y] += 1
        queue = [i for i in range(n) if preNum[i] == 0]
        while len(queue):
            q = queue.pop(0)
            for x in tree[q]:
                preNum[x] -= 1
                if quiet[ans[q]] < quiet[ans[x]]:
                    ans[x] = ans[q]
                if preNum[x] == 0:
                    queue.append(x)
        return ans



so = Solution()
print(so.loudAndRich( [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], [3,2,5,4,6,1,7,0]))
print(so.loudAndRich( [], [0]))
print(so.loudAndRich( [[0,1],[1,2]], [0,1,2]))


