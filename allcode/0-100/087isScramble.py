# 给定一个字符串s1，我们可以把它递归地分割成两个非空子字符串，从而将其表示为二叉树。
#
# 下图是字符串s1="great"的一种可能的表示形式。
#
#     great
#    /    \
#   gr    eat
#  / \    /  \
# g   r  e   at
#            / \
#           a   t
# 在扰乱这个字符串的过程中，我们可以挑选任何一个非叶节点，然后交换它的两个子节点。
#
# 例如，如果我们挑选非叶节点"gr"，交换它的两个子节点，将会产生扰乱字符串"rgeat"。
#
#     rgeat
#    /    \
#   rg    eat
#  / \    /  \
# r   g  e   at
#            / \
#           a   t
# 我们将"rgeat”称作"great"的一个扰乱字符串。
#
# 同样地，如果我们继续交换节点"eat"和"at"的子节点，将会产生另一个新的扰乱字符串"rgtae"。
#
#     rgtae
#    /    \
#   rg    tae
#  / \    /  \
# r   g  ta  e
#        / \
#       t   a
# 我们将"rgtae”称作"great"的一个扰乱字符串。
#
# 给出两个长度相等的字符串 s1 和s2，判断s2是否是s1的扰乱字符串。
#
# 示例1:
#
# 输入: s1 = "great", s2 = "rgeat"
# 输出: true
# 示例2:
#
# 输入: s1 = "abcde", s2 = "caebd"
# 输出: false



from typing import List
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        def isPermulation(s1, s2):
            d = {}
            if len(s1) != len(s2):
                return False
            for i in s1:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
            for i in s2:
                if i not in d:
                    return False
                if 0 == d[i]:
                    return False
                d[i] -= 1
            return True

        def helper(s1, s2):
            N = len(s1)
            if 1 == N:
                return True if s1 == s2 else False
            if (s1, s2) in scramble:
                return scramble[(s1, s2)]
            if not isPermulation(s1, s2):
                scramble[(s1, s2)] = False
                return False
            for i in range(0, N-1):
                if isPermulation(s1[:i + 1], s2[:i + 1]):
                    if helper(s1[:i + 1], s2[:i + 1]) and helper(s1[i + 1:], s2[i + 1:]):
                        scramble[(s1, s2)] = True
                        return True
                if isPermulation(s1[:i + 1], s2[N-i-1:]):
                    if helper(s1[:i + 1], s2[N-i-1:]) and helper(s1[i + 1:], s2[:N-i-1]):
                        scramble[(s1, s2)] = True
                        return True
            scramble[(s1, s2)] = False
            return False
        scramble = {}
        return helper(s1, s2)


so = Solution()
print(so.isScramble(s1 = "great", s2 = "rgeat"))
print(so.isScramble(s1 = "abcde", s2 = "caebd"))
print(so.isScramble("acddaaaadbcbdcdaccabdbadccaaa", "adcbacccabbaaddadcdaabddccaaa"))

