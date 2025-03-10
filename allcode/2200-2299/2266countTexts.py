# Alice 在给 Bob 用手机打字。数字到字母的 对应 如下图所示。
#
#
#
# 为了 打出 一个字母，Alice 需要 按 对应字母 i 次，i 是该字母在这个按键上所处的位置。
#
# 比方说，为了按出字母 's' ，Alice 需要按 '7' 四次。类似的， Alice 需要按 '5' 两次得到字母  'k' 。
# 注意，数字 '0' 和 '1' 不映射到任何字母，所以 Alice 不 使用它们。
# 但是，由于传输的错误，Bob 没有收到 Alice 打字的字母信息，反而收到了 按键的字符串信息 。
#
# 比方说，Alice 发出的信息为 "bob" ，Bob 将收到字符串 "2266622" 。
# 给你一个字符串 pressedKeys ，表示 Bob 收到的字符串，请你返回 Alice 总共可能发出多少种文字信息 。
#
# 由于答案可能很大，将它对 109 + 7 取余 后返回。
#
#
#
# 示例 1：
#
# 输入：pressedKeys = "22233"
# 输出：8
# 解释：
# Alice 可能发出的文字信息包括：
# "aaadd", "abdd", "badd", "cdd", "aaae", "abe", "bae" 和 "ce" 。
# 由于总共有 8 种可能的信息，所以我们返回 8 。
# 示例 2：
#
# 输入：pressedKeys = "222222222222222222222222222222222222"
# 输出：82876089
# 解释：
# 总共有 2082876103 种 Alice 可能发出的文字信息。
# 由于我们需要将答案对 109 + 7 取余，所以我们返回 2082876103 % (109 + 7) = 82876089 。
#
#
# 提示：
#
# 1 <= pressedKeys.length <= 105
# pressedKeys 只包含数字 '2' 到 '9' 。


# Map = [['U' for _ in range(n)] for _ in range(m)]

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countTexts1(self, pressedKeys: str) -> int:
        Max = int(1e9 + 7)

        @lru_cache(None)
        def calc(totalL, maxSubL):
            if totalL == 0:
                return 0
            num = 0
            for l in range(1, maxSubL + 1):
                if l > totalL:
                    return num
                if l == totalL:
                    num += 1
                    continue
                num += calc(totalL - l, maxSubL)
                num %= Max
            return num
        def getMaxSubL(e):
            if e not in ('97') :
                return 3
            else:
                return 4
        print(calc(4, 4))
        pressedKeys += 'Z'
        pressedKeys = 'Z' + pressedKeys
        n = len(pressedKeys)
        cur = 'Z'
        curL = 1
        ans = 1
        for i in range(1, n):
            if cur != pressedKeys[i]:
                num = calc(curL, getMaxSubL(pressedKeys[i - 1]))
                cur, curL = pressedKeys[i], 1
                if num == 0:
                    continue
                ans *= num
                ans %= Max
            else:
                curL += 1
        return ans % Max


    def countTexts(self, pressedKeys: str) -> int:
        # 2025/1/19 简化写法
        n = len(pressedKeys)
        MOD = 10 ** 9 + 7
        d = [0, 0, 3, 3, 3, 3, 3, 4, 3, 4]
        @cache
        def dfs(start):
            if start >= n - 1: return 1
            res = 0
            for i in range(d[int(pressedKeys[start])]):
                if start + i >= n or pressedKeys[start] != pressedKeys[start + i]: break
                res += dfs(start + i + 1)
                res %= MOD
            return res
        return dfs(0)



so = Solution()
print(so.countTexts("22"))
print(so.countTexts("55555555999977779555"))
print(so.countTexts("444479999555588866"))
print(so.countTexts("22233"))
print(so.countTexts("222222222222222222222222222222222222"))




