class Solution:
    def computeArea(self, left1: int, lower1: int, right1: int, upper1: int, left2: int, lower2: int, right2: int, upper2: int) -> int:
        if left1 >= right2 or left2 >= right1 or lower1 >= upper2 or lower2 >= upper1:
            s3 = 0
        else:
            horizontal = min(abs(left1-right2), abs(left2-right1), abs(left1-right1), abs(left2-right2))
            vertical = min(abs(upper1-lower2), abs(upper2-lower1), abs(upper1-lower1), abs(upper2-lower2))
            s3 = horizontal * vertical #重叠面积
        s1 = (right1-left1) * (upper1-lower1)
        s2 = (right2-left2) * (upper2-lower2)
        return s1 + s2 - s3

so = Solution()
print(so.computeArea(-3, 0, 3, 4, 0, -1, 9, 2))
print(so.computeArea(0, 0, 0, 0, -1, -1, 1, 1))
print(so.computeArea(-2, -2, 2, 2, 3, 3, 4, 4))

