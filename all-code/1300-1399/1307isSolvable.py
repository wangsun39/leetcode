# 给你一个方程，左边用 words 表示，右边用 result 表示。
#
# 你需要根据以下规则检查方程是否可解：
#
# 每个字符都会被解码成一位数字（0 - 9）。
# 每对不同的字符必须映射到不同的数字。
# 每个 words[i] 和 result 都会被解码成一个没有前导零的数字。
# 左侧数字之和（words）等于右侧数字（result）。
# 如果方程可解，返回 True，否则返回 False。
#
#
#
# 示例 1：
#
# 输入：words = ["SEND","MORE"], result = "MONEY"
# 输出：true
# 解释：映射 'S'-> 9, 'E'->5, 'N'->6, 'D'->7, 'M'->1, 'O'->0, 'R'->8, 'Y'->'2'
# 所以 "SEND" + "MORE" = "MONEY" ,  9567 + 1085 = 10652
# 示例 2：
#
# 输入：words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"
# 输出：true
# 解释：映射 'S'-> 6, 'I'->5, 'X'->0, 'E'->8, 'V'->7, 'N'->2, 'T'->1, 'W'->'3', 'Y'->4
# 所以 "SIX" + "SEVEN" + "SEVEN" = "TWENTY" ,  650 + 68782 + 68782 = 138214
# 示例 3：
#
# 输入：words = ["THIS","IS","TOO"], result = "FUNNY"
# 输出：true
# 示例 4：
#
# 输入：words = ["LEET","CODE"], result = "POINT"
# 输出：false
#
#
# 提示：
#
# 2 <= words.length <= 5
# 1 <= words[i].length, results.length <= 7
# words[i], result 只含有大写英文字母
# 表达式中使用的不同字符数最大为 10
from functools import cache
from typing import List

class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        h = set(w[0] for w in words + [result] if len(w) > 1)  # 首字母
        d = {}  # 字母到数字的映射
        words = [list(w[::-1]) for w in words]  # 倒序放置
        result = list(result[::-1])
        # print(words)
        n = len(words)
        if len(result) < max(map(len, words)):
            return False
        m = len(result)

        def dfs(idx, mask, carry):
            if idx > m - 1: return carry == 0
            s = 0
            # 寻找 words[0][idx] + ... + words[n - 1][idx] == result[idx]
            not_finish = 0
            for i in range(n):
                if len(words[i]) <= idx: continue
                if words[i][idx] in d:
                    s += d[words[i][idx]]
                    continue
                not_finish = 1
                # 走到这说明进入这个函数的时候，有的字母还没有全部映射到数字，需要在下面的for中映射
                # 如果在for中找到正确的组合，那就在for中能return True，否则就失败了
                for j in range(10):
                    if mask & 1 << j: continue
                    if words[i][idx] in h and j == 0: continue
                    d[words[i][idx]] = j
                    res = dfs(idx, mask | (1 << j), carry)
                    if res: return True
                    d.pop(words[i][idx])
                if not_finish:  # 这个地方很关键，开始把这段放在了 i 的for循环之外，性能差了很多！！！
                    return False
            # 走到这里说明进入这个函数的时，所有的字母都已经映射到数字，只要校验一下即可
            if result[idx] in d:
                if d[result[idx]] != (s + carry) % 10:
                    return False
                return dfs(idx + 1, mask, (s + carry) // 10)

            v = (s + carry) % 10
            if mask & 1 << v or (v == 0 and result[idx] in h): return False
            d[result[idx]] = v
            res = dfs(idx + 1, mask | 1 << v, (s + carry) // 10)
            if res: return True
            d.pop(result[idx])

        return dfs(0, 0, 0)






so = Solution()
print(so.isSolvable(["AB","CD","EF"], "GHIJ"))  # False
print(so.isSolvable(["AA","BB"], "AA"))  # True
print(so.isSolvable(["A","B"], "A"))  # True
print(so.isSolvable(["CHE","IJGD","GFJG","GAD","GCG"], "EEIE"))  # True
print(so.isSolvable(["CBA","CBA","CBA","CBA","CBA"], "EDD"))  # False
print(so.isSolvable(words = ["SEND","MORE"], result = "MONEY"))  # True
# print(so.isSolvable(["I","THINK","IT","BE","THINE"], "INDEED"))
print(so.isSolvable(words = ["LEET","CODE"], result = "POINT"))  # False
print(so.isSolvable(["BUT","ITS","STILL"], "FUNNY"))
print(so.isSolvable(words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"))
print(so.isSolvable(words = ["THIS","IS","TOO"], result = "FUNNY"))




