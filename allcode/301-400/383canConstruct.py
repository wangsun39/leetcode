from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dic = defaultdict(int)
        for k in magazine:
            mag_dic[k] += 1
        for i in ransomNote:
            if i not in mag_dic or mag_dic[i] <= 0:
                return False
            mag_dic[i] -= 1
        return True




so = Solution()
print(so.canConstruct("a", "b"))
print(so.canConstruct("aa", "ab"))
print(so.canConstruct("aa", "aab"))

