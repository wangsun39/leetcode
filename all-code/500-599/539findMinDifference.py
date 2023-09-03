# 给定一个 24 小时制（小时:分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。
#
#  
#
# 示例 1：
#
# 输入：timePoints = ["23:59","00:00"]
# 输出：1
# 示例 2：
#
# 输入：timePoints = ["00:00","23:59","00:00"]
# 输出：0
#  
#
# 提示：
#
# 2 <= timePoints <= 2 * 104
# timePoints[i] 格式为 "HH:MM"


from typing import List
from collections import defaultdict

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        timeIntList = [time.split(':') for time in timePoints]
        print(timeIntList)
        N = len(timeIntList)

        def sub(y, x):
            res = int(y[0]) * 60 + int(y[1]) - int(x[0]) * 60 - int(x[1])
            return min(res, 24 * 60 - res)
        res = sub(timeIntList[-1], timeIntList[0])
        for i in range(1, N):
            res = min(res, sub(timeIntList[i], timeIntList[i-1]))
        return res



so = Solution()
print(so.findMinDifference( ["00:00","23:59"]))
print(so.findMinDifference( ["00:00","23:59","00:00"]))

