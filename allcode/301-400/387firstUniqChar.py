# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
#
#  
#
# 示例：
#
# s = "leetcode"
# 返回 0
#
# s = "loveleetcode"
# 返回 2
#  
#
# 提示：你可以假定该字符串只包含小写字母。



from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {} # 'a' -> idx   字符在s中的首次出现的位置，-1表示已经出现重复了
        N = len(s)
        for idx, e in enumerate(s):
            if e not in d:
                d[e] = idx
            else:
                d[e] = N
        res = min(d.values())
        return res if res < N else -1


so = Solution()
print(so.firstUniqChar("leetcode"))
print(so.firstUniqChar("loveleetcode"))

