

from leetcode.allcode.competition.mypackage import *

class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        if k in (1, 3, 9):
            return '9' * n
        if n < 2:
            if k >= 5: return str(k)
            if k == 2 or k == 4: return '8'
            if k == 3: return '9'
        if k == 2:
            return '8' + '9' * (n - 2) + '8'
        if k == 4:
            if n <= 4: return '8' * n
            return '88' + '9' * (n - 4) + '88'
        if k == 5:
            return '5' + '9' * (n - 2) + '5'
        if k == 6:
            if n == 2: return '66'
            if n & 1: return '8' + '9' * ((n - 3) // 2) + '8' + '9' * ((n - 3) // 2) + '8'
            return '8' + '9' * ((n - 4) // 2) + '77' + '9' * ((n - 4) // 2) + '8'
        if k == 8:
            if n <= 6: return '8' * n
            return '888' + '9' * (n - 6) + '888'
        if n & 1:
            mx = int(10 ** (n // 2 + 1) - 1)
            for i in range(int(mx), -1, -1):
                v = str(i) + str(i)[:-1][::-1]
                if int(v) % 7 == 0:
                    return v
        else:
            mx = int(10 ** (n // 2) - 1)
            for i in range(int(mx), -1, -1):
                v = str(i) + str(i)[::-1]
                if int(v) % 7 == 0:
                    return v



so = Solution()
print(so.largestPalindrome(4869, 7))
print(so.largestPalindrome(4, 7))




