import copy
class Solution:
    def knightDialer(self, N: int):
        if 1 == N:
            return 10
        self.nextNums = {1: {6, 8}, 2: {7, 9}, 3: {4, 8}, 4: {3, 9, 0}, 5: set(), 6: {1, 7, 0}, 7: {2, 6}, 8: {1, 3}, 9: {2, 4}, 0: {4, 6}}
        nDict_pre = {i: 1 for i in range(10)}
        for j in range(N-1):
            nDict_cur = {i: 0 for i in range(10)}
            for key in nDict_pre:
                for i in self.nextNums[key]:
                    nDict_cur[i] += nDict_pre[key]
                    nDict_cur[i] %= 1000000007
            nDict_pre = nDict_cur
        res = 0
        for i in nDict_cur:
            res += nDict_cur[i]
        return res % 1000000007


so = Solution()
print(so.knightDialer(3))
print(so.knightDialer(3660))
'''so.knightDialer(3)
so.knightDialer(4)
so.knightDialer(5)'''
