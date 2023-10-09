# 在一个由 'L' , 'R' 和 'X' 三个字符组成的字符串（例如"RXXLRXRXL"）中进行移动操作。一次移动操作指用一个"LX"替换一个"XL"，或者用一个"XR"替换一个"RX"。现给定起始字符串start和结束字符串end，请编写代码，当且仅当存在一系列移动操作使得start可以转换成end时， 返回True。
#
#  
#
# 示例 :
#
# 输入: start = "RXXLRXRXL", end = "XRLXXRRLX"
# 输出: True
# 解释:
# 我们可以通过以下几步将start转换成end:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
#  
#
# 提示：
#
# 1 <= len(start) = len(end) <= 10000。
# start和end中的字符串仅限于'L', 'R'和'X'。
#
# https://leetcode.cn/problems/swap-adjacent-in-lr-string


from typing import List

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start.replace('X', '') != end.replace('X', ''):
            return False
        cnt, n = 0, len(start)
        L, R = [], []
        for i, e in enumerate(start):
            if e == 'X':
                cnt += 1
                continue
            if e == 'L':
                L.append(cnt)
            else:
                R.append(cnt)
        cnt, cntL, cntR = 0, 0, 0
        for i, e in enumerate(end):
            if e == 'X':
                cnt += 1
                continue
            if e == 'L':
                if L[cntL] < cnt:
                    return False
                cntL += 1
            else:
                if R[cntR] > cnt:
                    return False
                cntR += 1
        return True



so = Solution()
print(so.canTransform(start = "RXXLRXRXL", end = "XRLXXRRLX"))  # 1

