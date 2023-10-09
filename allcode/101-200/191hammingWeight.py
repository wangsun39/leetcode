
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            if 1 == n % 2:
                res += 1
            n = n // 2
        return res

so = Solution()

print(so.hammingWeight(3))
print(so.hammingWeight(4))
