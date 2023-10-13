

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        n = len(processorTime)
        ans = 0
        for i in range(n):
            for j in range(4):
                ans = max(ans, processorTime[i] + tasks[i * 4 + j])
        return ans



so = Solution()
print(so.minProcessingTime(processorTime = [8,10], tasks = [2,2,3,1,8,7,4,5]))
print(so.minProcessingTime(processorTime = [10,20], tasks = [2,3,1,2,5,8,4,3]))




