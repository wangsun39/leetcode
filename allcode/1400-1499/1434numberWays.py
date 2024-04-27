

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        men = [0] * 40   # 第i个帽子适合哪些人
        for i, x in enumerate(hats):
            for y in x:
                men[y - 1] |= (1 << i)

        all_men = reduce(lambda x, y: x | y, men)

        @cache
        def dfs(start, left):  # 从第start个帽子开始，left是剩余没有帽子的人的bitmap
            if left == 0: return 1
            if start == 40:
                return 0
            res = dfs(start + 1, left)
            if men[start] == 0:
                return res
            for i in range(10):
                if men[start] & (1 << i) & left:  # 第i个人没有帽子
                    res += dfs(start + 1, left & (~(1 << i)))
                    res %= MOD
            return res
        return dfs(0, all_men)




so = Solution()
print(so.numberWays(hats = [[3,5,1],[3,5]]))
print(so.numberWays(hats = [[1,3,5,10,12,13,14,15,16,18,19,20,21,27,34,35,38,39,40],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40],[3,7,10,12,13,14,15,17,21,25,29,31,35,40],[2,3,7,8,9,11,12,14,15,16,17,18,19,20,22,24,25,28,29,32,33,34,35,36,38],[6,12,17,20,22,26,28,30,31,32,34,35],[1,4,6,7,12,13,14,15,21,22,27,28,30,31,32,35,37,38,40],[6,12,21,25,38],[1,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36,37,38,39,40]]))
print(so.numberWays(hats = [[3,4],[4,5],[5]]))
print(so.numberWays(hats = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]))
print(so.numberWays(hats = [[1,2,3],[2,3,5,6],[1,3,7,9],[1,8,9],[2,5,7]]))




