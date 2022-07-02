
class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        N = len(string)
        i = 0
        while i < N // 2:
            if string[i] != string[N-1-i]:
                return False
            i += 1
        return True



so = Solution()
print(so.isPalindrome(121))
print(so.isPalindrome(-121))
