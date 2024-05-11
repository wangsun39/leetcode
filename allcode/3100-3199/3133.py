import math

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n2 = bin(n - 1)[2:][::-1]
        x2 = bin(x)[2:]
        arr = list(x2)[::-1]
        j = 0
        end = False
        for i in range(len(n2)):
            if end:
                arr.append(n2[i])
                continue
            while j < len(arr) and arr[j] == '1':
                j += 1
            if j < len(arr):
                arr[j] = n2[i]
                j += 1
            else:
                arr.append(n2[i])
                end = True
        res = ''.join(arr[::-1])
        return int(res, 2)



so = Solution()
print(so.minEnd(n = 3, x = 4))
print(so.minEnd(n = 2, x = 7))




