# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
# 示例1:
#
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 示例 2:
#
# 输入: s = "rat", t = "car"
# 输出: false
# 说明:
# 你可以假设字符串只包含小写字母。
#
# 进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        L1, L2 = [0 for _ in range(26)],  [0 for _ in range(26)]
        asca = ord('a')
        N = len(s)
        for i in range(N):
            L1[ord(s[i]) - asca] += 1
            L2[ord(t[i]) - asca] += 1
        for i in range(26):
            if L1[i] != L2[i]:
                return False
        return True


so = Solution()

print(so.isAnagram("anagram", "nagaram"))
# print(so.isAnagram("2*3-4*5"))

