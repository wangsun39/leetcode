# https://leetcode.cn/problems/check-if-dfs-strings-are-palindromes/solutions/2957704/mo-ban-dfs-shi-jian-chuo-manacher-suan-f-ttu6

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



