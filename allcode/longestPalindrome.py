class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n == 0:
            return ""
        max_len = 1
        arg_max_head = 0
        i = 0
        while i < n:
            #print(1111,i,max_len,arg_max_head)
            j = 1
            cur_len = 1
            cur_head = i
            while j <= i:
                if i + j >= n or s[i-j] != s[i+j]:
                    break
                cur_len += 2
                cur_head = i - j
                j += 1
            if cur_len > max_len:
                max_len = cur_len
                arg_max_head = cur_head
            j = 0
            cur_len = 0
            cur_head = i
            while j <= i:
                if i + 1 + j >= n or s[i-j] != s[i+1+j]:
                    break
                cur_len += 2
                cur_head = i - j
                j += 1
            if cur_len > max_len:
                max_len = cur_len
                arg_max_head = cur_head
            i += 1
            #print(3333, i, max_len, arg_max_head)
        return s[arg_max_head:arg_max_head+max_len]

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x>=0 else -1
        string = str(sign*x)
        rev_str = string[::-1]
        real = sign*int(rev_str)
        if real > 2147483647 or real < -(2147483648):
            return 0
        else:
            return real

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip(' ')
        if len(str) == 0:
            return 0
        if str[0] == '-':
            sign = -1
            str = str[1:]
        elif str[0] == '+':
            sign = 1
            str = str[1:]
        else:
            sign = 1
        if len(str) == 0:
            return 0
        for i in range(len(str)):
            if not str[i].isdigit():
                i -= 1
                break
        str = str[:i+1]
        str = 0 if str =='' else str
        print(1111,str)
        real = int(str)*sign
        if real > 2147483647 :
            return 2147483647
        elif real < -(2147483648):
            return -2147483648
        else:
            return real

so = Solution()

'''print(so.longestPalindrome("abccba") == "abccba")
print(so.longestPalindrome("abcba"),so.longestPalindrome("abcba") == "abcba")
print(so.longestPalindrome("cbbd"),so.longestPalindrome("cbbd") == "bb")
print(so.longestPalindrome("bb"),so.longestPalindrome("bb") == "bb")
print(so.longestPalindrome("aaaa"),so.longestPalindrome("aaaa") == "aaaa")
print(so.longestPalindrome("bananas") )'''
print(so.myAtoi("123") == 123)
print(so.myAtoi("-123") == -123)
print(so.myAtoi("   -123ba") == -123)
print(so.myAtoi("   ba") == 0)
print(so.myAtoi("-") == 0)
print(so.myAtoi("  ") == 0)
print(so.myAtoi("-91283472332") == -2147483648)
