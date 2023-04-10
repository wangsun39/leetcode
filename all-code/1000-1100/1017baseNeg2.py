class Solution:
    def baseNeg21(self, N: int):
        quotient = N
        strings = ''
        if 0 == N:
            return '0'
        while quotient != 0:
            quotient, remainder = self.division(quotient)
            strings = str(remainder) + strings
        return strings
    def division(self, N):
        # N = (-2) * quotient + remainder (0 <= remainder <= 1)
        # return quotient, remainder
        if N % 2 == 0:
            return N / (-2), 0
        remainder = 1
        quotient = (N - remainder) / (-2)
        return quotient, remainder

    def baseNeg2(self, N: int):
        # 2023/4/6
        def div2(x):
            q, r = divmod(x, -2)
            if r == -1:
                q += 1
                r = 1
            return q, r
        if N == 0: return '0'
        ans = []
        while N != 0:
            q, r = div2(N)
            N = q
            ans.append(str(r))
        return ''.join(ans[::-1])


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
obj = Solution()
print(obj.baseNeg2(3))
print(obj.baseNeg2(4))

