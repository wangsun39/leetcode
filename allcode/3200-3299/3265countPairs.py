# 给你一个正整数数组 nums 。
#
# 如果我们执行以下操作 至多一次 可以让两个整数 x 和 y 相等，那么我们称这个数对是 近似相等 的：
#
# 选择 x 或者 y  之一，将这个数字中的两个数位交换。
# 请你返回 nums 中，下标 i 和 j 满足 i < j 且 nums[i] 和 nums[j] 近似相等 的数对数目。
#
# 注意 ，执行操作后一个整数可以有前导 0 。
#
#
#
# 示例 1：
#
# 输入：nums = [3,12,30,17,21]
#
# 输出：2
#
# 解释：
#
# 近似相等数对包括：
#
# 3 和 30 。交换 30 中的数位 3 和 0 ，得到 3 。
# 12 和 21 。交换12 中的数位 1 和 2 ，得到 21 。
# 示例 2：
#
# 输入：nums = [1,1,1,1,1]
#
# 输出：10
#
# 解释：
#
# 数组中的任意两个元素都是近似相等的。
#
# 示例 3：
#
# 输入：nums = [123,231]
#
# 输出：0
#
# 解释：
#
# 我们无法通过交换 123 或者 321 中的两个数位得到另一个数。
#
#
#
# 提示：
#
# 2 <= nums.length <= 100
# 1 <= nums[i] <= 106

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countPairs(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        def check1(x, y):
            if x == y:
                return True
            if x > y: x, y = y, x
            sx, sy = list(str(x)), list(str(y))
            c1, c2 = Counter(sx), Counter(sy)
            # if c1 == c2:
            #     print(sx, sy)
            if len(sy) - len(sx) > 1:
                return False
            if len(sy) - len(sx) == 1:
                for i, u in enumerate(sy):
                    if u == '0':
                        sy[i], sy[0] = sy[0], sy[i]
                        if sx == sy[1:]:
                            return True
                        sy[i], sy[0] = sy[0], sy[i]
                return False
            # if sum(sx[i] != sy[i] for i in range(len(sx))) <= 2:
            #     print(sx, sy)
            diff = []
            for i, x in enumerate(sy):
                if x != sx[i]:
                    diff.append(i)
            if len(diff) != 2:
                return False
            return sx[diff[0]] == sy[diff[1]] and sx[diff[1]] == sy[diff[0]]

        def check(x, y):
            if x == y:
                return True
            if x > y: x, y = y, x
            sy = list(str(y))
            for i in range(len(sy)):
                for j in range(i + 1, len(sy)):
                    sy[i], sy[j] = sy[j], sy[i]
                    if int(''.join(sy)) == x:
                        return True
                    sy[i], sy[j] = sy[j], sy[i]
            return False

        for i in range(n):
            for j in range(i + 1, n):
                if check(nums[i], nums[j]):
                    ans += 1
        return ans




so = Solution()
print(so.countPairs(nums = [3,12,30,17,21]))
print(so.countPairs(nums = [50701, 751]))
print(so.countPairs(nums = [886595,767627,6691,593887,857750,919155,830918,593887,593788,593788,660078,598873,310196,668007,597883,983587,897853,668700,435383,953887,631608,897853,953887,240754,593887,597883,455127,627877,643862,660087,893587,129173,228736,627877,775850,875750,50701,830255,751,729113,684778,114586,154186,593887,668700,238726]))

print(so.countPairs(nums = [1,1,1,1,1]))
print(so.countPairs(nums = [123,231]))
print(so.countPairs(nums = [593887,593788]))




