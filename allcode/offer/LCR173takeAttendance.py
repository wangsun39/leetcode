# 某班级 n 位同学的学号为 0 ~ n-1。点名结果记录于升序数组 records。假定仅有一位同学缺席，请返回他的学号。
#
#
#
# 示例 1：
#
# 输入：records = [0,1,2,3,5]
# 输出：4
# 示例 2：
#
# 输入：records = [0, 1, 2, 3, 4, 5, 6, 8]
# 输出：7
#
#
# 提示：
#
# 1 <= records.length <= 10000

from leetcode.allcode.competition.mypackage import *

class Solution:
    def takeAttendance(self, records: List[int]) -> int:
        n = len(records)
        if records[0] != 0: return 0
        if records[-1] != n: return n
        lo, hi = 0, n - 1
        while lo < hi - 1:
            mid = (lo + hi) // 2
            if records[mid] - records[lo] == mid - lo:
                lo = mid
            else:
                hi = mid
        return hi



so = Solution()
print(so.takeAttendance([0,1,2,3,5]))




