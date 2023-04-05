from typing import List
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alienDict = {}
        def makeAlienDict():
            idx = 0
            for e in order:
                alienDict[e] = idx
                idx += 1
            return
        def lessThanEqual(s1, s2):
            idx = 0
            L1, L2 = len(s1), len(s2)
            N = min(L1, L2)
            while idx < N:
                if alienDict[s1[idx]] > alienDict[s2[idx]]:
                    return False
                elif alienDict[s1[idx]] < alienDict[s2[idx]]:
                    return True
                idx += 1
            if L1 > N:
                return False
            return True
        # if len(words) <= 1:
        #     return True
        makeAlienDict()
        print(alienDict)
        cur = words[0]
        for word in words[1:]:
            if not lessThanEqual(cur, word):
                return False
            cur = word
        return True


so = Solution()
print(so.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"))
print(so.isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"))
print(so.isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"))
#print(so.largestComponentSize(3660))

