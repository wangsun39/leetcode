# 为了提高自己的代码能力，小张制定了 LeetCode 刷题计划，他选中了 LeetCode 题库中的 n 道题，编号从 0 到 n-1，并计划在 m 天内按照题目编号顺序刷完所有的题目（注意，小张不能用多天完成同一题）。
#
# 在小张刷题计划中，小张需要用 time[i] 的时间完成编号 i 的题目。此外，小张还可以使用场外求助功能，通过询问他的好朋友小杨题目的解法，可以省去该题的做题时间。为了防止“小张刷题计划”变成“小杨刷题计划”，小张每天最多使用一次求助。
#
# 我们定义 m 天中做题时间最多的一天耗时为 T（小杨完成的题目不计入做题总时间）。请你帮小张求出最小的 T是多少。
#
# 示例 1：
#
# 输入：time = [1,2,3,3], m = 2
#
# 输出：3
#
# 解释：第一天小张完成前三题，其中第三题找小杨帮忙；第二天完成第四题，并且找小杨帮忙。这样做题时间最多的一天花费了 3 的时间，并且这个值是最小的。
#
# 示例 2：
#
# 输入：time = [999,999,999], m = 4
#
# 输出：0
#
# 解释：在前三天中，小张每天求助小杨一次，这样他可以在三天内完成所有的题目并不花任何时间。
#
#
#
# 限制：
#
# 1 <= time.length <= 10^5
# 1 <= time[i] <= 10000
# 1 <= m <= 1000

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minTime(self, time: List[int], m: int) -> int:
        n = len(time)
        if m >= n:
            return 0
        ss = sum(time)
        s = list(accumulate(time, initial=0))

        def check(val):
            cnt = 0
            mx = 0
            l = 0
            for r, x in enumerate(time):
                mx = max(mx, x)
                slr = s[r + 1] - s[l]
                if slr - mx <= val:
                    continue
                cnt += 1
                if cnt > m: return False
                l = r
                mx = x
            return cnt + 1 <= m

        lo, hi = 0, ss
        while lo < hi - 1:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid
        return hi


so = Solution()
print(so.minTime(time = [1,2,3], m = 3))
print(so.minTime(time = [1,2,3,3,3], m = 2))
print(so.minTime(time = [1,2,3,3], m = 2))





