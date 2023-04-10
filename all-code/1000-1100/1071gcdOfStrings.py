class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def get_gcd(self, n1, n2):
        if n1 == n2:
            return n1
        if n1 < n2:
            n1, n2 = n2, n1
        while n1 % n2 != 0:
            n1 %= n2
            n1, n2 = n2, n1
        return n2
    def gcdOfStrings(self, str1: str, str2: str):
        def isDividedBy(a, b):
            length = len(a)
            for i in range(len(b)//length):
                if a != b[i*length:i*length+length]:
                    return False
            return True
        len1, len2 = len(str1), len(str2)
        if 0 == len1 or 0 == len2:
            return ''
        greatest_common_divisor = self.get_gcd(len1, len2)
        print(greatest_common_divisor)
        for i in range(greatest_common_divisor, 0, -1):
            if isDividedBy(str1[:greatest_common_divisor], str1) and isDividedBy(str1[:greatest_common_divisor], str2):
                return str1[:greatest_common_divisor]
        return ''

obj = Solution()
print(obj.gcdOfStrings('ABCABC','ABC'))

