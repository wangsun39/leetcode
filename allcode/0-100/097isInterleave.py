# 给定三个字符串s1、s2、s3，请你帮忙验证s3是否是由s1和s2 交错 组成的。
#
# 两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：
#
# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# 交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
# 提示：a + b 意味着字符串 a 和 b 连接。
#
# 
#
# 示例 1：
#
#
# 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 输出：true
# 示例 2：
#
# 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# 输出：false
# 示例 3：
#
# 输入：s1 = "", s2 = "", s3 = ""
# 输出：true
# 
#
# 提示：
#
# 0 <= s1.length, s2.length <= 100
# 0 <= s3.length <= 200
# s1、s2、和 s3 都由小写英文字母组成
#


from typing import List

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        d = {}
        def helper(s1, s2, s3):
            if (s1, s2, s3) in d:
                return d[(s1, s2, s3)]
            if 0 == len(s3):
                return True
            if 0 == len(s1) or 0 == len(s2):
                return s3 == s1 + s2
            if s1[0] == s3[0]:
                ret = helper(s1[1:], s2, s3[1:])
                if ret:
                    d[(s1, s2, s3)] = True
                    return True
            if s2[0] == s3[0]:
                ret = helper(s1, s2[1:], s3[1:])
                d[(s1, s2, s3)] = ret
                return ret
            d[(s1, s2, s3)] = False
            return False


        if len(s1) + len(s2) != len(s3):
            return False
        return helper(s1, s2, s3)


so = Solution()

print(so.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"))
print(so.isInterleave("aabcc", s2 = "dbbca", s3 = "aadbbbaccc"))
print(so.isInterleave(s1 = "", s2 = "", s3 = ""))

