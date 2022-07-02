# 统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
#
# 请注意，你可以假定字符串里不包括任何不可打印的字符。
#
# 示例:
#
# 输入: "Hello, my name is John"
# 输出: 5
# 解释: 这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。



from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def countSegments(self, s: str) -> int:
        s = s.strip()
        N = len(s)
        if 0 == N:
            return 0
        count = 1
        for i in range(1, N):
            if s[i] == ' ' and ' ' != s[i-1]:
                count += 1
        return count


so = Solution()
print(so.countSegments("Hello, my name is John"))
