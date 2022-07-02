
class Solution:
    def numEquivDominoPairs(self, dominoes):
        def equal(a, b):
            if (a[0] == b[0] and a[1] == b[1]) or (a[1] == b[0] and a[0] == b[1]):
                return True
            return False
        nums = len(dominoes)
        res = 0
        while len(dominoes) > 1:
            nums = len(dominoes)
            sum_D0 = 1 # 与第0个domino相同的domino个数(包括第0个)
            for l2 in range(nums-1, 0, -1):
                if equal(dominoes[0], dominoes[l2]):
                    sum_D0 += 1
                    dominoes.pop(l2)
            res += (sum_D0 * (sum_D0-1) // 2)
            dominoes.pop(0)
        return res

obj = Solution()
print(obj.numEquivDominoPairs([[1,2]]))
print(obj.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))

