from functools import lru_cache
class Solution:
    def __init__(self):
        self.getAllStates(6)
    def funcA(self, L):
        for i in range(0, len(L)):
            L[i] *= -1
        return L
    def funcB(self, L):
        for i in range(1, len(L), 2):
            L[i] *= -1
        return L
    def funcC(self, L):
        for i in range(0, len(L), 2):
            L[i] *= -1
        return L
    def funcD(self, L):
        for i in range(0, len(L), 3):
            L[i] *= -1
        return L
    def getAllStates(self, n):
        '''
           假设原始状态为O
           有些基本规律，如：XX=O (X为任意A，B，C，D)，AB=C，AC=B，BC=A，可以得到下面的结论：
           操作1次可能的结果是A，B，C，D
           操作2次可能的结果是A，B，C，O，AD，BD，CD
           操作3次或以上可能的结果是A，B，C，D，O，AD，BD，CD'''
        self.allStates = [[1] * n]
        self.allStates.append(self.funcA([1] * n))
        self.allStates.append(self.funcB([1] * n))
        self.allStates.append(self.funcC([1] * n))
        self.allStates.append(self.funcD([1] * n))
        self.allStates.append(self.funcA(self.funcD([1] * n)))
        self.allStates.append(self.funcB(self.funcD([1] * n)))
        self.allStates.append(self.funcC(self.funcD([1] * n)))
        print(self.allStates)
    def flipLights1(self, n: int, m: int):
        if 0 == n:
            return 0
        if 0 == m:
            return 1
        if 1 == n:
            return 2
        if 2 == n:
            if 1 == m:
                return 3
            else:
                return 4
        if 1 == m:
            return 4
        if 2 == m:
            return 7
        else:
            return 8

    def flipLights(self, n: int, presses: int):
        @lru_cache(None)
        def next(L, time):
            # if L in ans:
            #     return
            if time == 0:
                ans.add(L)
                return
            n = len(L)
            L1, L2, L3, L4 = [], [], [], []
            for i in range(n):
                L1.append(-L[i])
                L2.append(L[i] if i % 2 == 0 else -L[i])
                L3.append(L[i] if i % 2 == 1 else -L[i])
                L4.append(-L[i] if i % 3 == 0 else L[i])

            next(tuple(L1), time - 1)
            next(tuple(L2), time - 1)
            next(tuple(L3), time - 1)
            next(tuple(L4), time - 1)

        # if presses == 0: return 1
        ans = set()
        L = tuple([1] * min(n, 6))
        next(L, presses)
        print(ans)
        return len(ans)




obj = Solution()
obj.flipLights(3, 2)
