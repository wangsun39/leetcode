# 这里有 n 个航班，它们分别从 1 到 n 进行编号。
#
# 有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi] 意味着在从 firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。
#
# 请你返回一个长度为 n 的数组 answer，里面的元素是每个航班预定的座位总数。
#
#
#
# 示例 1：
#
# 输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
# 输出：[10,55,45,25,25]
# 解释：
# 航班编号        1   2   3   4   5
# 预订记录 1 ：   10  10
# 预订记录 2 ：       20  20
# 预订记录 3 ：       25  25  25  25
# 总座位数：      10  55  45  25  25
# 因此，answer = [10,55,45,25,25]
# 示例 2：
#
# 输入：bookings = [[1,2,10],[2,2,15]], n = 2
# 输出：[10,25]
# 解释：
# 航班编号        1   2
# 预订记录 1 ：   10  10
# 预订记录 2 ：       15
# 总座位数：      10  25
# 因此，answer = [10,25]
#
#
# 提示：
#
# 1 <= n <= 2 * 104
# 1 <= bookings.length <= 2 * 104
# bookings[i].length == 3
# 1 <= firsti <= lasti <= n
# 1 <= seatsi <= 104


from leetcode.allcode.competition.mypackage import *


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * n
        diff = [0] * (n + 1)
        for x, y, c in bookings:
            diff[x - 1] += c
            diff[y] -= c
        s = 0
        for i, x in enumerate(diff[:-1]):
            s += x
            ans[i] = s
        return ans


obj = Solution()
print(obj.corpFlightBookings(bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5))


