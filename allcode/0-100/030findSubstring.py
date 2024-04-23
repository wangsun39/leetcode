from collections import defaultdict
from collections import Counter
from typing import List
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
        words = set(words)
        n = len(s)
        ans = []
        def proc(start):
            counter = Counter()
            l = start
            r = start
            while l < n:
                while (r - l) // lw < len(words):
                    if s[r: r + lw] not in words:
                        l = r = r + lw
                        break
                    while counter[s[r: r + lw]] > 1:
                        counter[s[l: l + lw]] -= 1
                        l += lw

                    counter[s[r: r + lw]] += 1
        for i in range(lw):
            proc(i)
        return ans

so = Solution()
print(so.findSubstring("barfoothefoobarman", ["foo","bar"]))
print(so.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake",["fooo","barr","wing","ding","wing"]))
