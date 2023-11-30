# 给你一个表示大整数的字符串 num ，和一个整数 k 。
#
# 如果某个整数是 num 中各位数字的一个 排列 且它的 值大于 num ，则称这个整数为 妙数 。可能存在很多妙数，但是只需要关注 值最小 的那些。
#
# 例如，num = "5489355142" ：
# 第 1 个最小妙数是 "5489355214"
# 第 2 个最小妙数是 "5489355241"
# 第 3 个最小妙数是 "5489355412"
# 第 4 个最小妙数是 "5489355421"
# 返回要得到第 k 个 最小妙数 需要对 num 执行的 相邻位数字交换的最小次数 。
#
# 测试用例是按存在第 k 个最小妙数而生成的。
#
#
#
# 示例 1：
#
# 输入：num = "5489355142", k = 4
# 输出：2
# 解释：第 4 个最小妙数是 "5489355421" ，要想得到这个数字：
# - 交换下标 7 和下标 8 对应的位："5489355142" -> "5489355412"
# - 交换下标 8 和下标 9 对应的位："5489355412" -> "5489355421"
# 示例 2：
#
# 输入：num = "11112", k = 4
# 输出：4
# 解释：第 4 个最小妙数是 "21111" ，要想得到这个数字：
# - 交换下标 3 和下标 4 对应的位："11112" -> "11121"
# - 交换下标 2 和下标 3 对应的位："11121" -> "11211"
# - 交换下标 1 和下标 2 对应的位："11211" -> "12111"
# - 交换下标 0 和下标 1 对应的位："12111" -> "21111"
# 示例 3：
#
# 输入：num = "00123", k = 1
# 输出：1
# 解释：第 1 个最小妙数是 "00132" ，要想得到这个数字：
# - 交换下标 3 和下标 4 对应的位："00123" -> "00132"
#
#
# 提示：
#
# 2 <= num.length <= 1000
# 1 <= k <= 1000
# num 仅由数字组成

from leetcode.allcode.competition.mypackage import *

class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        origin_num = list(num)
        lnum = list(num)
        n = len(num)
        def next_perm(l):
            j = 0
            for i in range(n - 2, -1, -1):
                if l[i] < l[i + 1]:
                    j = i
                    break
            k = n - 1  # 从右向左第一个比l[j]大的元素位置
            while True:
                if l[k] > l[j]:
                    break
                k -= 1
            l[k], l[j] = l[j], l[k]
            return l[:j + 1] + l[j + 1:][::-1]
        for _ in range(k):
            lnum = next_perm(lnum)
        ans = 0
        for i in range(n):
            if origin_num[i] == lnum[i]: continue
            for j in range(i + 1, n):
                if origin_num[j] == lnum[i]:
                    origin_num[i: j + 1] = [origin_num[j]] + origin_num[i: j]
                    break
            ans += (j - i)
        return ans





so = Solution()
print(so.getMinSwaps(num = "5489355142", k = 4))
print(so.getMinSwaps(num = "059", k = 5))
print(so.getMinSwaps(num = "11112", k = 4))
print(so.getMinSwaps(num = "00123", k = 1))




