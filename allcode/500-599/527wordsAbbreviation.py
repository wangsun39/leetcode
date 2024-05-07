# 给你一个字符串数组 words ，该数组由 互不相同 的若干字符串组成，请你找出并返回每个单词的 最小缩写 。
#
# 生成缩写的规则如下：
#
# 初始缩写由起始字母+省略字母的数量+结尾字母组成。
# 若存在冲突，亦即多于一个单词有同样的缩写，则使用更长的前缀代替首字母，直到从单词到缩写的映射唯一。换而言之，最终的缩写必须只能映射到一个单词。
# 若缩写并不比原单词更短，则保留原样。
#
#
# 示例 1：
#
# 输入: words = ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
# 输出: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
# 示例 2：
#
# 输入：words = ["aa","aaa"]
# 输出：["aa","aaa"]
#
#
# 提示：
#
# 1 <= words.length <= 400
# 2 <= words[i].length <= 400
# words[i] 由小写英文字母组成
# words 中的所有字符串 互不相同

from leetcode.allcode.competition.mypackage import *

class Trie:

    def __init__(self):
        self.root = {'cnt': 0}

    def insert(self, word: str) -> None:  # O(log(len(word)))
        cur = self.root
        for e in word:
            if e not in cur:
                cur[e] = {'cnt': 1}
            else:
                cur[e]['cnt'] += 1
            cur = cur[e]
        if 'end' not in cur:
            cur['end'] = 1
        else:
            cur['end'] += 1
        # cur['cnt'] += 1

    def startWith(self, word: str) -> int:
        # 返回word的一个唯一前缀长度
        cur = self.root
        res = 0
        for e in word:
            res += 1
            if cur[e]['cnt'] == 1:
                return res
            cur = cur[e]
        return res

class Solution:
    def wordsAbbreviation1(self, words: List[str]) -> List[str]:
        tr = Trie()
        ans = []
        for w in words:
            if len(w) < 4:
                ans.append(w)
            else:
                ans.append('')
                tr.insert(w[-1] + w[:-1])  # 把最后一个字母放在最前面

        for i, w in enumerate(words):
            if len(ans[i]) == 0:
                v = max(tr.startWith(w[-1] + w[:-1]), 2)  # 匹配后，至少得有首尾两个字母
                if len(w) - v <= 1:
                    ans[i] = w
                else:
                    ans[i] = w[:v - 1] + str(len(w) - v) + w[-1]
        return ans

    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        n = len(words)

        ans = [''] * n
        idx1 = list(range(n))
        remain = 2  # 保留几个字母
        # 从小到大枚举剩余的字母，每次循环排除掉唯一的元素，下次循环增加一个保留字母
        while len(idx1):
            pair = []
            for i in idx1:
                w = words[i]
                if len(w) - remain <= 1:
                    ans[i] = w
                else:
                    pair.append([w[:remain - 1] + str(len(w) - remain) + w[-1], i])
            counter = defaultdict(list)
            for w, i in pair:
                counter[w].append(i)
            idx2 = []
            for abbr, v in counter.items():
                if len(v) == 1:
                    ans[v[0]] = abbr
                else:
                    idx2 += v
            idx1 = idx2
            remain += 1
        return ans




so = Solution()
print(so.wordsAbbreviation(words = ["abcdefg","abccefg","abcckkg","abccekg"]))  # Trie 树 这个用了没有通过
print(so.wordsAbbreviation(words = ["aa","aaa","aaaa","aaaaa"]))
print(so.wordsAbbreviation(words = ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]))

