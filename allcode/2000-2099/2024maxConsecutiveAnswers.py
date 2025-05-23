# 一位老师正在出一场由 n道判断题构成的考试，每道题的答案为 true （用 'T' 表示）或者 false （用 'F'表示）。老师想增加学生对自己做出答案的不确定性，方法是最大化有 连续相同结果的题数。（也就是连续出现 true 或者连续出现 false）。
#
# 给你一个字符串answerKey，其中answerKey[i]是第 i个问题的正确结果。除此以外，还给你一个整数 k，表示你能进行以下操作的最多次数：
#
# 每次操作中，将问题的正确答案改为'T' 或者'F'（也就是将 answerKey[i] 改为'T'或者'F'）。
# 请你返回在不超过 k次操作的情况下，最大连续 'T'或者 'F'的数目。
#
#
#
# 示例 1：
#
# 输入：answerKey = "TTFF", k = 2
# 输出：4
# 解释：我们可以将两个 'F' 都变为 'T' ，得到 answerKey = "TTTT" 。
# 总共有四个连续的 'T' 。
# 示例 2：
#
# 输入：answerKey = "TFFT", k = 1
# 输出：3
# 解释：我们可以将最前面的 'T' 换成 'F' ，得到 answerKey = "FFFT" 。
# 或者，我们可以将第二个 'T' 换成 'F' ，得到 answerKey = "TFFF" 。
# 两种情况下，都有三个连续的 'F' 。
# 示例 3：
#
# 输入：answerKey = "TTFTTFTT", k = 1
# 输出：5
# 解释：我们可以将第一个 'F' 换成 'T' ，得到 answerKey = "TTTTTFTT" 。
# 或者我们可以将第二个 'F' 换成 'T' ，得到 answerKey = "TTFTTTTT" 。
# 两种情况下，都有五个连续的 'T' 。
#
#
# 提示：
#
# n == answerKey.length
# 1 <= n <= 5 * 104
# answerKey[i]要么是'T' ，要么是'F'
# 1 <= k <= n



class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def getMaxVal(type):
            left, right = 0, 0
            target = k
            res = 0
            while right < len(answerKey):
                if answerKey[right] != type:
                    target -= 1
                if target < 0:
                    if answerKey[left] != type:
                        target += 1
                    left += 1
                    target += 1
                else:
                    res = max(res, right - left + 1)
                    right += 1

            return res
        res1 = getMaxVal('T')
        res2 = getMaxVal('F')
        return max(res1, res2)

so = Solution()
print(so.maxConsecutiveAnswers("TTFF", k = 2))
print(so.maxConsecutiveAnswers("TFFT", k = 1))
print(so.maxConsecutiveAnswers("TTFTTFTT", k = 1))
