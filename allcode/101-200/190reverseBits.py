
class Solution:
    def reverseBits(self, n: int) -> int:
        res, cnt = 0, 0
        while cnt < 32:
            res = (res << 1) + (n & 1)
            n >>= 1
            cnt += 1
        return (res)

so = Solution()

print(so.reverseBits(10))
print(so.reverseBits(43261596))
print(so.reverseBits(4294967293))
