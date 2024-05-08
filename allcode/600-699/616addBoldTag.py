# 给定字符串 s 和字符串数组 words。
#
# 对于 s 内部的子字符串，若其存在于 words 数组中， 则通过添加闭合的粗体标签 <b> 和 </b> 进行加粗标记。
#
# 如果两个这样的子字符串重叠，你应该仅使用一对闭合的粗体标签将它们包围起来。
# 如果被粗体标签包围的两个子字符串是连续的，你应该将它们合并。
# 返回添加加粗标签后的字符串 s 。
#
#
#
# 示例 1：
#
# 输入： s = "abcxyz123", words = ["abc","123"]
# 输出："<b>abc</b>xyz<b>123</b>"
# 解释：两个单词字符串是 s 的子字符串，如下所示: "abcxyz123"。
# 我们在每个子字符串之前添加<b>，在每个子字符串之后添加</b>。
# 示例 2：
#
# 输入：s = "aaabbb", words = ["aa","b"]
# 输出："<b>aaabbb</b>"
# 解释：
# "aa"作为子字符串出现了两次: "aaabbb" 和 "aaabbb"。
# "b"作为子字符串出现了三次: "aaabbb"、"aaabbb" 和 "aaabbb"。
# 我们在每个子字符串之前添加<b>，在每个子字符串之后添加</b>: "<b>a<b>a</b>a</b><b>b</b><b>b</b><b>b</b>"。
# 由于前两个<b>重叠，把它们合并得到: "<b>aaa</b><b>b</b><b>b</b><b>b</b>"。
# 由于现在这四个<b>是连续的，把它们合并得到: "<b>aaabbb</b>"。
#
#
# 提示：
#
# 1 <= s.length <= 1000
# 0 <= words.length <= 100
# 1 <= words[i].length <= 1000
# s 和 words[i] 由英文字母和数字组成
# words 中的所有值 互不相同
#
#
# 注：此题与「758 - 字符串中的加粗单词」相同 - https://leetcode-cn.com/problems/bold-words-in-string

from leetcode.allcode.competition.mypackage import *

class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:  # O(log(len(word)))
        cur = self.root
        for e in word:
            if e not in cur:
                cur[e] = {}
            cur = cur[e]
        cur['end'] = True


    def search(self, word: str) -> bool:
        cur = self.root
        for e in word:
            if e in cur:
                cur = cur[e]
            else:
                return False
        return 'end' in cur

    def longestPrefixMatch(self, s: str) -> bool:
        cur = self.root
        cnt = 0
        res = 0
        for e in s:
            if e in cur:
                cur = cur[e]
                cnt += 1
                if 'end' in cur:
                    res = cnt
            else:
                break
        return res


    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for e in prefix:
            if e in cur:
                cur = cur[e]
            else:
                return False
        return True

class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        tr = Trie()
        for w in words:
            tr.insert(w)

        n = len(s)
        l = 0
        ans = []
        while l < n:
            r = l
            for cur in range(l, n):
                m = tr.longestPrefixMatch(s[cur:])  # 匹配的最大长度
                if m == 0:
                    if cur >= r:
                        break
                r = max(r, cur + m)
                if r >= n:
                    break
            if l < r:
                if ans and ans[-1].endswith('</b>'):
                    ans[-1] = ans[-1][:-4] + s[l: r] + '</b>'
                else:
                    ans.append('<b>' + s[l: r] + '</b>')
            else:
                ans.append(s[l])
                r += 1
            l = r
        return ''.join(ans)


so = Solution()
print(so.addBoldTag("abcxyz123", ["abc","123"]))

