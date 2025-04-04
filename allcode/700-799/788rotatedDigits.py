# 我们称一个数 X 为好数, 如果它的每位数字逐个地被旋转 180 度后，我们仍可以得到一个有效的，且和 X 不同的数。要求每位数字都要被旋转。
#
# 如果一个数的每位数字被旋转以后仍然还是一个数字，则这个数是有效的。0, 1, 和 8 被旋转后仍然是它们自己；2 和 5 可以互相旋转成对方（在这种情况下，它们以不同的方向旋转，换句话说，2 和 5 互为镜像）；6 和 9 同理，除了这些以外其他的数字旋转以后都不再是有效的数字。
#
# 现在我们有一个正整数N, 计算从1 到N 中有多少个数X 是好数？
#
#
#
# 示例：
#
# 输入: 10
# 输出: 4
# 解释:
# 在[1, 10]中有四个好数： 2, 5, 6, 9。
# 注意 1 和 10 不是好数, 因为他们在旋转之后不变。
#
#
# 提示：
#
# N的取值范围是[1, 10000]。
#
# https://leetcode.cn/problems/rotated-digits

class Solution:
    def __init__(self):
        self.good = []
        for i in range(1, 10001):
            s = str(i)
            flg = False
            for ss in s:
                if ss in '347':
                    flg = False
                    break
                if ss in '2569':
                    flg = True
            if flg:
                self.good.append(i)
    def rotatedDigits(self, n: int) -> int:
        ans = 0
        for i in range(len(self.good)):
            if self.good[i] <= n:
                print(self.good[i])
                ans += 1
        return ans



so = Solution()
print(so.rotatedDigits(857))
print(so.rotatedDigits(10))

