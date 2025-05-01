# 字符串轮转。给定两个字符串s1和s2，请编写代码检查s2是否为s1旋转而成（比如，waterbottle是erbottlewat旋转后的字符串）。
#
# 示例1:
#
#  输入：s1 = "waterbottle", s2 = "erbottlewat"
#  输出：True
# 示例2:
#
#  输入：s1 = "aa", s2 = "aba"
#  输出：False
# 提示：
#
# 字符串长度在[0, 100000]范围内。
# 说明:
#
# 你能只调用一次检查子串的方法吗？
#
# https://leetcode.cn/problems/string-rotation-lcci




from leetcode.allcode.competition.mypackage import *

class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2): return False
        s1 = s1 + s1
        pos = s1.find(s2)
        return pos != -1






