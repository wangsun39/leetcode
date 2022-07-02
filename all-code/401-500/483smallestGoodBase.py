import math
class Solution:
    def smallestGoodBase1(self, n: str) -> str:
        num = int(n)
        N = int(math.sqrt(num))
        def isRightBase(k):
            cur, res = 1, 1
            while True:
                cur *= k
                res += cur
                if res == num:
                    return True
                elif res > num:
                    return False
        for k in range(2, N+1):
            if isRightBase(k):
                return str(k)
        return str(num - 1)
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)
        N = int(math.log2(num+1)) # num = 1 + 2^1 + 2^2 + ... + 2^(N-1) = 2^N - 1
        def sumkN(k, N):   # (1 + k^1 + k^2 + ... + k^(N-1))
            cur, res = 1, 1
            for i in range(N-1):
                cur *= k
                res += cur
            return res
        # f(k) = 1 + k^1 + k^2 + ... + k^(N-1) 当N固定时，f是k的单调增函数，可以用二分法求出是否存在某个K使得f(K)==num
        # 其中k的范围是[2, num^(1/(N-1))]
        for exponent in range(N, 1, -1):
            lower, upper = 2, num-1 #int(math.pow(num, 1/(exponent-1)))
            while lower <= upper:
                base = (lower + upper) // 2
                res = sumkN(base, exponent)
                if num == res:
                    return str(base)
                elif num < res:
                    upper = base - 1
                else:
                    lower = base + 1



so = Solution()
print(so.smallestGoodBase("727004545306745403"))
print(so.smallestGoodBase("1000000000000000000"))
print(so.smallestGoodBase("13"))
print(so.smallestGoodBase("3541"))
print(so.smallestGoodBase("4681"))
#print(so.diffWaysToCompute("2*3-4*5"))

