# 给你一个下标从 0 开始的字符串 s ，你需要找到两个 不重叠的回文 子字符串，它们的长度都必须为 奇数 ，使得它们长度的乘积最大。
#
# 更正式地，你想要选择四个整数 i ，j ，k ，l ，使得 0 <= i <= j < k <= l < s.length ，且子字符串 s[i...j] 和 s[k...l] 都是回文串且长度为奇数。s[i...j] 表示下标从 i 到 j 且 包含 两端下标的子字符串。
#
# 请你返回两个不重叠回文子字符串长度的 最大 乘积。
#
# 回文字符串 指的是一个从前往后读和从后往前读一模一样的字符串。子字符串 指的是一个字符串中一段连续字符。
#
#
#
# 示例 1：
#
# 输入：s = "ababbb"
# 输出：9
# 解释：子字符串 "aba" 和 "bbb" 为奇数长度的回文串。乘积为 3 * 3 = 9 。
# 示例 2：
#
# 输入：s = "zaaaxbbby"
# 输出：9
# 解释：子字符串 "aaa" 和 "bbb" 为奇数长度的回文串。乘积为 3 * 3 = 9 。
#
#
# 提示：
#
# 2 <= s.length <= 105
# s 只包含小写英文字母。


from leetcode.allcode.competition.mypackage import *

class Manacher:
    def __init__(self, s: str):
        self.str = list(s)

        # Manacher 模板
        # 将 self.str 改造为 t，这样就不需要讨论 n 的奇偶性，因为新串 t 的每个回文子串都是奇回文串（都有回文中心）
        # self.str 和 t 的下标转换关系：
        # (self.str_i+1)*2 = ti
        # ti/2-1 = self.str_i
        # ti 为偶数，对应奇回文串（从 2 开始）
        # ti 为奇数，对应偶回文串（从 3 开始）
        t = '#'.join(['^'] + self.str + ['$'])

        # 定义一个奇回文串的回文半径=(长度+1)/2，即保留回文中心，去掉一侧后的剩余字符串的长度
        # halfLen[i] 表示在 t 上的以 t[i] 为回文中心的最长回文子串的回文半径
        # 即 [i-halfLen[i]+1,i+halfLen[i]-1] 是 t 上的一个回文子串
        self.halfLen = [0] * (len(t) - 2)
        self.halfLen[1] = 1
        # boxR 表示当前右边界下标最大的回文子串的右边界下标+1
        # boxM 为该回文子串的中心位置，二者的关系为 r=mid+halfLen[mid]
        boxM = boxR = 0
        for i in range(2, len(self.halfLen)):
            hl = 1
            if i < boxR:
                # 记 i 关于 boxM 的对称位置 i'=boxM*2-i
                # 若以 i' 为中心的最长回文子串范围超出了以 boxM 为中心的回文串的范围（即 i+halfLen[i'] >= boxR）
                # 则 halfLen[i] 应先初始化为已知的回文半径 boxR-i，然后再继续暴力匹配
                # 否则 halfLen[i] 与 halfLen[i'] 相等
                hl = min(self.halfLen[boxM * 2 - i], boxR - i)
            # 暴力扩展
            # 算法的复杂度取决于这部分执行的次数
            # 由于扩展之后 boxR 必然会更新（右移），且扩展的的次数就是 boxR 右移的次数
            # 因此算法的复杂度 = O(len(t)) = O(n)
            while t[i - hl] == t[i + hl]:
                hl += 1
                boxM, boxR = i, i + hl
            self.halfLen[i] = hl

        # t 中回文子串的长度为 hl*2-1
        # 由于其中 # 的数量总是比字母的数量多 1
        # 因此其在 self.str 中对应的回文子串的长度为 hl-1
        # 这一结论可用在 isPalindrome 中

    # 判断左闭右开区间 [l,r) 是否为回文串  0<=l<r<=n
    # 根据下标转换关系得到 self.str 的 [l,r) 子串在 t 中对应的回文中心下标为 l+r+1
    # 需要满足 halfLen[l + r + 1] - 1 >= r - l，即 halfLen[l + r + 1] > r - l
    def isPalindrome(self, l: int, r: int) -> bool:
        return self.halfLen[l + r + 1] > r - l

    def getSrcHalfLen(self, str_i: int) -> int:
        return (self.halfLen[(str_i + 1) * 2] + 1) // 2


class Solution:
    def maxProduct(self, s: str) -> int:
        mnc = Manacher(s)
        n = len(s)
        left, right = [1] * n, [1] * n  # s[:i+1] 和 s[i:] 中最长的奇数长度回文长度

        center = 0
        for i in range(1, n):
            left[i] = left[i - 1]
            while center <= i:
                if center + mnc.getSrcHalfLen(center) - 1 <= i:
                    left[i] = max(left[i], mnc.getSrcHalfLen(center) * 2 - 1)
                    center += 1
                else:
                    left[i] = max(left[i], (i - center) * 2 + 1)
                    break

        center = n - 1
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1]
            while center >= i:
                if center - mnc.getSrcHalfLen(center) + 1 >= i:
                    right[i] = max(right[i], mnc.getSrcHalfLen(center) * 2 - 1)
                    center -= 1
                else:
                    right[i] = max(right[i], (center - i) * 2 + 1)
                    break
        ans = 1
        for i in range(n - 1):
            ans = max((ans, left[i] * right[i + 1]))
        return ans

so = Solution()
print(so.maxProduct("ggbswiymmlevedhkbdhntnhdbkhdevelmmyiwsbgg"))
print(so.maxProduct("ababbb"))
print(so.maxProduct("zaaaxbbby"))


