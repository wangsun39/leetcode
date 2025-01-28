# 给定一个字符串和一个字符串字典，找到字典里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。如果答案不止一个，返回长度最长且字典顺序最小的字符串。如果答案不存在，则返回空字符串。
#
# 示例 1:
#
# 输入:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
#
# 输出:
# "apple"
# 示例2:
#
# 输入:
# s = "abpcplea", d = ["a","b","c"]
#
# 输出:
# "a"
# 说明:
#
# 所有输入的字符串只包含小写字母。
# 字典的大小不会超过 1000。
# 所有输入的字符串长度不会超过 1000。
from typing import List

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def match(s, d):
            if 0 == len(d):
                return True
            if 0 == len(s):
                return False
            pos = s.find(d[0])
            if -1 == pos:
                return False
            return match(s[pos+1:], d[1:])
        res = ''
        for x in d:
            if match(s, x):
                if len(x) > len(res):
                    res = x
                elif len(x) == len(res):
                    if x < res:
                        res = x
        return res


so = Solution()
print(so.findLongestWord('abpcplea', ["ale","apple","monkey","plea"]))
print(so.findLongestWord('abpcplea', ["a","b","c"]))
print(so.findLongestWord("bab", ["ba","ab","a","b"]))

