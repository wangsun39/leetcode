# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
#
# 注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。
#
#  
#
# 示例 1：
#
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 示例 2：
#
# 输入：s = "a", t = "a"
# 输出："a"
#  
#
# 提示：
#
# 1 <= s.length, t.length <= 105
# s 和 t 由英文字母组成
#  
#
# 进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？

from typing import List
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def str2dict(t):
            d = {}
            for i in t:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
            return d
        dictT = str2dict(t)
        print(dictT)
        dictS = {}   # {'A': [0, 3]]}  0, 3 是 A 在s中的位置，这个列表个数不超过dictT['A']的个数
        num_dictS = 0
        start, end = 0, len(s)
        for idx, x in enumerate(s):
            print(dictS)
            if x not in dictT:
                continue
            if x not in dictS:
                dictS[x] = [idx]
                num_dictS += 1
            else:
                if len(dictS[x]) >= dictT[x]:
                    dictS[x].pop(0)
                    num_dictS -= 1
                dictS[x].append(idx)
                num_dictS += 1
            if num_dictS == len(t):
                ch = min(dictS.keys(), key=(lambda k: dictS[k][0]))  # 找到dictS中下标最小的字符
                if idx - dictS[ch][0] < end - start:
                    start, end = dictS[ch][0], idx
                # res = min(res, idx - dictS[ch][0])
                dictS[ch].pop(0)  # 删除下标最小的字符，再继续循环
                num_dictS -= 1
        return s[start: end + 1] if end < len(s) else ''



so = Solution()
print(so.minWindow("a", "a"))
print(so.minWindow("ADOBECODEBANC", "ABC"))

