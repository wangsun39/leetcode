from typing import List
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        hash_dict = {}  # 把所以字符串的反序串放入字典中
        res = []
        for i, e in enumerate(words):
            hash_dict[e[::-1]] = i
        print(hash_dict)
        def isPalindrome(x):
            return x == x[::-1]
        def findPairs(idx, word):
            i = len(word)
            while i >= 0:
                if isPalindrome(word[i:]): # 后缀是回文
                    if word[:i] in hash_dict: # 前缀逆序在哈希表中
                        pair = hash_dict[word[:i]]
                        if idx != pair:
                            res.append([idx, pair])
                if isPalindrome(word[:i]) and 0 != i: # 前缀是回文
                    if word[i:] in hash_dict: # 后缀逆序在哈希表中
                        pair = hash_dict[word[i:]]
                        if idx != pair:
                            res.append([pair, idx])
                i -= 1
        for i, e in enumerate(words):
            findPairs(i, e)
        return res


so = Solution()
print(so.palindromePairs(["a",""]))
print(so.palindromePairs(["abcd","dcba","lls","s","sssll"]))
print(so.palindromePairs( ["bat","tab","cat"]))




