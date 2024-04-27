# 给定一个字符串 s 和一个字符串数组 words。 words 中所有字符串 长度相同。
#
#  s 中的 串联子串 是指一个包含  words 中所有字符串以任意顺序排列连接起来的子串。
#
# 例如，如果 words = ["ab","cd","ef"]， 那么 "abcdef"， "abefcd"，"cdabef"， "cdefab"，"efabcd"， 和 "efcdab" 都是串联子串。 "acdbef" 不是串联子串，因为他不是任何 words 排列的连接。
# 返回所有串联子串在 s 中的开始索引。你可以以 任意顺序 返回答案。
#
#
#
# 示例 1：
#
# 输入：s = "barfoothefoobarman", words = ["foo","bar"]
# 输出：[0,9]
# 解释：因为 words.length == 2 同时 words[i].length == 3，连接的子字符串的长度必须为 6。
# 子串 "barfoo" 开始位置是 0。它是 words 中以 ["bar","foo"] 顺序排列的连接。
# 子串 "foobar" 开始位置是 9。它是 words 中以 ["foo","bar"] 顺序排列的连接。
# 输出顺序无关紧要。返回 [9,0] 也是可以的。
# 示例 2：
#
# 输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# 输出：[]
# 解释：因为 words.length == 4 并且 words[i].length == 4，所以串联子串的长度必须为 16。
# s 中没有子串长度为 16 并且等于 words 的任何顺序排列的连接。
# 所以我们返回一个空数组。
# 示例 3：
#
# 输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# 输出：[6,9,12]
# 解释：因为 words.length == 3 并且 words[i].length == 3，所以串联子串的长度必须为 9。
# 子串 "foobarthe" 开始位置是 6。它是 words 中以 ["foo","bar","the"] 顺序排列的连接。
# 子串 "barthefoo" 开始位置是 9。它是 words 中以 ["bar","the","foo"] 顺序排列的连接。
# 子串 "thefoobar" 开始位置是 12。它是 words 中以 ["the","foo","bar"] 顺序排列的连接。
#
#
# 提示：
#
# 1 <= s.length <= 104
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 30
# words[i] 和 s 由小写英文字母组成

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findSubStringRecur(self, offset, s, words): # 以单个word的长度从s的头部，每次跨越一个word长度查找，直至结尾
        d = defaultdict(lambda: 0)
        len_of_word = len(words[0])
        len_of_total_substr = len_of_word * len(words)
        if len(s) < len_of_total_substr:
            return
        for word in words:
            d[word] += 1
        no_of_find = 0 # 表示已经找到的个数，与d对应
        pos_begin, pos_cur = 0, 0
        while pos_begin <= len(s) - len_of_total_substr:
            while pos_cur + len_of_word <= len(s):
                if s[pos_cur:pos_cur+len_of_word] not in d:
                    pos_begin += len_of_word
                    pos_cur = pos_begin
                    d.clear()
                    for word in words:
                        d[word] += 1
                    no_of_find = 0
                    break
                if d[s[pos_cur:pos_cur+len_of_word]] <= 0:
                    d[s[pos_begin:pos_begin + len_of_word]] += 1
                    pos_begin += len_of_word
                    # pos_cur = pos_begin
                    no_of_find -= 1
                    break
                no_of_find += 1
                d[s[pos_cur:pos_cur + len_of_word]] -= 1
                if no_of_find == len(words):
                    self.res.append(pos_begin+offset)
                    d[s[pos_begin:pos_begin + len_of_word]] += 1
                    pos_begin += len_of_word
                    pos_cur += len_of_word
                    no_of_find -= 1
                    break
                else:
                    pos_cur += len_of_word


    def findSubstring1(self, s: str, words):
        self.res = []
        if 0 == len(words):
            return []
        len_of_substr = len(words[0])
        for i in range(len_of_substr):
            self.findSubStringRecur(i, s[i:], words)
        return self.res


    def findSubstring2(self, s: str, words: List[str]) -> List[int]:
        lw = len(words[0])
        expect = Counter(words)
        def helper(s, offset):
            i = 0
            s1 = []
            while i + lw <= len(s):
                s1.append(s[i: i + lw])
                i += lw
            d = Counter(words)
            # numOfd = 0
            n = len(words)
            if len(s1) < n:
                return []
            i, j = 0, 0
            ans = []
            while j < len(s1):

                if s1[j] in d:
                    d[s1[j]] -= 1
                    if d[s1[j]] == 0:
                        del d[s1[j]]
                    # j += 1
                else:
                    if s1[j] in expect:
                        while s1[i] != s1[j]:
                            if s1[i] in d:
                                d[s1[i]] += 1
                            else:
                                d[s1[i]] = 1
                            i += 1
                        i += 1
                        j += 1
                        continue
                    else:
                        i = j + 1
                        j += 1
                        continue
                if len(d) == 0 and j - i + 1 == n:
                    ans.append(i + offset)
                    d[s1[i]] = 1
                    i += 1
                j += 1
            return ans
        ans = []
        for i in range(lw):
            ans += helper(s[i:], i)
        return ans

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        lw = len(words[0])
        m = len(words)
        target = Counter(words)
        n = len(s)
        ans = []
        def proc(start):
            counter = Counter()
            l = start
            r = start
            while l < n:
                while r < n and (r - l) // lw < m:
                    if s[r: r + lw] not in target:
                        l = r = r + lw
                        counter.clear()
                        continue
                    counter[s[r: r + lw]] += 1
                    while counter[s[r: r + lw]] > target[s[r: r + lw]]:
                        counter[s[l: l + lw]] -= 1
                        l += lw
                    r += lw
                if (r - l) // lw == m:
                    ans.append(l)
                if r >= n:
                    break
                counter[s[l: l + lw]] -= 1
                l += lw

        for i in range(lw):
            proc(i)
        return ans

so = Solution()
print(so.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))
print(so.findSubstring("barfoothefoobarman", ["foo","bar"]))
print(so.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake",["fooo","barr","wing","ding","wing"]))
