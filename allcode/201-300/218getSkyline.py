class Solution1:
    #允许超过9的组合解法
    def combinationSum3(self, k: int, n: int):
        l = self.A(k, n, 1)
        return l
    def A(self, k, n, lower_bound):
        #lower_bound，满足条件的组合各元素的下界
        if n == 2 or lower_bound > n:
            return []
        if n == 1:
            if k == 1:
                return [[1]]
            else:
                return []
        if k == 1:
            return [[n]]
        l = []
        for i in range(lower_bound, n):
            l_A = self.A(k-1, n-i, i+1)
            if len(l_A) > 0:
                for j in l_A:
                    j = j + [i]
                    l.append(j)
        return l
class Solution:
    def combinationSum3(self, k: int, n: int):
        l = self.A(k, n, 1)
        return l
    def A(self, k, n, lower_bound):
        #lower_bound，满足条件的组合各元素的下界
        if n == 2 or lower_bound > n:
            return []
        if n == 1:
            if k == 1:
                return [[1]]
            return []
        if k == 1:
            if n > 9:
                return []
            return [[n]]
        l = []
        for i in range(lower_bound, n):
            l_A = self.A(k-1, n-i, i+1)
            if len(l_A) > 0:
                for j in l_A:
                    j = j + [i]
                    l.append(j)
        return l
so = Solution()
print(so.combinationSum3(3, 9))
print(so.combinationSum3(2, 18))

