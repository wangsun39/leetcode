import math
from functools import cache


class Solution1:
    def numSquares(self, n: int):
        self.calc_dict = {}
        min_class = self.findSquares(n)
        print(min_class)
        return len(min_class)
    def findSquares(self, n):
        #print(111, n, self.calc_dict)
        if n in self.calc_dict:
            return self.calc_dict[n]
        print(111, n)
        min_class = []
        root = math.sqrt(n)
        if int(root) * int(root) == n:
            self.calc_dict[n] = [int(root)]
            return [int(root)]
        max_i = int(root)
        #print(333, max_i)
        for i in range(max_i, 0, -1):
            cur = self.findSquares(n - i*i)[:]
            cur.append(i)
            if len(min_class) == 0 or len(min_class) > len(cur):
                min_class = cur
        self.calc_dict[n] = min_class[:]
        return min_class


class Solution:
    def numSquares(self, n: int):
        squares = {}
        for i in range(1, max(n,2)):
            x = i * i
            if x <= n:
                squares[x] = 1
            else:
                break
        print(squares)
        level = 1
        l1 = [n]
        used = {i:False for i in range(n+1)}
        used[n] = True
        while True:
            l2 = []
            for i in l1:
                if i in squares:
                    return level
                for j in squares:
                    if i <= j:
                        break
                    if not used[i-j]:
                        print(111)
                        l2.append(i-j)
                        used[i-j] = True
            level += 1
            #print(l2)
            l1 = l2[:]
    def numSquares1(self, n: int) -> int:
        mx = int(n ** 0.5)
        nums = [i * i for i in range(1, mx + 1)]
        @cache
        def dfs(i, s):  # 前 i 个平方数，构成 s 需要的最小平方数个数
            if s == 0: return 0
            if i == 0: return s
            ans = dfs(i - 1, s)
            if s >= nums[i]:
                ans = min(ans, dfs(i, s - nums[i]) + 1)
            return ans
        return dfs(mx - 1, n)

so = Solution1()
#print(so.numSquares(13))
print(so.numSquares(1))
print(so.numSquares(4128))

so = Solution()
print(so.numSquares1(4128))