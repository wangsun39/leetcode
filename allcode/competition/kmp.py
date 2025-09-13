
from leetcode.allcode.competition.mypackage import *

# https://www.zhihu.com/question/21923021/answer/37475572

class Solution:

    def kmp(self, text: str, pattern: str) -> List[int]:
        # 在文本串 text 中查找模式串 pattern，返回所有成功匹配的位置（pattern[0] 在 text 中的下标）
        m = len(pattern)
        pi = [0] * m  # 前缀子串 s[:i + 1] 的真前缀和真后缀的最长匹配
        c = 0
        for i in range(1, m):
            v = pattern[i]
            while c and pattern[c] != v:
                c = pi[c - 1]
            if pattern[c] == v:
                c += 1
            pi[i] = c

        res = []
        c = 0
        for i, v in enumerate(text):
            v = text[i]
            while c and pattern[c] != v:
                c = pi[c - 1]
            if pattern[c] == v:
                c += 1
            if c == len(pattern):
                res.append(i - m + 1)
                c = pi[c - 1]
        return res


