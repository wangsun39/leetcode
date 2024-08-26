# 注意：在这个问题中，操作次数增加为至多 两次 。
#
# 给你一个正整数数组 nums 。
#
# 如果我们执行以下操作 至多两次 可以让两个整数 x 和 y 相等，那么我们称这个数对是 近似相等 的：
#
# 选择 x 或者 y  之一，将这个数字中的两个数位交换。
# 请你返回 nums 中，下标 i 和 j 满足 i < j 且 nums[i] 和 nums[j] 近似相等 的数对数目。
#
# 注意 ，执行操作后得到的整数可以有前导 0 。
#
#
#
# 示例 1：
#
# 输入：nums = [1023,2310,2130,213]
#
# 输出：4
#
# 解释：
#
# 近似相等数对包括：
#
# 1023 和 2310 。交换 1023 中数位 1 和 2 ，然后交换数位 0 和 3 ，得到 2310 。
# 1023 和 213 。交换 1023 中数位 1 和 0 ，然后交换数位 1 和 2 ，得到 0213 ，也就是 213 。
# 2310 和 213 。交换 2310 中数位 2 和 0 ，然后交换数位 3 和 2 ，得到 0213 ，也就是 213 。
# 2310 和 2130 。交换 2310 中数位 3 和 1 ，得到 2130 。
# 示例 2：
#
# 输入：nums = [1,10,100]
#
# 输出：3
#
# 解释：
#
# 近似相等数对包括：
#
# 1 和 10 。交换 10 中数位 1 和 0 ，得到 01 ，也就是 1 。
# 1 和 100 。交换 100 中数位 1 和从左往右的第二个 0 ，得到 001 ，也就是 1 。
# 10 和 100 。交换 100 中数位 1 和从左往右的第一个 0 ，得到 010 ，也就是 10 。
#
#
# 提示：
#
# 2 <= nums.length <= 5000
# 1 <= nums[i] < 107

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countPairs(self, nums: List[int]) -> int:
        ans = 0
        counter = Counter()
        mxl = len(str(max(nums)))

        @cache
        def ext(x):
            sx = list(str(x))
            # 前面补0成为最大长度
            sx = ['0'] * (mxl - len(sx)) + sx
            m = len(sx)
            res = {x}
            for i in range(m):
                for j in range(i + 1, m):
                    sx[i], sx[j] = sx[j], sx[i]
                    res.add(int(''.join(sx)))
                    sx[i], sx[j] = sx[j], sx[i]
            return res
        for x in nums:
            adj = set()
            l = ext(x)
            adj |= l
            for y in l:
                adj |= ext(y)
            for y in adj:
                counter[y] += 1

        for x in nums:
            ans += counter[x] - 1  # 排除和自己配对

        return ans // 2  # 所有配对都会出现正反两次


so = Solution()
# print(so.countPairs(nums = [668700,238726]))
print(so.countPairs(nums = [1023,2310,2130,213]))
print(so.countPairs(nums = [886595,767627,6691,593887,857750,919155,830918,593887,593788,593788,660078,598873,310196,668007,597883,983587,897853,668700,435383,953887,631608,897853,953887,240754,593887,597883,455127,627877,643862,660087,893587,129173,228736,627877,775850,875750,50701,830255,751,729113,684778,114586,154186,593887,668700,238726]))
print(so.countPairs(nums = [1,1,1,1,1]))
print(so.countPairs(nums = [3,12,30,17,21]))
print(so.countPairs(nums = [50701, 751]))
print(so.countPairs(nums = [1,1,1,1,1]))
print(so.countPairs(nums = [123,231]))
print(so.countPairs(nums = [593887,593788]))