print(so.addBoldTag("9NLRDk5b4igx8bZGb8wJayqENXuksNK0kIdI6pJN163YOxxmFl1KHwIsKcXw5u3pqcyVfoSt6wIniFJ1M2kkITtqC2nDCUvJFOffs2UeczTxKZfTYFQzHoVfcKSmHqq5eiNjczsjxxM8NyXzHFsa1N9YPLBGaCkuajGnmtoKzdIsNPFyPfjizIvgmD9KVG2BEwowiBlClPhKM9uGfbFSqXWELTdMnQzTHEaXDfiljZaufDYMXXu2Vk7QUKHNbj0ZTP9NP5dV10zAdv8B7xkLlwOR8yeTxTdAeInR8s1ZDjq8XM77Ru8RRdYEHN2XPorzCMjwngVM0mbKJ8Gq0XVmrwC7Na3Uvtb2DqU04Srn4BksGIueQVsnwdIBnLf5PtSK4jGE82T6T4sk06DIeJtiwsKlhjhMajQOypjSrRo0wEVwO0o0iDwqM7wbe0VvSXaJ3J34MjYDMP1QH9sUla9zFt9EFWQMcwGHik0ANzrPXr3wJlNvmr6BBxFutVShEucJykX12S1ni1Oby7anyhm5wGZruXyBqmht8m1fH68PxUFl5yJJRi31PA2OVlVpuE5tk4mU8dqP6NfJfeicLOEtfTBA1D5RFvsley0J2Ut8lAaZ",
                    ["QH9sUl","Uze8ek0NINV1xQ9MUYSEZ3fUumTqnFnLKmZ3KSsyfmcAQ64m6FL5yFuLZA5nhjwx6LmbYt6EB282xgB9jnhqwPqNatdNK8Emvn0C1rIswAVXNw6RpdxpmrJTfPu6v0BJsb2ihNT2BOmdp6SDZ9cyH4Td9YusYZCZshCgReY1pRvfnVZItnzNJfVdW74ubtJ2jw2l22WPQiJ1Mzl9AC2QBDvdbXToPlexChjb7keiZ5DeRZ04kezmM1BP75dDqHQBvYBOWm8vPNArZ5mua3kiKDrodvAuzujOwVaNFuIwf6PWmytMSz55gpfyMWKuRzjvJOv86WLKjInCHtZ73OM73ebuCRkwm7ZJDFgjhuHgE4QwlsPR9wazqKYE4qNhlpneGMiRiSR42bHyeCsv1xaFR8DiqpvnXx7brkvV4lFsBYtx4VzIbOtcgjtSCUjUVUpKIDMl1PuKOo2IcHChHLFIFQD3wcVoEWC8oeluDrbqbuSLpYlSlWSU6SDUrruYR7vRUtg5cW7RWQJrytKUr47dTd9AadhtaUUZ8Twf9Fq2MQmdSffaxaamFjcqXzy","JfeicLOEtfTBA1D5RFvsley0J2Ut8l","WELTdMnQzTHEaXDfiljZaufDYMXXu2Vk7QUKHNbj0ZTP9NP5dV10zAdv8B7xkLlwOR8yeTxTdAeInR8s1ZDjq8XM77Ru8RRdYEHN2XPorzCMjwngVM0mbKJ8Gq0XVmrw","RFlVw1HmmyVDWilgdFjhnDjOdq6jZAJOn8OrGy61np2yAqPS5328Y4cuHRS7BDTMMGxJBThj8aXqKXBywJlYcldVV4hX67lNUYqZXgbSvR2cdvYrGy","pJN163YOxxmFl1KHwIsKcXw5u3pqcyVfoSt6wIniFJ1M2kkITtqC2nDCUvJFOffs2UeczTxKZfTYFQzHoVfcKSmHqq5eiNjczsjxxM8NyXzHFsa1N9YPLBGaCkuajGnmtoKzdIsNPFyPfjizIvgmD9KVG2BEwowiBlClPhKM9uGfbFSqXWELTdMnQzTHEaXDfiljZaufDYMXXu2Vk7QUKHNbj0ZTP9NP5dV10zAdv8B7xkLlwOR8yeTxTdAeInR8s1ZDjq8XM77Ru8RRdYEHN2XPorzCMjwngVM0mbKJ8Gq0","L2NIjfp8jjHrMqLaAtEJUC7Kc4uxnAc9K8fKF1wNmA31mAYHryp73","1nE6Bb2QOeRS87RbfbHrIpjecaH2cVAmPhNThk8raF7Yn0aM9uDZa0Ij5s3BkpsOgHtYan34bchbeh7i8n3AiyiSPFWgAwzbmQX9rKqPZnCbJL5wc2doAHDQhr5jAGGedLKQdQMH9pRfaKeVUr8Qwhm6WP5HAqd1lqsmzaMyh","t8m1fH68PxUFl5yJJRi31PA2OVlVpuE5tk4mU8dqP6NfJfeicLOEtfTBA1D5RFvsley0J2U","nOkqMLkPvsnlzqRkmPp7Bip81gNhLyUhXCCZGEQQHTiRa8KWxKxoLVbBfrzN3PEwd11U","J34MjYDMP1QH9sU","LmhzTaGPNYQ58nrZAO4mzG2Xqqi86wu2XAwbdWlqmZDAZdBe2lkf2jvmqp8qIM0AZ8Nlk7xRVfvpUrSIXkjrfiThdnp9L67dzrKggABWd7UsvcUTM90vdHBc3Mq8ivLyVydAqwf1x7r55nLfJvrUjNuI11PZdS4hVqwvdl0N1zfFCWxVUpQwLVgBvrcD8VQxeVPvPR0HNFbRBxvEJv50YcNirfXNGDmBNIQvz87vk9LrJw1D39FhWhdPKDkZpGQ4qZYUof0nLSw6YoBDL2OGpDMk0GWlHjOdmg8uFOxaHO9DzPE2xTaWtVXZ1Gb8WQDbyQIBuk7fbLSebTdfRTzZbWC1djX116IxUJfPN6k1K1Wz9H6bFfp6EEkT0EgmCAqDendAopNH1XUPVgvnmbek7ora2teVGgmdQQQcenQQNn7YezKD1PsjNr1rtSVV5a8yr5EE1SVEyHpGX46NdnsG9EwKfaD3A56ypAV0ab0iCUdrm0Vs7QryC9hRJ2fTXDDoxaGMNa4pBkzaAQcmffW3igZKIA4MTqhG2roawsioCAH1FEnAO7jdDhO","04Srn4BksGIueQVsnwdIBnLf5PtSK4jGE82T6T4sk06DIeJtiwsKlhjhMajQOypjSrRo0wEVwO0o0iDwqM7wbe0VvSXaJ3J34MjYDMP1QH9sUla9zFt9EFWQMcwGH","sKlhjhMajQ","eQVsnwdIBnLf5PtSK4jGE82T6T4sk06DIeJtiwsKlhjhMajQOypjSrRo0wEVwO0o0iDwqM7wbe0VvSXaJ3J34MjYDMP1QH9sUla9zFt9EFWQMcwGHik0ANzrPXr3wJlNvmr6BBxFutVShEucJykX12S1ni1Oby7anyhm5wGZruXyBqmht8m1fH68PxUFl5yJJRi31PA2OVlVpuE5tk4mU8dqP6NfJfeicLO","OxxmFl1KHwIsKcXw5u3pqcyVfoSt6wIniFJ1M2kkITtqC2nDCUvJFOffs2UeczTxKZfTYFQzHoVfcKSmHqq5eiNjczsjxxM8NyXzHFsa1N9YPLBGaCkuajGnmtoKzdIsNPFyPfjizIvgmD9KVG2BEwowiBlClPhKM9uGfbFSqXWELTdMnQzTHEaXDfiljZaufDYMXXu2Vk7QUKHNbj0ZTP9NP5dV10zAdv8B7xkLlwOR8yeTxTdAeInR8s1ZDjq8XM77Ru8RRdYEHN2XPorzCMjwngVM0mbKJ8Gq0XVmrwC7Na3Uvtb2DqU04Srn4Bk","2s24R9tpcoeajmZlU7M1yLq3ag1WGOuqgwQF6TlAlLauGH1WQSjKvqHRxwPhg7YGcltBKb1GnuWB4sg8vqSmvsaT10ocDxz0ZBS3lTylHKBOdXVg676vOMw3cack5xnjgAe93JuBSrNGlxXzL7gUVqSVdoSfwXIdUNzevRZSBoLAUxnYrMDXCQPbHGgLEtowZ57ZoLgNWDembpo21iddAGylG0QglUZJevrZq6XPYV8AP1lpO35k9GRt7T2FJfFk5ek3lOcFpaOv9dmJonyswFdO1919Dl8HzRw49E7eFHYuMwgkkIu9eFAbdUE1oGcfACiqmtXc6a5ir9qNtbNxJgNFNnp6liQ0xf5QAERlgyB1r7LTBZmNZ2E00Sh8SzxV5OCdWbPmzCqqFnmd775fsyfUlobK7vhD1EKeOIAX5okEAJyRD77ztx1A20BsWfXSAp1VHc7Oyl5tpOGVvYiNE97ur66WQvxmn1jvd28FrnJUXdrHYt66lUOaoTipkbmN9s8uxBSB6nGwqBybd2kVr5vBd6TAH5peEwydbldrh7l3r38eACD3ToZqu6cUX8NzAoae1VmjvyWFiJg1t0ac5B0IJpv1eqmbq","w5u3pqcyVfoSt6w","8iEV4UfVBCu6MaPz30cu6Tp8ze0pMgkDmQT9OG4sWrHgAeAdDQmaBUhbRRUD7yWK5FGfGmwBNkAEGZw2db2OsP0nsuktGSn0WYmccydkuqEdYKovijXFWpH9FkwTRDzOt6xG2dgFd13ATXfc4fAGBwuSvi2RX8lwBod45zkmxs4byJKWxEvtZ2c7AyVYYEtkcj5jV9epkpYnO9zX5Oa5Hr6hoVfaX2Qr7QkeAJl0oqtyvaAfss54Z551cPbT4d5UPBiAI8pnjylCGpfXnEaSjH28zHW1P1LDjKzCDunCxkEWPxHRorl9E9zaRRw0197ExkM8oMSEd371sDlvkLTmbKclLLEIzqdvrgX28nZ1BoMSBtNpCb4kxzzTgojDn4oxeZJk66jRGS8dreQVjMlcOyIectIpwrhslOYeLK7hBQNliq7QxV27owiJytWA47W6br7Vv9RgsRQh9UUzKlM9vrmdRnm59C2CiWJZzEi9AvdxrtAcQmGFLA3yq0a95Nn5ysXfOLad0mZCtBrcFNLFl4iYV1QnsA2eoSbJV6Ia3nK6OtDT8lfnHPBR","S1ni1Oby7anyhm5wGZruXyBqmht8m1fH68PxUFl","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"]))



