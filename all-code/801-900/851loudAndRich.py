
class Solution:
    def loudAndRich(self, richer, quiet):
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



so = Solution()
#print(so.loudAndRich( [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], [3,2,5,4,6,1,7,0]))
#print(so.loudAndRich( [], [0]))
print(so.loudAndRich( [[0,1],[1,2]], [0,1,2]))


