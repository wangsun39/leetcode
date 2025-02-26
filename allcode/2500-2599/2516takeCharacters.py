# 给你一个由字符 'a'、'b'、'c' 组成的字符串 s 和一个非负整数 k 。每分钟，你可以选择取走 s 最左侧 还是 最右侧 的那个字符。
#
# 你必须取走每种字符 至少 k 个，返回需要的 最少 分钟数；如果无法取到，则返回 -1 。
#
#
#
# 示例 1：
#
# 输入：s = "aabaaaacaabc", k = 2
# 输出：8
# 解释：
# 从 s 的左侧取三个字符，现在共取到两个字符 'a' 、一个字符 'b' 。
# 从 s 的右侧取五个字符，现在共取到四个字符 'a' 、两个字符 'b' 和两个字符 'c' 。
# 共需要 3 + 5 = 8 分钟。
# 可以证明需要的最少分钟数是 8 。
# 示例 2：
#
# 输入：s = "a", k = 1
# 输出：-1
# 解释：无法取到一个字符 'b' 或者 'c'，所以返回 -1 。
#
#
# 提示：
#
# 1 <= s.length <= 105
# s 仅由字母 'a'、'b'、'c' 组成
# 0 <= k <= s.length

from leetcode.allcode.competition.mypackage import *

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0: return 0
        n = len(s)
        left, right = {'a': [0], 'b': [0], 'c': [0]}, {'a': [0], 'b': [0], 'c': [0]}
        for i in range(n):
            left['a'].append(left['a'][-1])
            right['a'].append(right['a'][-1])
            left['b'].append(left['b'][-1])
            right['b'].append(right['b'][-1])
            left['c'].append(left['c'][-1])
            right['c'].append(right['c'][-1])
            left[s[i]][-1] += 1
            right[s[n - i - 1]][-1] += 1
        print(left)
        if left['a'][-1] < k or left['b'][-1] < k or left['c'][-1] < k:
            return -1
        for i in range(n + 1):
            if left['a'][i] >= k and left['b'][i] >= k and left['c'][i] >= k:
                pl = i
                ans = i
                break
        for i in range(n + 1):
            if right['a'][i] >= k and right['b'][i] >= k and right['c'][i] >= k:
                pr = i
                ans = min(ans, pr)
                break
        pl = 1
        while pr > 0:
            while left['a'][pl] + right['a'][pr] >= k and left['b'][pl] + right['b'][pr] >= k and left['c'][pl] + right['c'][pr] >= k and pr > 0:
                ans = min(ans, pl + pr)
                pr -= 1
            pl += 1
            if left['a'][pl] + right['a'][pr] >= k and left['b'][pl] + right['b'][pr] >= k and left['c'][pl] + right['c'][pr] >= k:
                ans = min(ans, pl + pr)
        return ans


so = Solution()
print(so.takeCharacters(s = "aabaaaacaabc", k = 2))
print(so.takeCharacters(s = "a", k = 1))
# print(so.takeCharacters(s = "aabaaaacaabc", k = 2))




