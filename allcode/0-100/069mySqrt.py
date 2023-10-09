class Solution:
    def mySqrt(self, x: int):
        # 动态规划
        min = 0
        max = x // 2 + 2
        mid = (min + max) // 2
        while True:
            if mid * mid == x:
                return mid
            if max - min < 2:
                return min
            if mid * mid > x:
                max = mid
            else:
                min = mid
            mid = (min + max) // 2




so = Solution()
print(so.mySqrt(0))
print(so.mySqrt(1))
print(so.mySqrt(8))
print(so.mySqrt(4))
print(so.mySqrt(16))
print(so.mySqrt(17))
