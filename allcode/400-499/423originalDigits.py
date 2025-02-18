# 给你一个字符串 s ，其中包含字母顺序打乱的用英文单词表示的若干数字（0-9）。按 升序 返回原始的数字。
#
#
#
# 示例 1：
#
# 输入：s = "owoztneoer"
# 输出："012"
# 示例 2：
#
# 输入：s = "fviefuro"
# 输出："45"
#
#
# 提示：
#
# 1 <= s.length <= 105
# s[i] 为 ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"] 这些字符之一
# s 保证是一个符合题目要求的字符串

from leetcode.allcode.competition.mypackage import *

class Solution:
    def originalDigits(self, s: str) -> str:
        counter = Counter(s)
        d = [0] * 10
        if counter['z']:
            d[0] += counter['z']
            counter['e'] -= counter['z']
            counter['r'] -= counter['z']
            counter['o'] -= counter['z']
        if counter['u']:
            d[4] += counter['u']
            counter['f'] -= counter['u']
            counter['o'] -= counter['u']
            counter['r'] -= counter['u']
        if counter['x']:
            d[6] += counter['x']
            counter['s'] -= counter['x']
            counter['i'] -= counter['x']
        if counter['w']:
            d[2] += counter['w']
            counter['t'] -= counter['w']
            counter['o'] -= counter['w']
        if counter['g']:
            d[8] += counter['g']
            counter['e'] -= counter['g']
            counter['i'] -= counter['g']
            counter['h'] -= counter['g']
            counter['t'] -= counter['g']
        if counter['s']:
            d[7] += counter['s']
            counter['e'] -= counter['s'] * 2
            counter['v'] -= counter['s']
            counter['n'] -= counter['s']
        if counter['v']:
            d[5] += counter['v']
            counter['f'] -= counter['v']
            counter['i'] -= counter['v']
            counter['e'] -= counter['v']
        if counter['o']:
            d[1] += counter['o']
            counter['n'] -= counter['o']
            counter['e'] -= counter['o']
        if counter['t']:
            d[3] += counter['t']
            counter['h'] -= counter['t']
            counter['r'] -= counter['t']
            counter['e'] -= counter['t'] * 2
        if counter['i']:
            d[9] += counter['i']

        arr = []
        for i, x in enumerate(d):
            arr.append(str(i) * x)
        return ''.join(arr)



so = Solution()
print(so.originalDigits("owoztneoer"))




