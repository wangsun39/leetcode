# 返回 s 字典序最小的子序列，该子序列包含 s 的所有不同字符，且只包含一次。
#
#
#
# 示例 1：
#
# 输入：s = "bcabc"
# 输出："abc"
# 示例 2：
#
# 输入：s = "cbacdcbc"
# 输出："acdb"
#
#
# 提示：
#
# 1 <= s.length <= 1000
# s 由小写英文字母组成
#
#
# 注意：该题与 316 https://leetcode.cn/problems/remove-duplicate-letters/ 相同

from leetcode.allcode.competition.mypackage import *

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        l = list(s)

        def dfs(ss, mand):  # 返回满足题目要求的最小字典序的子序列，mand是必选字母
            if len(ss) == 0 or len(mand) == 0: return ''
            # 删除最后一个必须字母之后的所有字母
            for i in range(len(ss) - 1, -1, -1):
                if ss[i] in mand:
                    ss = ss[:i + 1]
                    break
            mn, mn_idx = ss[0], 0  # ss 上的最小值和第一个最小值的下标，无论这个最小值是否在mand中，这个最小字母都要是结果中的一项
            for i, x in enumerate(ss):
                if x < mn:
                    mn = x
                    mn_idx = i
            # 按mn的位置将ss分成3部分，mn之前，mn，mn之后
            # 先考虑之前的子串
            r1 = ''  # 前面子串的结果
            if mn_idx:
                s1, s2 = set(ss[:mn_idx]), set(ss[mn_idx + 1:])
                mand1 = set()  # 前一个子串的必选字母
                for x in s1:
                    if x in mand and x not in s2:
                        mand1.add(x)
                r1 = dfs(ss[:mn_idx], mand1)
            # 再考虑后面的子串
            # 先删除掉已经用掉的字母
            l2 = []
            vis = set(r1) | {mn}
            mand2 = set()
            for x in ss[mn_idx + 1:]:
                if x not in vis:
                    l2.append(x)
                    if x in mand:
                        mand2.add(x)
            r2 = dfs(l2, mand2)
            # print(ss, mand, r1, mn, r2)
            if len(r2) == 0 and mn not in mand:  # 这步很关键
                return r1
            return r1 + mn + r2
        return dfs(l, set(l))


so = Solution()
print(so.smallestSubsequence(s = "ojmgznybdllqahkblcickrmsfrppubzjkjxkcszeqprtnrmtpnqislrcxekuuuzbtsipvtujjulzkxaudxdhegzojdqzsyfuecfrpvqdhyyvxskpicqfyomeogckoagnzowhuogpqgueqgmtddtjepyhiphwkhlvjibnfpelhtffearwjusxnusrlabbgewycildblnepauwwpuhdxcdbbhhohadutuvkhoaafjohrvxeerfxknivvkavznkgvwfacojnkjcuqxzazeudtykpymeyiggujcithaczexffuzuxhkaqtjxbavxsmrgaektyfgtiaqjjkmegmkumiivlihlbhplybhrqmkoeohaflnbpsfaseuupyuumdgfckebamqxfamgaidrbkja"))
print(so.smallestSubsequence(s = "bcabc"))
print(so.smallestSubsequence(s = "cbacdcbc"))




