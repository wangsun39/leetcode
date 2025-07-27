

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
                clc += ct
            elif x == 'T':
                ct += 1
        delta_l = cct  # 加T一定是在开头，delta_l表示加在开头将增加的数量
        cl = 0
        for i in range(n):
            cl_arr[i] = cl
            if s[i] == 'L':
                cl += 1
        ct = 0
        for i in range(n - 1, -1, -1):
            ct_arr[i] = ct
            if s[i] == 'T':
                ct += 1
        delta_c = 0
        for i in range(n):  # 每个位置都可以加C，增加的值为，前面L的个数和后面T的个数取小
            delta_c = max(delta_c, min(cl_arr[i], ct_arr[i]))
        return orig_s + max(delta_l, delta_c, delta_t)


so = Solution()
print(so.numOfSubsequences(s = "LCCT"))
print(so.numOfSubsequences(s = "LMCT"))




