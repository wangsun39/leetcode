# 现有一串神秘的密文 ciphertext，经调查，密文的特点和规则如下：
#
# 密文由非负整数组成
# 数字 0-25 分别对应字母 a-z
# 请根据上述规则将密文 ciphertext 解密为字母，并返回共有多少种解密结果。
#
#
#
#
#
# 示例 1：
#
# 输入：ciphertext = 216612
# 输出：6
# 解释：216612 解密后有 6 种不同的形式，分别是 "cbggbc"，"vggbc"，"vggm"，"cbggm"，"cqgbc" 和 "cqgm"
#
#
# 提示：
#
# 0 <= ciphertext < 231

from leetcode.allcode.competition.mypackage import *


class Solution:
    def crackNumber(self, ciphertext: int) -> int:
        ciphertext = str(ciphertext)
        n = len(ciphertext)
        dp1 = [0] * n
        dp2 = [0] * n
        dp1[0] = 1
        for i in range(1, n):
            dp1[i] = dp1[i - 1] + dp2[i - 1]
            if ciphertext[i - 1] != '0' and int(ciphertext[i - 1: i + 1]) < 26:
                if i > 1:
                    dp2[i] = dp1[i - 2] + dp2[i - 2]
                else:
                    dp2[i] = 1

        return dp1[-1] + dp2[-1]

so = Solution()
print(so.crackNumber(216612))




