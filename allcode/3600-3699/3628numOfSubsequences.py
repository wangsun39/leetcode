# 给你一个由大写英文字母组成的字符串 s。
#
# 你可以在字符串的 任意 位置（包括字符串的开头或结尾）最多插入一个 大写英文字母。
#
# 返回在 最多插入一个字母 后，字符串中可以形成的 "LCT" 子序列的 最大 数量。
#
# 子序列 是从另一个字符串中删除某些字符（可以不删除）且不改变剩余字符顺序后得到的一个 非空 字符串。
#
#
#
# 示例 1：
#
# 输入： s = "LMCT"
#
# 输出： 2
#
# 解释：
#
# 可以在字符串 s 的开头插入一个 "L"，变为 "LLMCT"，其中包含 2 个子序列，分别位于下标 [0, 3, 4] 和 [1, 3, 4]。
#
# 示例 2：
#
# 输入： s = "LCCT"
#
# 输出： 4
#
# 解释：
#
# 可以在字符串 s 的开头插入一个 "L"，变为 "LLCCT"，其中包含 4 个子序列，分别位于下标 [0, 2, 4]、[0, 3, 4]、[1, 2, 4] 和 [1, 3, 4]。
#
# 示例 3：
#
# 输入： s = "L"
#
# 输出： 0
#
# 解释：
#
# 插入一个字母无法获得子序列 "LCT"，结果为 0。
#
#
#
# 提示：
#
# 1 <= s.length <= 105
# s 仅由大写英文字母组成。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numOfSubsequences(self, s: str) -> int:
        n = len(s)
        cl = cc = clc = ct = clct = 0
        cl_arr = [0] * n
        ct_arr = [0] * n
        for x in s:
            if x == 'L':
                cl += 1
            elif x == 'C':
                cc += 1
                clc += cl
            elif x == 'T':
                ct += 1
                clct += clc
        delta_t = clc  # 加T一定是在末尾，delta_t表示加在末尾将增加的数量
        orig_s = clct
        cl = cc = clct = ct = cct = 0
        for x in s[::-1]:
            if x == 'L':
                cl += 1
                clct += cct
            elif x == 'C':
                cc += 1
                cct += ct
            elif x == 'T':
                ct += 1
        delta_l = cct  # 加L一定是在开头，delta_l表示加在开头将增加的数量
        cl = 0
        for i in range(n):
            if s[i] == 'L':
                cl += 1
            cl_arr[i] = cl
        ct = 0
        for i in range(n - 1, -1, -1):
            ct_arr[i] = ct
            if s[i] == 'T':
                ct += 1
        delta_c = 0
        for i in range(n):  # 每个位置都可以加C，增加的值为，前面L的个数和后面T的个数取小
            delta_c = max(delta_c, cl_arr[i] * ct_arr[i])
        return orig_s + max(delta_l, delta_c, delta_t)


so = Solution()
print(so.numOfSubsequences(s = "LCLPTTGC"))
print(so.numOfSubsequences(s = "CT"))
print(so.numOfSubsequences(s = "LT"))
print(so.numOfSubsequences(s = "LCCT"))
print(so.numOfSubsequences(s = "LMCT"))




