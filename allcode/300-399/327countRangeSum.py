import bisect
class Solution:
    def countRangeSum(self, nums, lower: int, upper: int):
        s = 0
        sums = [0]
        res = 0
        for i in nums:
            s += i
            if s - upper <= sums[-1] and s - lower >= sums[0]:
                min_idx = bisect.bisect_left(sums, s - upper)
                max_idx = bisect.bisect_right(sums, s - lower)
                # print(sums, i, s, max_idx, min_idx, max_idx - min_idx + 1)
                res += (max_idx - min_idx)
            bisect.insort(sums, s)
        return res


so = Solution()
print('res =', so.countRangeSum([-2,5,-1], -2, 2))
print('res =', so.countRangeSum([2147483647,-2147483648,-1,0], -1, 0))
print(bisect.bisect_left([1,2,2,3], 2))
print(bisect.bisect_left([1,2,2,3], 4))
print(bisect.bisect_right([1,2,2,3], 4))
print(bisect.bisect_left([1,2,2,3], 0))



