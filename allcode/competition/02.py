

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        stack = [meetings[0]]
        for x, y in meetings[1:]:
            if stack[-1][1] >= x:
                stack[-1][1] = max(stack[-1][1], y)
            else:
                stack.append([x, y])
        s = sum(y - x + 1 for x, y in stack)
        return days - s





so = Solution()
print(so.countDays(days = 10, meetings = [[5,7],[1,3],[9,10]]))
print(so.countDays(days = 5, meetings = [[2,4],[1,3]]))
print(so.countDays(days = 6, meetings = [[1,6]]))




