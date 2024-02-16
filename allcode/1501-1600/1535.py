

from leetcode.allcode.competition.mypackage import *

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        dq = deque(arr)
        x = dq.popleft()
        cnt = 0
        if k >= len(arr) - 1:
            return max(arr)
        while True:
            y = dq.popleft()
            if x > y:
                cnt += 1
                dq.append(y)
            else:
                cnt = 1
                dq.append(x)
                x = y
            if cnt >= k:
                return x



so = Solution()
print(so.getWinner([1,25,35,42,68,70], 1))
print(so.getWinner(arr = [2,1,3,5,4,6,7], k = 2))
print(so.getWinner(arr = [3,2,1], k = 10))
print(so.getWinner(arr = [1,9,8,2,3,7,6,4,5], k = 7))
print(so.getWinner(arr = [1,11,22,33,44,55,66,77,88,99], k = 1000000000))




